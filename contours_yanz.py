"""
读取自适应阈值后的图
提取轮廓
绘制提取的轮廓、轮廓画在自适应阈值图、轮廓画在标注图
"""
import cv2
import numpy as np

# 读取自适应阈值的图像
img = cv2.imread('DataImage/4/1_B5_adathre.png', 0)

# 读取背景图像 (用于绘制轮廓的原始彩色图)
original_img = cv2.imread('DataImage/4/1b.png')

# 高斯模糊平滑
blur = cv2.GaussianBlur(img, (5, 5), 0)

# 自适应阈值分割
thresh = cv2.adaptiveThreshold(blur,
                               255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               11,
                               2)

# 形态学处理，填充小洞
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 寻找轮廓
contours, _ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个空白图像用于绘制轮廓
contour_image = np.zeros_like(img)  # 黑色背景，与原图尺寸一致

# 在灰度图上绘制轮廓（用于修改的 1e_B_adathre.png）
adathre_with_contours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # 将灰度图转为彩色以绘制彩色轮廓

i = 20
# 在空白图像和灰度图上绘制轮廓
for cnt in contours:
    if cv2.contourArea(cnt) > i:  # 过滤掉小的轮廓
        cv2.drawContours(contour_image, [cnt], 0, 255, 1)  # 使用白色绘制轮廓，线条宽度为1
        cv2.drawContours(adathre_with_contours, [cnt], 0, (0, 255, 0), 2)  # 在灰度图上绘制绿色轮廓
        cv2.drawContours(original_img, [cnt], 0, (0, 255, 0), 2)  # 使用绿色绘制轮廓


# 显示结果
# cv2.imshow('Adaptive Threshold', thresh)  # 自适应阈值结果
cv2.imshow('Contours on Original Image', original_img)  # 显示原始图像上的轮廓
# cv2.imshow('Contours ', adathre_with_contours)  # 显示绘制了轮廓的灰度图
# cv2.imshow('Contour Image', contour_image)  # 显示单独的轮廓图

# 保存结果
# cv2.imwrite('DataImage/3/2e_B_adathre.png', thresh)
cv2.imwrite('DataImage/4/1b_5_contours20.png', original_img)  # 保存原图上绘制的轮廓
# cv2.imwrite('DataImage/3/contour_only.png', contour_image)  # 保存单独的轮廓图
# cv2.imwrite('DataImage/3/10.png', adathre_with_contours)  # 保存绘制了轮廓的灰度图

cv2.waitKey(0)
cv2.destroyAllWindows()
