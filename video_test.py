import cv2
import tensorflow as tf
import numpy as np
import os, shutil, sys
import subprocess

from enum import Enum
from typing import Any, List, Tuple

class Task(Enum):
    CLIPPING = 1
    VISUALIZATION_OBJECT = 2
    VISUALIZATION_AREA = 3


SEQUENCE_IMAGES_DIR = './temp_seq_images'
DEFAULT_OUTPUT_FILE = './outputs/output_{0}.mp4'.format(len(os.listdir('./outputs'))+1)
ROLLING_WINDOW_SIZE = 25
VERTICAL_FORMAT = (16,9)
TYPE_TASK = Task.VISUALIZATION_AREA


def main():
    if len(sys.argv) == 1:
        print('Ошибка: пропущен видеофайл')
        return

    model = get_saved_model()
    video_path = sys.argv[1]

    if TYPE_TASK == Task.CLIPPING:
        run_clipping_video_by_salient_area_task(video_path, model)

    elif TYPE_TASK == Task.VISUALIZATION_OBJECT:
        run_visualization_salient_object_task(video_path, model)
    
    elif TYPE_TASK == Task.VISUALIZATION_AREA:
        run_visualization_salient_area_task(video_path, model)


def run_visualization_salient_object_task(video_path: str, model: Any, need_log: bool = True):
    os.makedirs(SEQUENCE_IMAGES_DIR, exist_ok=True)

    video_cap = cv2.VideoCapture(video_path)
    number_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if (video_cap.isOpened() == False):
        print("Ошибка открытия видеофайла")
    else:
        print("Определение основного объекта по кадрам...")
        for i in range(1, number_frames+1):
            ret, frame = video_cap.read()

            if ret == True:
                image_tensor = tf.convert_to_tensor(frame)
                salient_mask = model.signatures["serving_default"](image_tensor)['mask'].numpy()
                mask = cv2.cvtColor(salient_mask*255, cv2.COLOR_GRAY2RGB)
                writefile = '{0:s}/img{1:05d}.jpg'.format(SEQUENCE_IMAGES_DIR, i)
                cv2.imwrite(writefile, highlight_by_mask(frame, mask))

                if need_log:
                    print_progress_bar(i, number_frames)
            else:
                print("Ошибка чтения {0} кадра".format(i))
                break

    video_cap.release()        
    create_video_using_ffmpeg()
    shutil.rmtree(SEQUENCE_IMAGES_DIR)


def run_visualization_salient_area_task(video_path: str, model: Any):
    video_cap = cv2.VideoCapture(video_path)
    width  = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    result_video_shape = vertical_shape_from_horizontal((height, width), VERTICAL_FORMAT)

    # Найти левый верхний угол прямоугольника с основным объектом для каждого кадра видео
    corners = find_all_corners(video_cap, model, result_video_shape)
    video_cap.release()

    # Сглаживание
    corners = list(zip(
        rolling_list(list(map(lambda pair: pair[0], corners)), ROLLING_WINDOW_SIZE),
        rolling_list(list(map(lambda pair: pair[1], corners)), ROLLING_WINDOW_SIZE)))

    os.makedirs(SEQUENCE_IMAGES_DIR, exist_ok=True)

    # Обрезка видео
    video_cap = cv2.VideoCapture(video_path)
    highlight_and_write_video(video_cap, corners, result_video_shape)
    video_cap.release()

    create_video_using_ffmpeg()
    shutil.rmtree(SEQUENCE_IMAGES_DIR)


def highlight_and_write_video(video_cap: cv2.VideoCapture, corners: List, area_shape: Tuple):
    number_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    assert number_frames == len(corners), "Количество кадров в видео должно быть равно количеству углов"

    if (video_cap.isOpened() == False):
        print("Ошибка открытия видеофайла")
    else:
        print("Обрезка кадров...")
        for i in range(1, number_frames+1):
            ret, frame = video_cap.read()
            if ret == True:
                left_up_i, left_up_j = corners[i-1]
                mask = np.zeros(frame.shape, dtype = "uint8")
                polygon = np.array([[
                    [left_up_j, left_up_i], 
                    [left_up_j, left_up_i+area_shape[0]-1], 
                    [left_up_j+area_shape[1], left_up_i+area_shape[0]-1],
                    [left_up_j+area_shape[1], left_up_i]
                ]], np.int32)

                cv2.fillPoly(mask, polygon, (255,255,255))

                writefile = '{0:s}/img{1:05d}.jpg'.format(SEQUENCE_IMAGES_DIR, i)
                cv2.imwrite(writefile, highlight_by_mask(frame, mask))
            else:
                print("Ошибка чтения {0} кадра".format(i))
                break


