import matplotlib.pyplot as plt
import tensorflow as tf

from keras.utils import array_to_img

def display(display_list, titles, figsize=(12, 12)):
    assert len(display_list) == len(titles), "Размер списка изображений должен соотвествовать размеру списка заголовков"
    
    plt.figure(figsize=figsize)
    
    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i+1)
        plt.title(titles[i])
        plt.imshow(array_to_img(display_list[i]))
    plt.show()


class DisplayCallback(tf.keras.callbacks.Callback):
    def __init__(self, image, mask, freq, total_epochs=None):
        super().__init__() 
        self.freq = freq
        self.image = image
        self.mask = mask
        self.total_epochs = total_epochs
        
    def on_epoch_end(self, epoch, logs=None):
        if epoch % self.freq == 0 or epoch == self.total_epochs-1:
            out = self.model(tf.expand_dims(self.image, axis=0))
            print ('\nSample Prediction after epoch {}\n'.format(epoch + 1))
            display(
                [self.image, self.mask, out[0][0], tf.math.round(out[0][0])],
                ["Input image", "True mask", "Predicted mask", "Rounded mask"]
            )