'''
kmeans聚类
最常见的聚类算法
画出来的图能看到目标区域的雏形
感觉暂时还有用
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

def preprocess_image(image):
    #图像转换为浮点型并归一
    normalized_image = image.astype(np.float32) / 255.0
    #规定尺寸
    #resized_image = cv2.resize(normalized_image, (500, 500))
    #模糊处理减小噪音
    blurred_image = cv2.GaussianBlur(normalized_image, (5, 5), 0)
    return blurred_image

def kmeans_segmentation(image, num_clusters):
    pixel_values = image.reshape(-1, 3).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
    _, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    segmented_image = centers[labels.flatten()].reshape(image.shape)
    return segmented_image

# 加载图像
img = cv2.imread('DataImage/2/1o.png')

# 预处理图像
processed_image = preprocess_image(img)

# 对图像进行K-means分割
num_clusters = 20  # 设置聚类簇的数量
segmented_image = kmeans_segmentation(processed_image, num_clusters)

# 使用 Matplotlib 显示原始图像和分割结果
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.title('Original Image')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# plt.title('Segmented Image')
# plt.imshow(segmented_image)
# plt.axis('off')
#
# plt.show()
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey()
cv2.destroyAllWindows()
# 保存分割结果
cv2.imwrite('DataImage/2/1ok.png', segmented_image * 255)