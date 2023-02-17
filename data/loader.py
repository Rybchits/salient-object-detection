import tensorflow as tf
from glob import glob

from data.augmentation import augmentation


def _get_paths(images_path, masks_path):
    images = sorted(glob(images_path))
    masks = sorted(glob(masks_path))
    return images, masks


def _load(x, y, image_shape, mask_shape):
    def f(x, y):
        x = x.decode()
        y = y.decode()

        x = load_image(x, image_shape[:-1], image_shape[-1])
        y = load_image(y, mask_shape[:-1], mask_shape[-1])

        return x, y

    image, mask = tf.numpy_function(f, [x, y], [tf.float32, tf.float32])

    image /= 255.0
    mask /= 255.0
    
    image.set_shape(image_shape)
    mask.set_shape(mask_shape)

    return image, mask


def load_image(path, image_size, num_channels, interpolation="bilinear"):
    """Load an image from a path and resize it."""
    img = tf.io.read_file(path)
    img = tf.compat.v2.image.decode_image(img, channels=num_channels, expand_animations=False)

    img = tf.compat.v2.image.resize(img, image_size, method=interpolation)
        
    img.set_shape((image_size[0], image_size[1], num_channels))
    return img


def load_dataset(images_dir_path, masks_dir_path, image_shape, mask_shape):
    x, y = _get_paths(images_dir_path, masks_dir_path)
    dataset = (
        tf.data.Dataset.from_tensor_slices((x, y))
        .map(lambda x, y: _load(x, y, image_shape, mask_shape), num_parallel_calls=tf.data.AUTOTUNE)
    )
    return dataset


def load_train_dataset(
    images_dir_path,
    masks_dir_path,
    image_shape,
    mask_shape,
    buffer_size=1000,
    batch=8,
    needAugmentation=False
):
    dataset = (
        load_dataset(images_dir_path, masks_dir_path, image_shape, mask_shape)
        .shuffle(buffer_size)
        .batch(batch)
    )

    if needAugmentation:
        dataset = dataset.map(lambda x, y: augmentation(x, y), num_parallel_calls=tf.data.AUTOTUNE)
    
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    return dataset

