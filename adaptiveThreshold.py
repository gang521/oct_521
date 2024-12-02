"""
自适应阈值
"""
import cv2

# 读取图像
img = cv2.imread('DataImage/1/1e_B.png', cv2.IMREAD_GRAYSCALE)

# 高斯模糊以减少噪声
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# 自适应阈值处理
adaptive_thresh = cv2.adaptiveThreshold(
    blurred,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    15,
    2
)

# 显示结果
cv2.imshow('Adaptive Threshold', adaptive_thresh)
cv2.imwrite('DataImage/1/1e_B_adathre.png', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()