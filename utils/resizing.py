from keras import layers
import tensorflow as tf

class ResizingExt(layers.Layer):
    def __init__(
        self,
        height,
        width,
        interpolation="bilinear",
        crop_to_aspect_ratio=False,
        **kwargs,
    ):
        self.height = height
        self.width = width
        self.interpolation = interpolation
        self.crop_to_aspect_ratio = crop_to_aspect_ratio
        super().__init__(**kwargs, trainable=False, name="resizing_ext")

    def call(self, inputs):
        size = tf.shape(inputs)[:2]
        x = layers.Resizing(self.height, self.width, self.interpolation, self.crop_to_aspect_ratio)(inputs)
        return x, size
    
    def get_config(self):
        config = {
            "height": self.height,
            "width": self.width,
            "interpolation": self.interpolation,
            "crop_to_aspect_ratio": self.crop_to_aspect_ratio,
        }
        base_config = super().get_config()
        return dict(list(base_config.items()) + list(config.items()))
