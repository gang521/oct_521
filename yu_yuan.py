"""
预处理（圆形）
"""
import cv2
import numpy as np
import math

# ----- 全局参数
# PAI值
PI = math.pi
CIRCLE_RADIUS = 365  # 图像半径
Circle_x0, Circle_y0 = 511, 383  # 圆心像素值
height, width = 768, 898
# 极坐标转换后图像的高，可自己设置
LINE_height = int(CIRCLE_RADIUS)
# 极坐标转换后图像的宽，一般是原来圆形的周长
LINE_width = int(CIRCLE_RADIUS * PI * 2)  # 貌似不能*2


def bgr2rgb(bgr):
    return cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2RGB)[0, 0]


def rgb2bgr(rgb):
    return cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2BGR)[0, 0]


def hsv2rgb(h, s, v):
    hsv = np.uint8([[[h, s * 255, v * 255]]])
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return tuple(rgb[0, 0])


def rgb2hsv(r, g, b):
    rgb = np.uint8([[[r, g, b]]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
    return hsv[0, 0][0], hsv[0, 0][1] / 255.0, hsv[0, 0][2] / 255.0


def create_line_image(img):  # ----- 将圆环变为矩形
    # 建立展开后的图像
    line_image = np.zeros((LINE_height, LINE_width, 3), dtype=np.uint8)
    # 按照圆的极坐标赋值
    for row in range(line_image.shape[0]):
        for col in range(line_image.shape[1]):
            # 角度，最后的-0.1是用于优化结果，可以自行调整
            theta = PI * 2 / LINE_width * (col + 1)
            # 半径，减1防止超界
            rho = CIRCLE_RADIUS - row

            x = int(Circle_x0 + rho * math.cos(theta) + 0.0)
            y = int(Circle_y0 - rho * math.sin(theta) + 0.0)

            # 检查坐标是否在图像内
            if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
                line_image[row, col, :] = img[y, x, :]
    return line_image


def delete_slope_line(img):  # 去除倾斜线
    img = img[0:height, 0:width]
    # 创建一个遮罩，用于标记圆外的像素
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, (Circle_x0, Circle_y0), CIRCLE_RADIUS, 255, -1)
    mask_inv = cv2.bitwise_not(mask)
    # 将圆外的像素设为黑色
    img[mask_inv == 255] = (0, 0, 0)
    for x in range(width):  # 处理原图中斜线
        y0 = []
        B = []
        G = []
        R = []
        y1 = round(383 - (x - 511) * 182 / 316)  # 直接找线附近的点，根据像素判断，在去上下两点HSV的平均
        for y in range(y1 - 2, y1 + 3):
            pixel = bgr2rgb(img[y, x])
            b, g, r = pixel[0], pixel[1], pixel[2]
            B.append(b)
            G.append(g)
            R.append(r)
            if g == 128:
                if b == 0 or r == 0:
                    y0.append(y)
        if len(y0) == 1:
            pixel0 = bgr2rgb(img[y0[0] - 1, x])
            pixel1 = bgr2rgb(img[y0[0] + 1, x])
            h1, s1, v1 = rgb2hsv(*pixel0)
            h2, s2, v2 = rgb2hsv(*pixel1)
            rgb = hsv2rgb((h1 + h2) / 2, (s1 + s2) / 2, (v1 + v2) / 2)
            img[y0[0], x] = rgb2bgr(rgb)
    return img


def delete_arch_line(img):  # 去除弧线
    for x in range(0, img.shape[1] - 1):
        y0 = []
        B = []
        G = []
        R = []
        for y in range(314, 332):
            pixel = bgr2rgb(img[y, x])
            b, g, r = pixel[2], pixel[1], pixel[0]
            B.append(b)
            G.append(g)
            R.append(r)
            if g == 255 and b == 255 and r == 0:
                y0.append(y)
        if len(y0) == 1:
            pixel0 = bgr2rgb(img[y0[0] - 1, x])
            pixel1 = bgr2rgb(img[y0[0] + 1, x])
            h1, s1, v1 = rgb2hsv(*pixel0)
            h2, s2, v2 = rgb2hsv(*pixel1)
            rgb = hsv2rgb((h1 + h2) / 2, (s1 + s2) / 2, (v1 + v2) / 2)
            img[y0[0], x] = rgb2bgr(rgb)
        if len(y0) == 2:  # 好像有问题
            print(y0)
            pixel0 = bgr2rgb(img[y0[0] - 1, x])
            pixel1 = bgr2rgb(img[y0[0] + 2, x])
            h1, s1, v1 = rgb2hsv(*pixel0)
            h2, s2, v2 = rgb2hsv(*pixel1)
            rgb1 = hsv2rgb((2 * h1 + h2) / 3, (2 * s1 + s2) / 3, (2 * v1 + v2) / 3)
            rgb2 = hsv2rgb((2 * h2 + h2) / 3, (2 * s2 + s1) / 3, (2 * v2 + v1) / 3)
            img[315, x] = rgb2bgr(rgb1)
            img[316, x] = rgb2bgr(rgb2)
    return img


# ----- 主程序
def main(imgpath):
    # 读取图像
    img = cv2.imread(imgpath)  # 读取彩色图像(BGR)
    if img is None:
        print("please check image path")
        return
    print(img.shape)

    #    cv2.imshow("src", img)# 展示原图
    img1 = delete_slope_line(img)  # 去倾斜
    #    cv2.imshow("delete slope",img1)
    # img2 = create_line_image(img1)  # 坐标转换
    #    cv2.namedWindow("line image",cv2.WINDOW_NORMAL)
    #    cv2.resizeWindow("line image",LINE_width,LINE_height)
    #    cv2.imshow("line image",img2)
    img3 = delete_arch_line(img1)  # 去弧线
    #    cv2.namedWindow("delete arch",cv2.WINDOW_NORMAL)
    #    cv2.resizeWindow("delete arch",LINE_width,LINE_height)
    #    cv2.imshow("delete arch",img3)
    #    cv2.waitKey()
    #    cv2.destroyAllWindows()
    cv2.imwrite(saveFile, img3)


if __name__ == '__main__':
    for i in range(1, 12):
        # 输入图像路径
        imgpath = "Image/3/{}b.png".format(i)
        saveFile = "Image/3/{}bo.png".format(i)
        main(imgpath)
