"""
preprocessing.py

Preprocessing pipeline for the food-101-5-classes dataset:
- resizing
- intensity normalization
- data augmentation (train only)
- on-the-fly ("lazy") image loading, so we never hold the whole dataset in memory

Split strategy: sklearn's train_test_split on file PATHS + LABELS (not on the
images themselves), stratified so every class is proportionally represented
in train/val/test. This is more explicit and precise than letting
image_dataset_from_directory split automatically.

How labels get attached to images:
    We never manually tag anything. Each image's label comes from the name
    of the folder it lives in (see _collect_paths_and_labels below).
    food-101-5-classes/baklava/*.jpg  -> label "baklava"
    food-101-5-classes/pizza/*.jpg    -> label "pizza"

Usage:
    from preprocessing import load_datasets, build_pipeline

    train_ds, val_ds, test_ds, class_names = load_datasets("../../data/food-101-5-classes")
    train_ds, val_ds, test_ds = build_pipeline(train_ds, val_ds, test_ds)
"""

from pathlib import Path

import numpy as np
import tensorflow as tf
from keras import layers
from sklearn.model_selection import train_test_split

# --- Config ---
IMG_SIZE = (224, 224)
        # state-of-the-art networks are typically trained on 224x224x3
BATCH_SIZE = 32
        # the model processes 32 images at a time before each weight update
TEST_SIZE = 0.15
        # 15% of all images held out as the test set, never seen during training
VAL_SIZE = 0.15
        # 15% of all images held out as the validation set
SEED = 42
        # fixes randomness so the split is reproducible


def _collect_paths_and_labels(data_dir: Path):
    """Scan data_dir for class subfolders and collect (path, label) pairs.

    This is where images get "connected" to their classifier label: we don't
    tag anything by hand, we just read which folder each image sits in.
    Every file under data_dir/baklava/ automatically gets the label
    "baklava" (encoded as an integer index), every file under
    data_dir/pizza/ gets "pizza", and so on.
    """
    class_names = sorted([d.name for d in data_dir.iterdir() if d.is_dir()])
    class_to_index = {name: idx for idx, name in enumerate(class_names)}

    paths = []
    labels = []
    for class_name in class_names:
        class_dir = data_dir / class_name
        for img_path in class_dir.glob("*.jpg"):
            paths.append(str(img_path))
            labels.append(class_to_index[class_name])

    return np.array(paths), np.array(labels), class_names


def load_datasets(data_dir: str | Path):
    """Split into train/val/test with sklearn's train_test_split (stratified
    on the label array), then wrap each split in a tf.data.Dataset that
    loads and resizes images lazily -- only when a batch is actually
    requested. This is the "data loader" / "image generator" idea from the
    lecture: images never all sit in memory at once.
    """
    data_dir = Path(data_dir)
    paths, labels, class_names = _collect_paths_and_labels(data_dir)

    # Step 1: carve off the test set first
    train_val_paths, test_paths, train_val_labels, test_labels = train_test_split(
        paths, labels,
        test_size=TEST_SIZE,
        stratify=labels,        # keep class proportions equal across splits
        random_state=SEED,
    )

    # Step 2: split what's left into train and validation.
    # VAL_SIZE is meant as a fraction of the ORIGINAL dataset, so we scale it
    # up relative to what remains after removing the test set.
    relative_val_size = VAL_SIZE / (1 - TEST_SIZE)
    train_paths, val_paths, train_labels, val_labels = train_test_split(
        train_val_paths, train_val_labels,
        test_size=relative_val_size,
        stratify=train_val_labels,
        random_state=SEED,
    )

    train_ds = _make_dataset(train_paths, train_labels, shuffle=True)
    val_ds = _make_dataset(val_paths, val_labels, shuffle=False)
    test_ds = _make_dataset(test_paths, test_labels, shuffle=False)

    return train_ds, val_ds, test_ds, class_names


def _load_and_resize(path, label):
    """Read ONE image file from disk, decode it, and resize it.

    This function is the actual "image generator" / lazy-loading step: it
    only runs when tf.data needs the next image for a batch, never for the
    whole dataset upfront. That's how we avoid running out of memory.
    """
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, IMG_SIZE)
    return image, label


def _make_dataset(paths, labels, shuffle: bool) -> tf.data.Dataset:
    """Build a tf.data.Dataset of (path, label) pairs and attach the lazy
    loading step. Note this dataset only holds STRINGS and INTS until
    .map(_load_and_resize) actually pulls and decodes an image."""
    ds = tf.data.Dataset.from_tensor_slices((paths, labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(paths), seed=SEED)
    ds = ds.map(_load_and_resize, num_parallel_calls=tf.data.AUTOTUNE)
    ds = ds.batch(BATCH_SIZE)
    return ds


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
    then configure prefetching for performance.

    Note: normalization and augmentation are applied here as part of the
    tf.data pipeline for clarity. Alternatively, you can put
    `normalization_layer` / `data_augmentation` directly as the first layers
    of your model instead -- both approaches are common, pick one and stay
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

    train_ds = train_ds.prefetch(AUTOTUNE)
    val_ds = val_ds.prefetch(AUTOTUNE)
    test_ds = test_ds.prefetch(AUTOTUNE)

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
