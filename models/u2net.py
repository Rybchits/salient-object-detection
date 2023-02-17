from keras import losses, Model, Input
from keras.layers import Layer, Conv2D, ReLU, BatchNormalization, UpSampling2D, MaxPool2D, Activation
import tensorflow as tf

bce = losses.BinaryCrossentropy()

def bce_loss(y_true, y_pred):
    y_pred = tf.expand_dims(y_pred, axis=-1)
    loss0 = bce(y_true, y_pred[0])
    loss1 = bce(y_true, y_pred[1])
    loss2 = bce(y_true, y_pred[2])
    loss3 = bce(y_true, y_pred[3])
    loss4 = bce(y_true, y_pred[4])
    loss5 = bce(y_true, y_pred[5])
    loss6 = bce(y_true, y_pred[6])
    return loss0 + loss1 + loss2 + loss3 + loss4 + loss5 + loss6


class ConvBNReLU(Layer):
    def __init__(self, num_filters, trainable=True, dirate=1, name=None, **kwargs):
        super().__init__(trainable, name, **kwargs)

        self.conv = Conv2D(
            filters=num_filters,
            kernel_size=(3, 3),
            padding="same",
            strides=(1, 1),
            dilation_rate=dirate
        )

        self.bn = BatchNormalization()
        self.relu = ReLU()

    def call(self, inputs):
        x = self.conv(inputs)
        x = self.bn(x)
        x = self.relu(x)
        return x
    


class RSU7(Layer):
    def __init__(self, mid_chanels, out_chanels):
        super(RSU7, self).__init__()
        
        self.mid_chanels = mid_chanels
        self.out_chanels = out_chanels
        
        # encode
        self.conv0 = ConvBNReLU(out_chanels, name="rsu7_conv0")

        self.conv1 = ConvBNReLU(mid_chanels, name="rsu7_conv1")
        self.pool1 = MaxPool2D(2, strides=(2, 2), name="rsu7_pool1")

        self.conv2 = ConvBNReLU(mid_chanels, name="rsu7_conv2")
        self.pool2 = MaxPool2D(2, strides=(2, 2), name="rsu7_pool2")

        self.conv3 = ConvBNReLU(mid_chanels, name="rsu7_conv3")
        self.pool3 = MaxPool2D(2, strides=(2, 2), name="rsu7_pool3")

        self.conv4 = ConvBNReLU(mid_chanels, name="rsu7_conv4")
        self.pool4 = MaxPool2D(2, strides=(2, 2), name="rsu7_pool4")

        self.conv5 = ConvBNReLU(mid_chanels, name="rsu7_conv5")
        self.pool5 = MaxPool2D(2, strides=(2, 2), name="rsu7_pool5")

        #bottleneck layers
        self.conv6 = ConvBNReLU(mid_chanels, name="rsu7_conv6")
        self.conv7 = ConvBNReLU(mid_chanels, dirate=2, name="rsu7_conv7")
        self.conv6_d = ConvBNReLU(mid_chanels, name="rsu7_conv6_d")

        # decode
        self.upsample_1 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu7_upsample_1")
        self.conv5_d = ConvBNReLU(mid_chanels, name="rsu7_conv5_d")
        self.upsample_2 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu7_upsample_2")
        self.conv4_d = ConvBNReLU(mid_chanels, name="rsu7_conv4_d")
        self.upsample_3 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu7_upsample_3")
        self.conv3_d = ConvBNReLU(mid_chanels, name="rsu7_conv3_d")
        self.upsample_4 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu7_upsample_4")
        self.conv2_d = ConvBNReLU(mid_chanels, name="rsu7_conv2_d")
        self.upsample_5 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu7_upsample_5")
        self.conv1_d = ConvBNReLU(out_chanels, name="rsu7_conv1_d")
    
    def call(self, inputs):
        hx = inputs

        # convolution + convolution + pooling (save result for skip)
        hxin = self.conv0(hx)
        x_skip1 = self.conv1(hxin)
        hx = self.pool1(x_skip1)

        # convolution + pooling 
        x_skip2 = self.conv2(hx)
        hx = self.pool2(x_skip2)

        # convolution + pooling
        x_skip3 = self.conv3(hx)
        hx = self.pool3(x_skip3)

        # convolution + pooling
        x_skip4 = self.conv4(hx)
        hx = self.pool4(x_skip4)

        # convolution + pooling
        x_skip5 = self.conv5(hx)
        hx = self.pool5(x_skip5)

        # bottleneck
        btlneck1 = self.conv6(hx)
        btlneck2 = self.conv7(btlneck1)

        # decode
        decode = self.conv6_d(tf.concat([btlneck2, btlneck1], axis=3))
        decode = self.upsample_5(decode)

        decode = self.conv5_d(tf.concat([decode, x_skip5], axis=3))
        decode = self.upsample_4(decode)

        decode = self.conv4_d(tf.concat([decode, x_skip4], axis=3))
        decode = self.upsample_3(decode)

        decode = self.conv3_d(tf.concat([decode, x_skip3], axis=3))
        decode = self.upsample_2(decode)

        decode =  self.conv2_d(tf.concat([decode, x_skip2], axis=3))
        decode = self.upsample_1(decode)

        decode = self.conv1_d(tf.concat([decode, x_skip1], axis=3))
        
        return decode + hxin
    
    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'mid_chanels': self.mid_chanels,
            'out_chanels': self.out_chanels,
        })
        return config


