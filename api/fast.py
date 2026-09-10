import io
import json
import os
from contextlib import asynccontextmanager
from pathlib import Path

import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import tensorflow as tf  # noqa: E402

# Paths are resolved relative to this file, not the working directory,
# so the app starts correctly no matter where uvicorn is launched from.
REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = REPO_ROOT / "artifacts"

MODEL_PATH = Path(os.getenv("MODEL_PATH", ARTIFACTS / "gluten_guard_mobilenetv2.keras"))
CLASSES_PATH = Path(os.getenv("CLASSES_PATH", ARTIFACTS / "class_names.json"))
IMG_SIZE = (224, 224)

# Load the model once at startup, not per request - otherwise every call
# would take several seconds.
state: dict = {"model": None, "class_names": []}


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not MODEL_PATH.exists():
        raise RuntimeError(f"Model not found: {MODEL_PATH}")
    if not CLASSES_PATH.exists():
        raise RuntimeError(f"Class names not found: {CLASSES_PATH}")

    state["model"] = tf.keras.models.load_model(MODEL_PATH)

    data = json.loads(CLASSES_PATH.read_text())
    state["class_names"] = data["class_names"] if isinstance(data, dict) else data

    n_out = state["model"].output_shape[-1]
    if n_out != len(state["class_names"]):
        raise RuntimeError(
            f"Model has {n_out} outputs but {len(state['class_names'])} class names."
        )

    print(f"Model loaded: {MODEL_PATH.name}, {len(state['class_names'])} classes")
    yield
    state.clear()


app = FastAPI(title="Gluten-Guard API", lifespan=lifespan)


# Root endpoint
@app.get("/")
def root():
    """Root endpoint returning a greeting."""
    return {"greeting": "hello"}


# Dummy endpoint
@app.get("/dummy")
def dummy(number: int):
    """Dummy endpoint that returns the square of the input number."""
    return {"result": number ** 2}


@app.get("/health")
def health():
    """Liveness check - reports whether the model is loaded."""
    return {
        "status": "ok" if state.get("model") is not None else "model not loaded",
        "num_classes": len(state.get("class_names", [])),
    }


def preprocess(raw: bytes) -> np.ndarray:
    """Bring an uploaded image into the exact shape the model saw during training.

    IMPORTANT: do not divide by 255. The rescaling to [-1, 1] is a layer inside the
    model. Dividing here as well produces values in [-1, -0.99] and therefore garbage
    predictions - without anything crashing.
    """
    try:
        img = Image.open(io.BytesIO(raw))
    except Exception:
        raise HTTPException(status_code=400, detail="File is not a readable image.")

    img = img.convert("RGB").resize(IMG_SIZE)
    arr = np.array(img, dtype=np.float32)      # 0-255
    return np.expand_dims(arr, axis=0)          # (1, 224, 224, 3)


@app.post("/predict")
async def predict(file: UploadFile = File(...), top_k: int = 5):
    """Upload an image, get the top-k predicted dishes back."""
    model = state.get("model")
    class_names = state.get("class_names", [])

    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    raw = await file.read()
    if not raw:
        raise HTTPException(status_code=400, detail="Empty file.")

    probs = model.predict(preprocess(raw), verbose=0)[0]

    k = max(1, min(top_k, len(class_names)))
    top_idx = np.argsort(probs)[::-1][:k]

    return {
        "filename": file.filename,
        "predictions": [
            {"label": class_names[i], "confidence": round(float(probs[i]), 4)}
            for i in top_idx
        ],
    }
