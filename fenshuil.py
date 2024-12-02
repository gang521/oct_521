"""
分水岭算法
"""
import cv2
import numpy as np

def watershed_segmentation(img):
    """
    使用分水岭算法对图像进行分割

    参数:
    img (numpy.ndarray): 输入图像

    返回:
    numpy.ndarray: 分割结果
    """
    # 灰度化图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 进行高斯模糊平滑
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 找到图像的梯度
    edges = cv2.Canny(blur, 100, 200)

    # 获取图像的距离变换
    dist = cv2.distanceTransform(edges, cv2.DIST_L2, 5)

    # 归一化距离变换图像
    dist_norm = cv2.normalize(dist, None, 0, 1.0, cv2.NORM_MINMAX)

    # 对距离变换图像进行阈值处理,得到种子点
    ret, sure_fg = cv2.threshold(dist_norm, 0.7, 1.0, cv2.THRESH_BINARY)
    sure_fg = sure_fg.astype(np.uint8)

    # 膨胀种子点,得到背景区域
    kernel = np.ones((3, 3), np.uint8)
    sure_bg = cv2.dilate(edges, kernel, iterations=3)
    sure_bg = cv2.bitwise_not(sure_bg).astype(np.uint8)

    # 合并前景和背景,得到未知区域
    unknown = cv2.subtract(sure_bg, sure_fg)

    # 标记所有区域
    ret, markers = cv2.connectedComponents(sure_fg)
    markers[unknown == 255] = 0

    # 进行分水岭分割
    markers = cv2.watershed(img, markers)

    # 将标签图像转换为彩色图像
    segmented_img = np.zeros_like(img)
    segmented_img[markers == -1] = [255, 0, 0]  # 边界为蓝色
    unique_labels = np.unique(markers)
    for label in unique_labels:
        if label > 0:
            segmented_img[markers == label] = [np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)]

    return segmented_img

# 读取图像
img = cv2.imread('DataImage/2/10e.png.png')

# 进行分水岭分割
segmented_img = watershed_segmentation(img)

# 显示分割结果
cv2.imshow('Segmented Image', segmented_img)
# cv2.imwrite('DataImage/2/10eG87-k_con_com-fsl.png', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()