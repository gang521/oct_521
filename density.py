#计算密度图
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# 读取图像
image_path = 'DataImage/2/1d.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 二值化处理
# _, binary_image = cv2.threshold(image, 64, 255, cv2.THRESH_BINARY)

# 计算局部密度
density = gaussian_filter(image.astype(float), sigma=10)
# density=image.astype(float)

# 颜色编码
density_normalized = (density - density.min()) / (density.max() - density.min())
color_mapped_image = cv2.applyColorMap((density_normalized * 255).astype(np.uint8), cv2.COLORMAP_JET)

# 显示原图和颜色编码图
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
# plt.imshow(binary_image, cmap='gray')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Density Map')
plt.imshow(color_mapped_image)

plt.show()