def run_clipping_video_by_salient_area_task(video_path: str, model: Any):
    video_cap = cv2.VideoCapture(video_path)
    width  = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    result_video_shape = vertical_shape_from_horizontal((height, width), VERTICAL_FORMAT)

    # Найти левый верхний угол прямоугольника с основным объектом для каждого кадра видео
    corners = find_all_corners(video_cap, model, result_video_shape)
    video_cap.release()

    # Сглаживание
    corners = list(zip(
        rolling_list(list(map(lambda pair: pair[0], corners)), ROLLING_WINDOW_SIZE),
        rolling_list(list(map(lambda pair: pair[1], corners)), ROLLING_WINDOW_SIZE)))

    os.makedirs(SEQUENCE_IMAGES_DIR, exist_ok=True)

    # Обрезка видео
    video_cap = cv2.VideoCapture(video_path)
    crop_and_write_video(video_cap, corners, result_video_shape)
    video_cap.release()

    create_video_using_ffmpeg()
    shutil.rmtree(SEQUENCE_IMAGES_DIR)



def highlight_by_mask(image, mask):
    background_image = change_brightness(image, -60)
    masked_image = cv2.bitwise_and(image, mask)
    mask = cv2.bitwise_not(mask)
    background_image = cv2.bitwise_and(background_image, mask)
    highlight_image = cv2.bitwise_or(masked_image, background_image)
    return highlight_image



def find_all_corners(video_cap: cv2.VideoCapture, model: Any, shape_bounding_box: Tuple, need_log: bool = True) -> List:
    corners = []
    number_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    salient_weights = create_center_gradient_image(shape_bounding_box[0], shape_bounding_box[1], dtype=tf.uint32)

    if (video_cap.isOpened() == False):
        print("Ошибка открытия видеофайла")
    else:
        print("Определение основного объекта по кадрам...")
        for i in range(1, number_frames+1):
            ret, frame = video_cap.read()

            if ret == True:
                image_tensor = tf.convert_to_tensor(frame)
                salient_mask = model.signatures["serving_default"](image_tensor)['mask']                

                left_up_i, left_up_j = find_salient_area_left_corner(salient_mask, shape_bounding_box, salient_weights)
                corners.append([left_up_i, left_up_j])

                if need_log:
                    print_progress_bar(i, number_frames)
            else:
                print("Ошибка чтения {0} кадра".format(i))
                break
    return corners



