"""
提取自适应阈值图的轮廓
"""
import cv2
import numpy as np

# 读取自适应阈值的图
img = cv2.imread('DataImage/4/1_B5_adathre.png', 0)

# 高斯模糊平滑
blur = cv2.GaussianBlur(img, (5, 5), 0)

# 自适应阈值分割
thresh = cv2.adaptiveThreshold(blur,
                               255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               11,
                               2)

# 形态学处理,填充小洞
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 寻找轮廓
contours, _ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制提取的区域
result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# roi_img = np.zeros_like(img)
for cnt in contours:
    if cv2.contourArea(cnt) > 1:
        cv2.drawContours(result, [cnt], 0, (0, 255, 0), 2)

# 显示结果
cv2.imshow('Result', result)
cv2.imwrite('DataImage/4/1_B5_adathre_contour.png', result)
# cv2.imshow('roi_image.png', roi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()