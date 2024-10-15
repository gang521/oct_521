'''
两种高低阈值分割出两幅二值化图像
相减获得其差异区域
理论上可以借此选取特征区域
实测效果不咋地
不同的图片的差异阈值不同，感觉没什么普适性
'''
import cv2
import os
import numpy as np

def binary_threshold(image, threshold1, threshold2):
    '''
    获取高低阈值下的二值化图像
    :param image:
    :param threshold1: 二值化的第一个阈值
    :param threshold2: 第二个阈值
    :return: 两张二值化图像
    '''
    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行二值化操作
    max_value = 255  # 最大像素值
    _, binary_image1 = cv2.threshold(gray_image, threshold1, max_value, cv2.THRESH_BINARY)
    _, binary_image2 = cv2.threshold(gray_image, threshold2, max_value, cv2.THRESH_BINARY)

    return binary_image1, binary_image2

def subtract_images(image1, image2):
    # 计算两张灰度图像的差异
    diff_image = cv2.subtract(image1, image2)
    return diff_image

def process_image(image_path, threshold1, threshold2):
    # 读取原始图像
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 进行二值化操作
    binary_image1, binary_image2 = binary_threshold(image, threshold1, threshold2)

    # 计算差异图
    diff_image = subtract_images(binary_image1, binary_image2)

    # 显示三张图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Image (Threshold 1)', binary_image1)
    cv2.imshow('Binary Image (Threshold 2)', binary_image2)
    cv2.imshow('Difference Image', diff_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用，设置可调阈值
process_image('DataImage/2/1.png', 10, 120)