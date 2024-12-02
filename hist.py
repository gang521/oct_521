"""
直方图
"""
import cv2

# 读取原始图像
original_image = cv2.imread('DataImage/1/1e.png')

# 将图像转换为灰度图，因为直方图分割通常在灰度图上进行
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# 使用Otsu's方法自动确定阈值
threshold, segmented_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 显示原始图像和分割后的图像
cv2.imshow('Original Image', original_image)
cv2.imshow('Segmented Image', segmented_image)
cv2.imwrite('DataImage/1/1e_hist.png', segmented_image)

# 等待按键后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()