def rolling_list(source: List, rolling_window: int) -> List:
    padding_size = rolling_window // 2
    assert padding_size < len(source), "Указано слишком большое окно для сглаживания"
    assert rolling_window % 2 == 1, "Окно для сглаживания должно быть нечетного размера"

    # mirror
    list_with_padding = [*reversed(source[:padding_size]), *source, *reversed(source[-padding_size:])]
    result = []

    for i in range(0, len(list_with_padding)-rolling_window+1):
        result.append(sum(list_with_padding[i:i+rolling_window]) // rolling_window)

    return result



def crop_and_write_video(video_cap: cv2.VideoCapture, corners: List, shape_bounding_box: Tuple):
    number_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    assert number_frames == len(corners), "Количество кадров в видео должно быть равно количеству углов"

    if (video_cap.isOpened() == False):
        print("Ошибка открытия видеофайла")
    else:
        print("Обрезка кадров...")
        for i in range(1, number_frames+1):
            ret, frame = video_cap.read()
            if ret == True:
                image_tensor = tf.convert_to_tensor(frame)
                left_up_i, left_up_j = corners[i-1]
                cropped_image = tf.slice(image_tensor, 
                                         [left_up_i, left_up_j, 0], 
                                         [shape_bounding_box[0], shape_bounding_box[1], 3])

                writefile = '{0:s}/img{1:05d}.jpg'.format(SEQUENCE_IMAGES_DIR, i)
                cv2.imwrite(writefile, cropped_image.numpy())
            else:
                print("Ошибка чтения {0} кадра".format(i))
                break



def get_saved_model():
    return tf.saved_model.load('./serving/models/u2net/3')



def find_salient_area_left_corner(salient_mask, area_shape, weights=None):
    mask_height = salient_mask.shape[0]
    mask_width = salient_mask.shape[1]

    area_height = area_shape[0]
    area_width = area_shape[1]

    if weights == None:
        weights = tf.fill([area_height, area_width, 1])

    max_saliency = 0
    corner = []
    salient_mask = tf.cast(salient_mask, tf.uint32)

    for i in range(mask_height-area_height + 1):
        for j in range(mask_width-area_width + 1):
            sum_saliency_area = tf.reduce_sum(
                tf.math.multiply(tf.slice(salient_mask, [i, j, 0], [area_height, area_width, 1]), weights)
            )
            if max_saliency < sum_saliency_area:
                max_saliency = sum_saliency_area
                corner = [i, j]

    return corner



def create_video_using_ffmpeg():
    subprocess.call(
        'ffmpeg -framerate 25 -i {0}/img%05d.jpg -pix_fmt yuv420p {1}'
                        .format(SEQUENCE_IMAGES_DIR, DEFAULT_OUTPUT_FILE), 
        shell=True,
    )



def vertical_shape_from_horizontal(source_shape: tuple, proportions_of_sides: tuple):
    assert len(source_shape) == 2 and len(proportions_of_sides) == 2
    assert proportions_of_sides[0] > proportions_of_sides[1]
    part = source_shape[0]//proportions_of_sides[0]
    height = (proportions_of_sides[0] * part) - (proportions_of_sides[0] * part % 2)
    width = (proportions_of_sides[1] * part) - (proportions_of_sides[1] * part % 2)
    return [height, width]



def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img



def print_progress_bar (current_iteration: int, total_iterations: int, length = 50, prefix = 'Progress:'):
    percent = "{0:.1f}".format(100 * (current_iteration / float(total_iterations)))
    filledLength = int(length * current_iteration // total_iterations)
    bar = '█' * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}%', end = "\r")
    # Print New Line on Complete
    if current_iteration == total_iterations: 
        print()



def create_center_gradient_image(height: int, width: int, shift_scale=1, dtype: Any = None) -> tf.Tensor:
    matrix = []
    for i in range(height):
        row = []
        if i < (height+1)//2:
            shift_i = i + 1
        else:
            shift_i = height - i
        for j in range(width):
            if j < (width+1)//2:
                shift_j = j + 1
            else:
                shift_j = width - j
            row.append([(shift_i + shift_j)*shift_scale])
        matrix.append(row)
    return tf.convert_to_tensor(matrix, dtype=dtype)



def show_salient_area_polygon(video_cap: cv2.VideoCapture, model: Any):
    width  = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    shape_bounding_box = vertical_shape_from_horizontal((height, width), (16,9))
    print(shape_bounding_box)
    ret, frame = video_cap.read()
    if ret == True:
        image_tensor = tf.convert_to_tensor(frame)
        salient_mask = model.signatures["serving_default"](image_tensor)['mask']

        salient_weights = create_center_gradient_image(shape_bounding_box[0], shape_bounding_box[1], dtype=tf.uint32)
        left_up_row, left_up_col = find_salient_area_left_corner(salient_mask, shape_bounding_box, salient_weights)

        polygon = np.array([[
            [left_up_col, left_up_row], 
            [left_up_col, left_up_row+shape_bounding_box[0]-1], 
            [left_up_col+shape_bounding_box[1], left_up_row+shape_bounding_box[0]-1],
            [left_up_col+shape_bounding_box[1], left_up_row]
            ]], np.int32)
        img_mod = cv2.polylines(image_tensor.numpy(), [polygon], True, (0,255,0),3)

        cv2.imshow("Frame", img_mod)
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()