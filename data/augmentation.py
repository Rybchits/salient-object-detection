from typing import Tuple

import tensorflow as tf

def _aug_color(image: tf.Tensor) -> tf.Tensor:
    """Color augmentation
    Args:
        image: Image
    Returns:
        Augmented image
    """
    image = tf.image.random_hue(image, 0.2)
    image = tf.image.random_saturation(image, 0.6, 1.0)
    image = tf.image.random_brightness(image, 0.4)
    image = tf.image.random_contrast(image, 0.7, 2.1)
    return image


def _aug_rotate(image: tf.Tensor, mask: tf.Tensor) -> Tuple[tf.Tensor, tf.Tensor]:
    """Rotate augmentation
    Args:
        image: Image
        mask: Image
    Returns:
        Augmented image and mask
    """
    k = tf.random.uniform(shape=[], minval=0, maxval=4, dtype=tf.int32)
    return tf.image.rot90(image, k), tf.image.rot90(mask, k)


def augmentation(image: tf.Tensor, mask: tf.Tensor) -> Tuple[tf.Tensor, tf.Tensor]:
    image = _aug_color(image)
    return _aug_rotate(image, mask)