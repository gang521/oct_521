import cv2
import numpy as np
import maxflow

def graph_cut_segmentation(img, seed_mask):
    """
    使用 GraphCut 算法对图像进行分割

    参数:
    img (numpy.ndarray): 输入图像
    seed_mask (numpy.ndarray): 用户提供的种子掩码, 0表示背景, 1表示前景

    返回:
    numpy.ndarray: 分割结果
    """
    height, width, _ = img.shape

    # 构建图
    g = maxflow.Graph[float](width, height)

    # 添加节点
    nodes = g.add_nodes(width * height)

    # 添加边
    for y in range(height):
        for x in range(width):
            # 添加数据项
            if seed_mask[y, x] == 0:  # 背景
                g.add_tedge(nodes[y * width + x], 100, 0)
            elif seed_mask[y, x] == 1:  # 前景
                g.add_tedge(nodes[y * width + x], 0, 100)
            else:  # 未标记
                g.add_tedge(nodes[y * width + x], 50, 50)

            # 添加平滑项
            if x > 0:
                g.add_edge(nodes[y * width + x], nodes[y * width + x - 1], 10, 10)
            if y > 0:
                g.add_edge(nodes[y * width + x], nodes[(y - 1) * width + x], 10, 10)

    # 运行 GraphCut 算法
    g.maxflow()

    # 获取分割结果
    return (g.get_grid_segments(nodes) > 0).astype(np.uint8)

# 读取图像
img = cv2.imread('DataImage/1/1e.png')

# 创建种子掩码
seed_mask = np.zeros_like(img, dtype=np.uint8)

# 在图像上手动标记一些前景和背景区域
cv2.rectangle(seed_mask, (100, 100), (200, 200), (1, 0, 0), -1)  # 前景
cv2.rectangle(seed_mask, (300, 300), (400, 400), (0, 1, 0), -1)  # 背景

# 进行 GraphCut 分割
segmented_img = graph_cut_segmentation(img, seed_mask[:, :, 0])

# 显示分割结果
cv2.imshow('Segmented Image', segmented_img * 255)  # 乘以255以便可视化
cv2.imwrite('DataImage/1/1eg.png', segmented_img * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()