class RSU6(Layer):
    def __init__(self, mid_chanels, out_chanels):
        super(RSU6, self).__init__()
        
        self.mid_chanels = mid_chanels
        self.out_chanels = out_chanels
        
        self.conv0 = ConvBNReLU(out_chanels, name="rsu6_conv0")

        self.conv1 = ConvBNReLU(mid_chanels, name="rsu6_conv1")
        self.pool1 = MaxPool2D(2, strides=(2, 2), name="rsu6_pool1")

        self.conv2 = ConvBNReLU(mid_chanels, name="rsu6_conv2")
        self.pool2 = MaxPool2D(2, strides=(2, 2), name="rsu6_pool2")

        self.conv3 = ConvBNReLU(mid_chanels, name="rsu6_conv3")
        self.pool3 = MaxPool2D(2, strides=(2, 2), name="rsu6_pool3")

        self.conv4 = ConvBNReLU(mid_chanels, name="rsu6_conv4")
        self.pool4 = MaxPool2D(2, strides=(2, 2), name="rsu6_pool4")

        self.conv5 = ConvBNReLU(mid_chanels, name="rsu6_conv5")
        self.conv6 = ConvBNReLU(mid_chanels, dirate=2, name="rsu6_conv6")

        self.conv5_d = ConvBNReLU(mid_chanels, name="rsu6_conv5_d")

        self.upsample_1 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu6_upsample_1")
        self.conv4_d = ConvBNReLU(mid_chanels, name="rsu6_conv4_d")
        self.upsample_2 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu6_upsample_2")
        self.conv3_d = ConvBNReLU(mid_chanels, name="rsu6_conv3_d")
        self.upsample_3 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu6_upsample_3")
        self.conv2_d = ConvBNReLU(mid_chanels, name="rsu6_conv2_d")
        self.upsample_4 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu6_upsample_4")
        self.conv1_d = ConvBNReLU(out_chanels, name="rsu6_conv1_d")


    def call(self, inputs):
        # encode
        hx = inputs
        hxin = self.conv0(hx)

        x_skip1 = self.conv1(hxin)
        hx = self.pool1(x_skip1)

        x_skip2 = self.conv2(hx)
        hx = self.pool2(x_skip2)

        x_skip3 = self.conv3(hx)
        hx = self.pool3(x_skip3)

        x_skip4 = self.conv4(hx)
        hx = self.pool4(x_skip4)

        # bottleneck
        btlneck1 = self.conv5(hx)
        btlneck2 = self.conv6(btlneck1)

        # decode
        decode = self.conv5_d(tf.concat([btlneck2, btlneck1], axis=3))
        decode = self.upsample_4(decode)

        decode = self.conv4_d(tf.concat([decode, x_skip4], axis=3))
        decode = self.upsample_3(decode)

        decode = self.conv3_d(tf.concat([decode, x_skip3], axis=3))
        decode = self.upsample_2(decode)

        decode =  self.conv2_d(tf.concat([decode, x_skip2], axis=3))
        decode = self.upsample_1(decode)

        decode = self.conv1_d(tf.concat([decode, x_skip1], axis=3))
        
        return decode + hxin
    
    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'mid_chanels': self.mid_chanels,
            'out_chanels': self.out_chanels,
        })
        return config



class RSU5(Layer):
    def __init__(self, mid_chanels, out_chanels):
        super(RSU5, self).__init__()
        
        self.mid_chanels = mid_chanels
        self.out_chanels = out_chanels
        
        self.conv0 = ConvBNReLU(out_chanels, name="rsu5_conv0")
        self.conv1 = ConvBNReLU(mid_chanels, name="rsu5_conv1")

        self.pool1 = MaxPool2D(2, strides=(2, 2), name="rsu5_pool1")
        self.conv2 = ConvBNReLU(mid_chanels, name="rsu5_conv2")

        self.pool2 = MaxPool2D(2, strides=(2, 2), name="rsu5_pool2")
        self.conv3 = ConvBNReLU(mid_chanels, name="rsu5_conv3")

        self.pool3 = MaxPool2D(2, strides=(2, 2), name="rsu5_pool3")
        self.conv4 = ConvBNReLU(mid_chanels, name="rsu5_conv4")

        self.conv5 = ConvBNReLU(mid_chanels, dirate=2, name="rsu5_conv5")
        self.conv4_d = ConvBNReLU(mid_chanels, name="rsu5_conv4_d")

        self.upsample_3 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu5_upsample_3")
        self.conv3_d = ConvBNReLU(mid_chanels, name="rsu5_conv3_d")

        self.upsample_2 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu5_upsample_2")
        self.conv2_d = ConvBNReLU(mid_chanels, name="rsu5_conv2_d")

        self.upsample_1 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu5_upsample_1")
        self.conv1_d = ConvBNReLU(out_chanels, name="rsu5_conv1_d")
        

    def call(self, inputs):
        # encode
        hx = inputs
        hxin = self.conv0(hx)

        x_skip1 = self.conv1(hxin)
        hx = self.pool1(x_skip1)

        x_skip2 = self.conv2(hx)
        hx = self.pool2(x_skip2)

        x_skip3 = self.conv3(hx)
        hx = self.pool3(x_skip3)

        # bottleneck
        btlneck1 = self.conv4(hx)
        btlneck2 = self.conv5(btlneck1)

        # decode
        decode = self.conv4_d(tf.concat([btlneck2, btlneck1], axis=3))
        decode = self.upsample_3(decode)

        decode = self.conv3_d(tf.concat([decode, x_skip3], axis=3))
        decode = self.upsample_2(decode)

        decode = self.conv2_d(tf.concat([decode, x_skip2], axis=3))
        decode = self.upsample_1(decode)

        decode =  self.conv1_d(tf.concat([decode, x_skip1], axis=3))
        
        return decode + hxin
    
    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'mid_chanels': self.mid_chanels,
            'out_chanels': self.out_chanels,
        })
        return config
    

