
import json
import requests
import numpy as np
import tensorflow as tf
import random

from data.loader import load_image
from utils.display import display

IMAGE_SHAPE = (320, 320, 3)
TEST_DATASET = './datasets/DUTS-TE/'

def get_rest_url(model_name='u2net', host='127.0.0.1', port='8501', task='predict', version=None):
    url = "http://{host}:{port}/v1/models/{model_name}".format(host=host, port=port, model_name=model_name)
    if version:
        url += '/versions/{version}'.format(version=version)
    url += ':{task}'.format(task=task)
    return url


def get_model_prediction(image, model_name='u2net'):
    """ This function sends request to the URL and get prediction in the form of response"""
    url = get_rest_url(model_name)

    data = json.dumps({"signature_name": "serving_default", "instances": image.numpy().tolist()})
    headers = {"content-type": "application/json"}

    # Send the post request and get response   
    rv = requests.post(url, data=data, headers=headers)
    return rv.json()['predictions']


if __name__ == '__main__':
    images = sorted(tf.io.gfile.glob(TEST_DATASET + "**/*.jpg"))
    pathfile = random.choice(images)

    image = load_image(pathfile, IMAGE_SHAPE[:-1], IMAGE_SHAPE[-1])
    prediction = get_model_prediction(image)

    display(
        [image, np.multiply(image, prediction), prediction], 
        ["Input image", "Masked image", "Predicted mask"],
        figsize=(10, 4),
    )