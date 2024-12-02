'''
进行闭运算
先膨胀后腐蚀
消除小孔和小的黑色区域
结果上看，图片看上去变糊了
但是感觉也是会有用的
'''
import numpy as np
import cv2 as cv

# 读取图像
img1 = cv.imread('DataImage/3/4eG70-k.png', 0)
if img1 is None:
    print("Error: Could not read image.")
    exit(1)

# 定义一个 3x3 的卷积核
kernel = np.ones((5, 5), np.uint8)

# 进行闭运算
closing = cv.morphologyEx(img1, cv.MORPH_CLOSE, kernel)

# 添加文本说明
cv.putText(closing, "Closing", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

# 显示闭运算后的图像
cv.imshow("origin", img1)
cv.imshow("Closed Image", closing)
cv.imwrite('DataImage/3/4eG70-k-close.png', closing)
cv.waitKey(0)
cv.destroyAllWindows()