"""
提取ROI
"""
import cv2
import numpy


def ROI(img_path):
    # 读取图像
    img = cv2.imread(img_path)

    # 定义ROI的位置和大小
    y_start = int(img.shape[0] * 0.12)
    y_end = int(img.shape[0] * 0.83)  # 靠下的位置的y坐标占比
    x = 0
    y = y_start
    w = img.shape[1]
    h = y_end - y_start

    # 创建矩形ROI
    roi = img[y:y + h, x:x + w]
    return roi

#
# for i in range(1, 11):
#     # 输入图像路径
#     imgpath = "Image/4/{}e.png".format(i)
#     saveFile = "DataImage/4/{}e.png".format(i)
#     # 提取ROI
#     roi = ROI(imgpath)
#
#     # 显示ROI
#     cv2.imshow('ROI', roi)
#     # 保存提取的ROI图像
#     cv2.imwrite(saveFile, roi)
#
#     # 等待按键，如果用户按下任意键，则退出
#     cv2.waitKey(0)
imgpath = "Image/3/2be.png"
saveFile = "DataImage/3/2be.png"
# 提取ROI
roi = ROI(imgpath)

# 显示ROI
cv2.imshow('ROI', roi)
# 保存提取的ROI图像
cv2.imwrite(saveFile, roi)

# 等待按键，如果用户按下任意键，则退出
cv2.waitKey(0)

# 关闭所有窗口
cv2.destroyAllWindows()
