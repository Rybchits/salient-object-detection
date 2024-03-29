from keras import Model, Input
from keras.layers import Conv2D, UpSampling2D, MaxPool2D, Activation, Rescaling
import tensorflow as tf

from models.u2net.layers import RSU4, RSU4F, RSU5, RSU6, RSU7
from utils.resizing import ResizingExt


def export_u2net_model(model, image_height, image_width):
    @tf.function(input_signature=[tf.TensorSpec([None, None, 3], tf.uint8)])
    def serving_fn(image):
        processed_img, input_shape = ResizingExt(height=image_height, width=image_width)(image) # Resize
        processed_img = Rescaling(1/255)(processed_img)         # Scale
        processed_img = tf.expand_dims(processed_img, axis=0)
        mask = model(processed_img)[0][0]
        mask = tf.image.resize(mask, input_shape)
        mask = tf.math.round(mask)
        mask = tf.cast(mask, tf.uint8)
        return {"mask": mask}
    
    return serving_fn


def U2NET(out_ch=1, shape_image=(None, None, 3)):
    inputs = Input(shape=shape_image)

    hx = inputs
    hx1 = RSU7(32, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx1)

    hx2 = RSU6(32, 128)(hx)
    hx = MaxPool2D((2, 2), 2)(hx2)

    hx3 = RSU5(64, 256)(hx)
    hx = MaxPool2D((2, 2), 2)(hx3)

    hx4 = RSU4(128, 512)(hx)
    hx = MaxPool2D((2, 2), 2)(hx4)

    hx5 = RSU4F(256, 512)(hx)
    hx = MaxPool2D((2, 2), 2)(hx5)

    hx6 = RSU4F(256, 512)(hx)
    hx6up = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx6)
    side6 = UpSampling2D(size=(32, 32), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx6))

    hx5d = RSU4F(256, 512)(tf.concat([hx6up, hx5], axis=3))
    hx5dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx5d)
    side5 = UpSampling2D(size=(16, 16), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx5d))

    hx4d = RSU4(128, 256)(tf.concat([hx5dup, hx4], axis=3))
    hx4dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx4d)
    side4 = UpSampling2D(size=(8, 8), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx4d))

    hx3d = RSU5(64, 128)(tf.concat([hx4dup, hx3], axis=3))
    hx3dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx3d)
    side3 = UpSampling2D(size=(4, 4), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx3d))

    hx2d = RSU6(32, 64)(tf.concat([hx3dup, hx2], axis=3))
    hx2dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx2d)
    side2 = UpSampling2D(size=(2, 2), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx2d))

    hx1d = RSU7(16, 64)(tf.concat([hx2dup, hx1], axis=3))
    side1 = Conv2D(out_ch, (3, 3), padding='same')(hx1d)

    fused_output = Conv2D(out_ch, (1, 1), padding='same')(tf.concat([side1, side2, side3, side4, side5, side6], axis=3))

    sig = Activation(tf.nn.sigmoid)

    outputs = [sig(fused_output), sig(side1), sig(side2), sig(side3), sig(side4), sig(side5), sig(side6)]
    return Model(inputs=inputs, outputs=outputs, name='u2netmodel')


def U2NETP(out_ch=1, shape_image=(None, None, 3)):
    inputs = Input(shape=shape_image)

    hx = inputs
    hx1 = RSU7(16, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx1)

    hx2 = RSU6(16, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx2)

    hx3 = RSU5(16, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx3)

    hx4 = RSU4(16, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx4)

    hx5 = RSU4F(16, 64)(hx)
    hx = MaxPool2D((2, 2), 2)(hx5)

    hx6 = RSU4F(16, 64)(hx)
    hx6up = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx6)
    side6 = UpSampling2D(size=(32, 32), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx6))

    hx5d = RSU4F(16, 64)(tf.concat([hx6up, hx5], axis=3))
    hx5dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx5d)
    side5 = UpSampling2D(size=(16, 16), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx5d))

    hx4d = RSU4(16, 64)(tf.concat([hx5dup, hx4], axis=3))
    hx4dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx4d)
    side4 = UpSampling2D(size=(8, 8), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx4d))

    hx3d = RSU5(16, 64)(tf.concat([hx4dup, hx3], axis=3))
    hx3dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx3d)
    side3 = UpSampling2D(size=(4, 4), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx3d))

    hx2d = RSU6(16, 64)(tf.concat([hx3dup, hx2], axis=3))
    hx2dup = UpSampling2D(size=(2, 2), interpolation='bilinear')(hx2d)
    side2 = UpSampling2D(size=(2, 2), interpolation='bilinear')(Conv2D(out_ch, (3, 3), padding='same')(hx2d))

    hx1d = RSU7(16, 64)(tf.concat([hx2dup, hx1], axis=3))
    side1 = Conv2D(out_ch, (3, 3), padding='same')(hx1d)

    fused_output = Conv2D(out_ch, (1, 1), padding='same')(tf.concat([side1, side2, side3, side4, side5, side6], axis=3))

    sig = Activation(tf.nn.sigmoid)

    outputs = [sig(fused_output), sig(side1), sig(side2), sig(side3), sig(side4), sig(side5), sig(side6)]

    return Model(inputs=inputs, outputs=outputs, name='u2netpmodel')

