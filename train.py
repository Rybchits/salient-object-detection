from data.loader import load_segmentation_dataset, load_train_dataset
from models.u2net import U2NET

import keras
from keras.metrics import MeanSquaredError, Precision, Recall

TRAIN_DATASETS = ["DUTS-TR", "DIS5K\DIS-TE1", "DIS5K\DIS-TE2", "DIS5K\DIS-TE3", "DIS5K\DIS-TE4", "DIS5K\DIS-TR", "DIS5K\DIS-VD"]
TEST_PATH = "./datasets/DUTS-TE/"

IMAGE_SHAPE = (320, 320, 3)
MASK_SHAPE = (320, 320, 1)

# Training
BATCH_SIZE = 8
EPOCHS = 100
LEARNING_RATE = 0.001


train_dataset = load_train_dataset(
    dir_path = ["./datasets/{}/".format(i) for i in TRAIN_DATASETS],
    image_shape = IMAGE_SHAPE,
    mask_shape = MASK_SHAPE,
    batch=BATCH_SIZE,
)

test_dataset = load_segmentation_dataset(
    dir_path = TEST_PATH,
    image_shape = IMAGE_SHAPE,
    mask_shape = MASK_SHAPE,
    need_scaling = True
).batch(BATCH_SIZE)


adam = keras.optimizers.Adam(learning_rate=LEARNING_RATE, beta_1=.9, beta_2=.999, epsilon=1e-08)
bce = keras.losses.BinaryCrossentropy()

model = U2NET()
model.compile(optimizer=adam, loss=bce, metrics=[[MeanSquaredError(), Precision(0.5), Recall(0.5)]] + [None] * 6)

callbacks = [
    keras.callbacks.TensorBoard(log_dir="./logs"),
    keras.callbacks.BackupAndRestore("./bkp"),
    keras.callbacks.ModelCheckpoint("./saved_models/u2net/best", monitor="val_activation_mean_squared_error", save_best_only=True),
]

history = model.fit(train_dataset, validation_data=test_dataset, callbacks=callbacks, epochs=EPOCHS, verbose=0)
model.save('./saved_models/u2net/latest', include_optimizer=False)