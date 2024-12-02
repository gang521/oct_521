import cv2
import numpy as np

# 读取轮廓图和原始图像
contour_image = cv2.imread('DataImage/3/1e_B_adathre.png')
original_image = cv2.imread('DataImage/3/1be.png')

# 创建与原图相同大小的空白图像
overlay = np.zeros_like(original_image)

# 绘制轮廓
contours, _ = cv2.findContours(cv2.cvtColor(contour_image, cv2.COLOR_BGR2GRAY), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 500:  # 根据需要调整面积阈值
        cv2.drawContours(overlay, [cnt], 0, (0, 255, 0), 2)  # 绿色轮廓

# 使用加权叠加将轮廓与原图结合
result = cv2.addWeighted(original_image, 1, overlay, 0.5, 0)

# 显示结果
cv2.imshow('Overlayed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
# cv2.imwrite('DataImage/3/overlayed_image.png', result)