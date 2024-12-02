"""
添加掩膜
"""
import cv2
import numpy as np

# 读取图像
annotated_img = cv2.imread('DataImage/1/3be.png')
original_img = cv2.imread('DataImage/1/3e.png')

# 转换为灰度图像
gray = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2GRAY)

# 阈值分割
_, mask = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

# 使用掩模提取
segmented = cv2.bitwise_and(original_img, original_img, mask=mask)

# 显示结果
cv2.imshow('Segmented Edema', segmented)
cv2.imwrite('DataImage/1/3e_bitwise.png', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()