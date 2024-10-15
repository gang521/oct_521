'''
把hsv变成rgb
和
把rgb变成hsv
'''
import cv2
import math

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

image_path="DataImage/2/1.png"
img = cv2.imread(image_path)  # 读取彩色图像(BGR)
img=img[0:768,0:898]
height, width = img.shape[:2]  # 图片的高度和宽度

atan_value=math.atan(634/367)
atan_degree=math.degrees(atan_value)
theta1=atan_degree   # 顺时针旋转角度，单位为角度
x0, y0 = 511, 383  # 以图像中心作为旋转中心
MAR1 = cv2.getRotationMatrix2D((x0,y0), theta1, 1.0)

imgR1 = cv2.warpAffine(img, MAR1, (width, height))  # 旋转变换，默认为黑色填充

#半径和中心
r=383-18
r1=383-272
x0=511
y0=383

#遍历每个像素，保留图像中央的圆形部分
for y in range(height):
    for x in range(width):
        if (x-x0)**2+(y-y0)**2>r**2: #判断当前像素 (x, y) 是否在以 (x0, y0) 为中心，半径为 r 的圆形区域之外
            imgR1[y,x]=(0,0,0) #当前像素在圆的外部，那么将这个像素的颜色设置为黑色
    pixel0=imgR1[y,509]
    pixel2=imgR1[y,513]
    h1,s1,v1=rgb2hsv(pixel0[2],pixel0[1],pixel0[0])
    h2,s2,v2=rgb2hsv(pixel2[2],pixel2[1],pixel2[0])  
    rgb1=hsv2rgb((h1*2+h2)/3,(s1*2+s2)/3,(v1*2+v2)/3)#不只是511有线，所以取加权消除
    rgb2=hsv2rgb((h1+h2)/2,(s1+s2)/2,(v1+v2)/2)
    rgb3=hsv2rgb((h1+2*h2)/3,(s1+2*s2)/3,(v1+2*v2)/3)
    imgR1[y,510]=(rgb1[2],rgb1[1],rgb1[0])
    imgR1[y,511]=(rgb2[2],rgb2[1],rgb2[0])
    imgR1[y,512]=(rgb3[2],rgb3[1],rgb3[0])


cv2.imshow("vertical",imgR1)
cv2.waitKey()
cv2.destroyAllWindows()
#saveFile="../oct/rot/1.png"
#cv2.imwrite(saveFile,imgR1)
