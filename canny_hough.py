"""
canny检测
hough变换
"""
import cv2
import numpy as np

# 读取图像
image = cv2.imread('DataImage/3/4e_R_adathre.png', cv2.IMREAD_GRAYSCALE)

# 检查图像是否加载成功
if image is None:
    print("Error: Image not found.")
else:
    # 高斯模糊
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Canny 边缘检测
    edges = cv2.Canny(blurred, 50, 150)

    # Hough 变换检测线条
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10)

    # 创建一个与原图相同大小的黑色图像
    line_image = np.zeros_like(image)

    # 在新图像上绘制检测到的线条
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), 2)  # 白色线条

    # 显示结果
    cv2.imshow('Detected Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()