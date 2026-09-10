"""
preprocessing.py

Preprocessing pipeline for the food-101-5-classes dataset:
- resizing
- intensity normalization
- data augmentation (train only)
- on-the-fly data loading via image_dataset_from_directory

Usage:
    from preprocessing import load_datasets, build_pipeline

    train_ds, val_ds, test_ds, class_names = load_datasets("../../data/food-101-5-classes")
    train_ds, val_ds, test_ds = build_pipeline(train_ds, val_ds, test_ds)
"""

from pathlib import Path

import tensorflow as tf
from keras import layers

# --- Config ---
IMG_SIZE = (224, 224)
        # state-of-the-art networks are typically trained on 224x224x3
BATCH_SIZE = 32
        # The model loads 32 images at a time, computes their predictions, calculates the error (loss)
        # updates its internal parameters (weights) once based on those 32 images.
VALIDATION_SPLIT = 0.15
        # 85 % data to train 15 % to test
SEED = 42
        # random number generator

def load_datasets(data_dir: str | Path):
    """
    Load train/val/test datasets from a directory structured as:
    data/food-101-5-classes/<class_name>/*.jpg

    Returns raw (unbatched preprocessing) datasets — resizing to IMG_SIZE and
    batching happen here, but normalization/augmentation are applied later
    in build_pipeline() so they can be attached to the model instead of the
    dataset (see module docstring / lecture notes on why).
    """
    data_dir = Path(data_dir)

    # 1. Load 70% of the images as the training set
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.3,  # Reserve 30% total for validation + test
        subset="training",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
    )

    # 2. Load the remaining 30% of the images
    val_and_test_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.3,
        subset="validation",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
    )

    # 3. Split the 30% subset evenly into validation (15%) and test (15%)
    val_batches = tf.data.experimental.cardinality(val_and_test_ds) // 2
    val_ds = val_and_test_ds.take(val_batches)
    test_ds = val_and_test_ds.skip(val_batches)

    class_names = train_ds.class_names
    return train_ds, val_ds, test_ds, class_names


# --- Normalization ---
# Rescale pixel values from [0, 255] to [0, 1]
normalization_layer = layers.Rescaling(1.0 / 255)


# --- Data augmentation ---
# Only ever applied to the TRAINING set, and only during training
# (Keras automatically disables these layers at inference time).
data_augmentation = tf.keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.05),
        layers.RandomZoom(0.1),
        layers.RandomContrast(0.1),
    ],
    name="data_augmentation",
)


def build_pipeline(train_ds, val_ds, test_ds):
    """Attach normalization (all splits) and augmentation (train only),
    then configure caching/prefetching for performance.

    Note: normalization and augmentation are applied as part of the tf.data
    pipeline here for clarity. Alternatively, you can skip this step and put
    `normalization_layer` / `data_augmentation` directly as the first layers
    of your model instead — both approaches are common, pick one and stay
    consistent so you don't normalize twice.
    """
    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.map(
        lambda x, y: (normalization_layer(data_augmentation(x, training=True)), y),
        num_parallel_calls=AUTOTUNE,
    )
    val_ds = val_ds.map(
        lambda x, y: (normalization_layer(x), y),
        num_parallel_calls=AUTOTUNE,
    )
    test_ds = test_ds.map(
        lambda x, y: (normalization_layer(x), y),
        num_parallel_calls=AUTOTUNE,
    )

    train_ds = train_ds.cache().shuffle(1000).prefetch(AUTOTUNE)
    val_ds = val_ds.cache().prefetch(AUTOTUNE)
    test_ds = test_ds.cache().prefetch(AUTOTUNE)

    return train_ds, val_ds, test_ds


if __name__ == "__main__":
    # Quick sanity check when running this file directly:
    # python preprocessing.py
    train_ds, val_ds, test_ds, class_names = load_datasets("../../data/food-101-5-classes")
    print(f"Classes ({len(class_names)}): {class_names}")

    train_ds, val_ds, test_ds = build_pipeline(train_ds, val_ds, test_ds)

    for images, labels in train_ds.take(1):
        print("Batch shape:", images.shape)
        print("Pixel value range after normalization:", images.numpy().min(), images.numpy().max())
        print("Labels:", labels.numpy())
