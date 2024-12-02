"""
超像素
"""
import cv2
import numpy as np

# 读取图像
image = cv2.imread('DataImage/3/2e.png')

# 将图像转换为Lab颜色空间
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# 初始化SLIC算法的参数
num_superpixels = 300
compactness = 12

# 创建SLIC对象
segments = cv2.ximgproc.createSuperpixelSLIC(lab_image, region_size=20, ruler=compactness)

# 迭代算法
segments.iterate(10)

# 获取超像素标签
labels = segments.getLabels()

# 将标签转换为8位单通道图像
labels_uint8 = np.uint8(labels)

# 应用颜色映射
segmented_image = cv2.applyColorMap(labels_uint8, cv2.COLORMAP_JET)

# 显示原始图像和分割后的图像
# cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()