class RSU4(Layer):
    def __init__(self, mid_chanels, out_chanels):
        super(RSU4, self).__init__()
        
        self.mid_chanels = mid_chanels
        self.out_chanels = out_chanels
        
        self.conv0 = ConvBNReLU(out_chanels, name="rsu4_conv0")
        self.conv1 = ConvBNReLU(mid_chanels, name="rsu4_conv1")

        self.conv2 = ConvBNReLU(mid_chanels, name="rsu4_conv2")
        self.pool1 = MaxPool2D(2, strides=(2, 2), name="rsu4_pool1")

        self.conv3 = ConvBNReLU(mid_chanels, name="rsu4_conv3")
        self.pool2 = MaxPool2D(2, strides=(2, 2), name="rsu4_pool2")

        self.conv4 = ConvBNReLU(mid_chanels, dirate=2, name="rsu4_conv6")
        self.conv3_d = ConvBNReLU(mid_chanels)

        self.upsample_2 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu4_upsample_2")
        self.conv2_d = ConvBNReLU(mid_chanels, name="rsu4_conv2_d")

        self.upsample_1 = UpSampling2D(size=(2, 2), interpolation='bilinear', name="rsu4_upsample_1")
        self.conv1_d = ConvBNReLU(out_chanels, name="rsu4_conv1_d")

        
    def call(self, inputs):
        # encode
        hx = inputs
        hxin = self.conv0(hx)

        x_skip1 = self.conv1(hxin)
        hx = self.pool1(x_skip1)

        x_skip2 = self.conv2(hx)
        hx = self.pool2(x_skip2)

        # bottleneck
        btlneck1 = self.conv3(hx)
        btlneck2 = self.conv4(btlneck1)

        # decode
        decode = self.conv3_d(tf.concat([btlneck2, btlneck1], axis=3))

        decode = self.upsample_2(decode)
        decode = self.conv2_d(tf.concat([decode, x_skip2], axis=3))

        decode = self.upsample_1(decode)
        decode =  self.conv1_d(tf.concat([decode, x_skip1], axis=3))
        
        return decode + hxin
    
    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'mid_chanels': self.mid_chanels,
            'out_chanels': self.out_chanels,
        })
        return config


class RSU4F(Layer):
    def __init__(self, mid_chanels, out_chanels):
        super(RSU4F, self).__init__()
        
        self.mid_chanels = mid_chanels
        self.out_chanels = out_chanels
        
        self.conv0 = ConvBNReLU(out_chanels, dirate=1)
        self.conv1 = ConvBNReLU(mid_chanels, dirate=1)
        self.conv2 = ConvBNReLU(mid_chanels, dirate=2)
        self.conv3 = ConvBNReLU(mid_chanels, dirate=4)
        self.conv4 = ConvBNReLU(mid_chanels, dirate=8)
        
        self.conv3_d = ConvBNReLU(mid_chanels, dirate=4)
        self.conv2_d = ConvBNReLU(mid_chanels, dirate=2)
        self.conv1_d = ConvBNReLU(out_chanels, dirate=1)

        
    def call(self, inputs):
        hx = inputs
        hxin = self.conv0(hx)
        
        x_skip1 = self.conv1(hxin)
        x_skip2 = self.conv2(x_skip1)

        x_3 = self.conv3(x_skip2)
        x_4 = self.conv4(x_3)

        decode = self.conv3_d(tf.concat([x_4, x_3], axis=3))
        decode = self.conv2_d(tf.concat([decode, x_skip2], axis=3))
        decode = self.conv1_d(tf.concat([decode, x_skip1], axis=3))

        return decode + hxin
    
    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'mid_chanels': self.mid_chanels,
            'out_chanels': self.out_chanels,
        })
        return config


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
