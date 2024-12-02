"""
对自适应阈值的图片进行轮廓处理
"""
import cv2
import numpy as np

# 读取自适应阈值处理后的图像
image_path = 'DataImage/4/2_R117.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 确保图像被正确读取
if image is None:
    raise ValueError("Could not read the image at the specified path.")

# 查找轮廓
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个空白图像用于绘制轮廓
segmented_image = np.zeros_like(image)

# 绘制轮廓
cv2.drawContours(segmented_image, contours, -1, (255), thickness=cv2.FILLED)

# 显示分割后的图像
cv2.imshow('Segmented Image', segmented_image)

# 等待按键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 假设您希望提取的区域是轮廓中的某个特定区域，这里我们尝试找到与红色轮廓相匹配的区域
# 由于我们没有具体的轮廓特征，我们可以尝试通过轮廓的几何特性来识别
# 例如，我们可以通过轮廓的周长和面积来估计

# 计算所有轮廓的周长和面积
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    # 根据周长和面积的比值或其他特征来识别红色轮廓
    # 这里需要您根据实际情况来确定识别逻辑

    # 绘制识别的轮廓
    if some_condition:  # 替换为实际的识别条件
        cv2.drawContours(segmented_image, [contour], -1, (0, 0, 255), thickness=2)

# 显示识别的红色轮廓
cv2.imshow('Identified Red Contour', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()