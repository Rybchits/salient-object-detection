from typing import Tuple

import tensorflow as tf

def aug_color_image(image: tf.Tensor) -> tf.Tensor:
    """Color augmentation
    Args:
        image: Image
    Returns:
        Augmented image
    """
    image = tf.image.random_hue(image, 0.15)
    image = tf.image.random_saturation(image, 0.5, 2.0)
    image = tf.image.random_brightness(image, 0.8)
    image = tf.image.random_contrast(image, 0.85, 1.15)
    return image


def aug_rotate_image_and_mask(image: tf.Tensor, mask: tf.Tensor) -> Tuple[tf.Tensor, tf.Tensor]:
    """Rotate augmentation
    Args:
        image: Image
        mask: Image
    Returns:
        A tuple of augmented image and mask
    """
    k = tf.random.uniform(shape=[], minval=0, maxval=4, dtype=tf.int32)
    return tf.image.rot90(image, k), tf.image.rot90(mask, k)
