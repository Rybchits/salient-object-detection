
import json
import requests
import numpy as np
import tensorflow as tf
import os
import random

from data.loader import load_image
from utils.display import display

IMAGE_SHAPE = (320, 320, 3)
TEST_DATASET = './datasets/DUTS-TR/'

def get_rest_url(model_name='u2net', host='127.0.0.1', port='8501', task='predict', version=None):
    url = "http://{host}:{port}/v1/models/{model_name}".format(host=host, port=port, model_name=model_name)
    if version:
        url += '/versions/{version}'.format(version=version)
    url += ':{task}'.format(task=task)
    return url


def get_model_prediction(image, model_name='u2net'):
    """ This function sends request to the URL and get prediction in the form of response"""
    url = get_rest_url(model_name)

    data = json.dumps({"instances": image.numpy().tolist()})
    headers = {"content-type": "application/json"}

    # Send the post request and get response
    rv = requests.post(url, data=data, headers=headers)
    return rv

def main():
    images = sorted(tf.io.gfile.glob(TEST_DATASET + "**/*.jpg"))
    pathfile = random.choice(images)
    image = load_image(pathfile, num_channels=IMAGE_SHAPE[-1])
    image = tf.cast(image, tf.uint8)

    if image.shape[0] > 2048 or image.shape[1] > 2048:
        print("Разрешение входного изображения не должно превышать 2048 на 2048...")
        return

    try:
        prediction = get_model_prediction(image)
        print(prediction.status_code)

        if prediction.status_code == 400:
            print(prediction.json()['error'])

        elif prediction.status_code == 200:
            mask = prediction.json()['predictions']
            display(
                [image, np.multiply(image, mask), mask], 
                ["Input image", "Masked image", "Predicted mask"],
                figsize=(10, 4),
            )
        else:
            print(prediction.status_code)

    except Exception as e:
        print('Что-то пошло не так...')


if __name__ == '__main__':
    main()
