"""
图像增强 CLAHE
我们的图像本身就比较亮
好像增强反而对比程度下降了
"""
import cv2


def apply_clahe(input_image_path, output_image_path):
    # 读取图像
    image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    # 如果图像为空则打印路径并返回
    if image is None:
        print(f"无法读取图像 {input_image_path}")
        return

    # 应用CLAHE(对比度受限的自适应直方图均衡化)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)  # 图像转换为LAB色彩空间
    l, a, b = cv2.split(lab)  # 分立LAB的L通道
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # 创建CLAHE对象
    l_clahe = clahe.apply(l)  # 对L通道应用CLAHE
    lab_clahe = cv2.merge((l_clahe, a, b))  # 合并CLAHE后的L通道和AB通道
    image_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR) #LAB转回BGR

    # 保存处理后的图像
    cv2.imwrite(output_image_path, image_clahe)
    print(f"已保存处理后的图像至 {output_image_path}")


# 图片的处理
input_image_path = "DataImage/3/1e.png"
output_image_path = "DataImage/3/1ec.png"
# 调用函数处理图像
apply_clahe(input_image_path, output_image_path)