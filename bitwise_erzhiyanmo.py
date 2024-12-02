"""
二值掩膜
"""
import cv2
import numpy as np

# 读取图像
# annotated_img = cv2.imread('DataImage/1/3be.png')
original_img = cv2.imread('DataImage/1/3e.png')

# 转换为灰度图像
gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(blurred, 50, 150)

# 创建掩模
_, mask = cv2.threshold(edges, 1, 255, cv2.THRESH_BINARY)

# 应用掩模提取目标区域
segmented = cv2.bitwise_and(original_img, original_img, mask=mask)

# 显示结果
cv2.imshow('Segmented Area', segmented)
# cv2.imwrite('DataImage/1/3b_bitwiseer.png', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()