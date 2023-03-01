from typing import Tuple, List, Union
import tensorflow as tf
from data.augmentation import augmentation

def _get_paths(dataset_path: Union[str, List]) -> tf.Tensor:
    images = []
    masks = []

    if isinstance(dataset_path, str):
        images = sorted(tf.io.gfile.glob(dataset_path + "**/*.jpg"))
        masks = sorted(tf.io.gfile.glob(dataset_path + "**/*.png"))

    elif isinstance(dataset_path, List):
        for path in dataset_path:
            images += sorted(tf.io.gfile.glob(path + "**/*.jpg"))
            masks += sorted(tf.io.gfile.glob(path + "**/*.png"))
        
    return tf.transpose([images, masks])


def _load(x: str, y: str, image_shape: Tuple, mask_shape: Tuple) -> Tuple:
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


def load_image(path: str, image_size: Tuple, num_channels: int, interpolation="bilinear") -> tf.Tensor:
    """Load an image from a path and resize it."""
    img = tf.io.read_file(path)
    img = tf.image.decode_image(img, channels=num_channels, expand_animations=False)
    img = tf.image.resize(img, image_size, method=interpolation)
    img.set_shape((image_size[0], image_size[1], num_channels))
    return img


def load_segmentation_dataset(
    dir_path: Union[str, List],
    image_shape: Tuple,
    mask_shape: Tuple
) -> tf.data.Dataset:
    
    dataset = tf.data.Dataset.from_tensor_slices(_get_paths(dir_path))
    return dataset.map(
        lambda pair: _load(pair[0], pair[1], image_shape, mask_shape),
        num_parallel_calls=tf.data.AUTOTUNE,
    )


def load_train_dataset(
    dir_path: Union[str, List],
    image_shape: Tuple,
    mask_shape: Tuple,
    buffer_size=1000,
    batch=8,
) -> tf.data.Dataset:
    
    dataset = ( 
        load_segmentation_dataset(dir_path, image_shape, mask_shape)
        .shuffle(buffer_size)
        .batch(batch)
        .prefetch(buffer_size=tf.data.AUTOTUNE)
        .map(lambda x, y: augmentation(x, y), num_parallel_calls=tf.data.AUTOTUNE)
    )
    
    return dataset

