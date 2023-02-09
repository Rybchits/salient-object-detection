import os
import tensorflow as tf
from data.augmentation import augmentation

from glob import glob

def _get_paths(path):
    images = sorted(glob(os.path.join(path, "Image/*")))
    masks = sorted(glob(os.path.join(path, "Mask/*")))
    return images, masks


def _read_image(path, shape):
    x = tf.keras.utils.load_img(path=path, target_size=shape)
    x = tf.keras.utils.img_to_array(x)
    x = x / 255.0
    x = tf.cast(x, tf.float32)
    return x


def _read_mask(path, shape):
    x = tf.keras.utils.load_img(path=path, color_mode = "grayscale", target_size=shape)
    x = tf.keras.utils.img_to_array(x)
    x = x / 255.0
    x = tf.cast(x, tf.float32)
    return x


def _preprocess(x, y, image_shape, mask_shape):
    def f(x, y):
        x = x.decode()
        y = y.decode()

        x = _read_image(x, image_shape[:-1])
        y = _read_mask(y, mask_shape[:-1])

        return x, y

    images, masks = tf.numpy_function(f, [x, y], [tf.float32, tf.float32])
    images.set_shape(image_shape)
    masks.set_shape(mask_shape)
    return images, masks


# ./DUTS-TR/
# ./DUTS-TE/
def get_dataset(dir_path, image_shape, mask_shape, batch=8, needAugmentation=False):
    x, y = _get_paths(dir_path)
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    dataset = dataset.map(lambda x, y: _preprocess(x, y, image_shape, mask_shape), num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.shuffle(buffer_size=1000)
    dataset = dataset.batch(batch)

    if needAugmentation:
        dataset = dataset.repeat(2)
        dataset = dataset.map(lambda x, y: augmentation(x, y), num_parallel_calls=tf.data.AUTOTUNE)
    
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    return dataset

