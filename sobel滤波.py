"""
sobel进行滤波
"""
import cv2
import numpy as np

# 读取原始图像
original_image = cv2.imread('Image/2/10o.png', cv2.IMREAD_GRAYSCALE)

# 应用Sobel滤波器进行边缘检测
sobelx = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度的幅度
gradient_magnitude = cv2.magnitude(sobelx, sobely)

# 将梯度幅度转换为8位无符号整数
gradient_magnitude_8u = cv2.convertScaleAbs(gradient_magnitude)

# 应用阈值来分割图像
_, segmented_image = cv2.threshold(gradient_magnitude_8u, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 显示原始图像和分割后的图像
cv2.imshow('Original Image', original_image)
cv2.imshow('Segmented Image', segmented_image)
# cv2.imwrite('DataImage/2/10e_sobel3.png', segmented_image)

# 等待按键后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()