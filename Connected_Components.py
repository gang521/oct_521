"""
连接元+轮廓
"""
import cv2
import numpy as np

# 读取原始图像
original_image = cv2.imread('Image/4/2_R117.png', cv2.IMREAD_GRAYSCALE)

# 如果图像不是灰度图，转换为灰度图
if original_image.ndim == 3:
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# 应用阈值化，以便更容易地识别连接元
_, thresh = cv2.threshold(original_image, 117, 255, cv2.THRESH_BINARY)

# 使用findContours函数找到图像中的轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个与原始图像同样大小的空白图像，用于绘制轮廓
segmented_image = np.zeros_like(original_image)

# 绘制轮廓
cv2.drawContours(segmented_image, contours, -1, (255), thickness=cv2.FILLED)

# 显示原始图像和分割后的图像
cv2.imshow('Original Image', original_image)
cv2.imshow('Segmented Image', segmented_image)
# cv2.imwrite('Image/4/2_R117-k_con_com117.png', segmented_image)

# 等待按键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()