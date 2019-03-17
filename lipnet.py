import cv2
import numpy as np

#获取视频
cap = cv2.VideoCapture('lipnet.mpg')

#判读正确打开
isOpened = cap.isOpened()
print(isOpened)

#视频帧率，每秒钟出现图片数
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

#视频的宽高信息
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#设定红色阈值，HSV空间
redLower = np.array([170, 100, 100])
redUpper = np.array([179, 255, 255])

i = 0

'''
(flag, frame) = cap.read()
print(flag)
'''

#遍历每一帧
while((isOpened) and (i < 3)):
    (flag, frame) = cap.read()
    #重要语句！！
    if ((flag == True) and (i < 3)):
        # 转到HSV空间
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 根据阈值构建掩膜
        mask_red = cv2.inRange(hsv, redLower, redUpper)
        # 腐蚀操作
        mask_red = cv2.erode(mask_red, None, iterations=2)
        # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        mask_red = cv2.dilate(mask_red, None, iterations=2)

        mask = mask_red

        cv2.imshow('src',mask_red)
        '''
        # 轮廓检测
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        #初始化嘴唇轮廓质心
        center = None
        #如果存在轮廓
        if ((len(cnts) > 0) and (i < 3)):
        #if i < 3:
            #找到面积最大的轮廓
            c = max(cnts, key = cv2.contourArea)
            #确定面积最大的轮廓的外接圆
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            #画出矩形
            #cv2.rectangle(frame,(int(x-50),int(y-50)),(int(x+50),int(y+50)),(0,255,0),3)

            #剪切出嘴唇
            mouth = frame[int(x-50):int(y-50), int(x+50):int(y+50)]
            #读取图片
            fileName = 'img' + str(i) + '.jpg'
            i = i + 1
            #写入图片
            cv2.imwrite(fileName, mouth, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 1文件名，2内容，3保存的图片质量
            '''






