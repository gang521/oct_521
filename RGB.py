"""
分离RGB通道
卧槽这个牛
"""
import cv2

# 读取图像
image_path = "DataImage/1/1e.png"
image = cv2.imread(image_path)

# 提取 RGB 通道值
b, g, r = cv2.split(image)

# 显示各通道图像
# cv2.imshow("Red", r)
# cv2.imshow("Green", g)
# cv2.imshow("Blue", b)

# # 保存绿色通道图像
output_path1 = "DataImage/1/1e_B.png"
cv2.imwrite(output_path1, b)
output_path2 = "DataImage/1/1e_R.png"
cv2.imwrite(output_path2, r)
output_path3 = "DataImage/1/1e_G.png"
cv2.imwrite(output_path3, g)

# 等待按键并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()