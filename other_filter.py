"""
几种滤波处理
"""
import cv2
import numpy as np

# 读取图像
image = cv2.imread('DataImage/1/1e_R.png')
# 如果图像不是灰度图，转换为灰度图
if image.ndim == 3:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用中值滤波
median_filtered = cv2.medianBlur(image, 5)
cv2.imshow('Median Filtered Image', median_filtered)
cv2.imwrite('DataImage/1/1e_R_medfil.png', median_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 应用双边滤波
bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Filtered Image', bilateral_filtered)
cv2.imwrite('DataImage/1/1e_R_bifil.png', bilateral_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # 转换为灰度图
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 应用自适应阈值滤波
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptive Threshold Image', thresh)
cv2.imwrite('DataImage/1/1e_R_adathre.png', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 定义结构元素
kernel = np.ones((5,5), np.uint8)
# 应用形态学腐蚀
eroded = cv2.erode(image, kernel, iterations=1)
# 应用形态学膨胀
dilated = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Eroded Image', eroded)
cv2.imwrite('DataImage/1/1e_R_eroded.png', eroded)
cv2.imshow('Dilated Image', dilated)
cv2.imwrite('DataImage/1/1e_R_dilated.png', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()