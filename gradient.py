import cv2
import numpy as np

# 读取原始图像
image = cv2.imread('input_image.png')

# 创建一个与原始图像大小相同的黑色遮罩
mask = np.zeros_like(image)

# 创建渐变遮罩,从白色到透明
gradient = np.linspace(255, 0, mask.shape[0]//2, dtype=np.uint8)
mask[:mask.shape[0]//2, :] = np.expand_dims(gradient, axis=1)

# 将遮罩应用到原始图像上
result = cv2.bitwise_and(image, mask)

# 保存结果图像
cv2.imshow('image', result)
# cv2.imwrite('output_image.png', result)