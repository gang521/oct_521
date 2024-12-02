import cv2

def binarize_image(input_image_path, output_image_path, threshold):
    """
    将图像进行二值化处理,并显示原图和二值化图像
    :param input_image_path: 输入图像路径
    :param output_image_path: 输出图像路径
    :param threshold: 二值化阈值
    """
    # 读取图像
    image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    # 检查图像是否成功读取
    if image is None:
        print(f"无法读取图像: {input_image_path}")
        return

    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行二值化处理
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

    # 保存二值化后的图像
    cv2.imwrite(output_image_path, binary_image)
    # print(f"已保存二值化图像至: {output_image_path}")

    # 显示原图和二值化图像
    # cv2.imshow("Original Image", image)
    cv2.imshow("Binarized Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 用法
input_image_path = "DataImage/4/1_B.png"
output_image_path = "DataImage/4/1_B5.png"
binarize_image(input_image_path, output_image_path, 5)
# input_image_path = "DataImage/2/2eB.png"
# output_image_path = "DataImage/2/2eB10.png"
# binarize_image(input_image_path, output_image_path, 10)