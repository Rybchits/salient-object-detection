from keras.metrics import Accuracy, MeanIoU
import tensorflow as tf

class RoundedAccuracy(Accuracy):
    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.math.round(y_pred)
        return super(RoundedAccuracy,self).update_state(y_true, y_pred, sample_weight)
    

class RoundedMeanIoU(MeanIoU):
    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.math.round(y_pred)
        return super(RoundedMeanIoU,self).update_state(y_true, y_pred, sample_weight)
    

def FBetaScore(precision: float, recall: float, squared_beta: float = 0.3) -> float:
    return ((1 + squared_beta) * precision * recall)/(squared_beta * precision + recall)