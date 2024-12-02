"""
flood_fill 泛洪填充
像素值的相似性
从一个种子点开始，检查该点的像素值
然后递归地检查相邻像素
如果相邻像素的值在指定的阈值范围内与种子点相似，
则将这些像素的值更改为新的值（通常是相同的值）
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util, color
from skimage.segmentation import flood_fill
from skimage.util import img_as_float

# 读取图像
image_path = 'DataImage/3/2e.png'
image = util.img_as_float(io.imread(image_path))
# 如果图像不是灰度图，需要转换为灰度图
if len(image.shape) > 2:
    image_gray = color.rgb2gray(image)
else:
    image_gray = image

# 将图像转换为浮点数类型
image_gray = img_as_float(image_gray)

# 设置阈值，用于分割图像
threshold = 0.5

# 使用flood_fill进行图像分割
# 这里我们选择一个种子点，然后根据阈值进行填充
seed_point = (image_gray.shape[0] // 2, image_gray.shape[1] // 2)
segmentation = flood_fill(image_gray, seed_point, threshold)

# 绘制结果
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Original Image')
ax[0].set_axis_off()

ax[1].imshow(segmentation, cmap='gray')
ax[1].set_title('Segmented Image')
ax[1].set_axis_off()

plt.show()