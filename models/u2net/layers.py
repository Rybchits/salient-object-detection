from keras.layers import Layer, Conv2D, ReLU, BatchNormalization, UpSampling2D, MaxPool2D
import tensorflow as tf


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