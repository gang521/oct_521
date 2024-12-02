"""
添加镜像、噪声、旋转
"""
import os
import cv2
import numpy as np
import random
from skimage.util import random_noise

def rotate_image(image, angle):
    """旋转图像"""
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def add_noise(image):
    """添加随机噪声"""
    noisy = random_noise(image, mode='s&p', amount=0.05)
    noisy = np.array(255 * noisy, dtype='uint8')
    return noisy


def mirror_image(image):
    """镜像图像"""
    mirrored = cv2.flip(image, 1)
    return mirrored


def process_and_save_images(input_dir, output_dir):
    """处理输入目录下的所有图像并保存到输出目录"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)
            label_path = os.path.splitext(image_path)[0] + "_label.png"
            label = cv2.imread(label_path, cv2.IMREAD_GRAYSCALE) if os.path.exists(label_path) else None

            # 处理并保存旋转图像
            angle = random.choice([90, 180, 270])
            rotated_image = rotate_image(image, angle)
            rotated_label = rotate_image(label, angle) if label is not None else None
            cv2.imwrite(os.path.join(output_dir, 'rotated_' + filename), rotated_image)
            if rotated_label is not None:
                cv2.imwrite(os.path.join(output_dir, 'rotated_' + os.path.splitext(filename)[0] + "_label.png"),
                            rotated_label)

            # 处理并保存带噪声图像
            noisy_image = add_noise(image)
            cv2.imwrite(os.path.join(output_dir, 'noisy_' + filename), noisy_image)

            # 处理并保存镜像图像
            mirrored_image = mirror_image(image)
            mirrored_label = mirror_image(label) if label is not None else None
            cv2.imwrite(os.path.join(output_dir, 'mirrored_' + filename), mirrored_image)
            if mirrored_label is not None:
                cv2.imwrite(os.path.join(output_dir, 'mirrored_' + os.path.splitext(filename)[0] + "_label.png"),
                            mirrored_label)


# 示例使用
input_dir = 'DataImage/3'  # 确保这是一个包含图像的目录
output_dir = 'DataImage/3/output'  # 替换为你的输出图像文件夹路径

process_and_save_images(input_dir, output_dir)
