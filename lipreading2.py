import dlib
import cv2
import numpy as np

#获取视频
cap = cv2.VideoCapture('lipnet.mpg')

#判读正确打开
isOpened = cap.isOpened()
print(isOpened)

#导入dlib的检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


#设定红色阈值，HSV空间
redLower = np.array([170, 43, 46])
redUpper = np.array([180, 255, 255])


#遍历每一帧
while(isOpened):
    (flag, frame) = cap.read()

    # read img file
    #img = cv2.imread(frame)

    # 取灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 计算人脸68特征点坐标
    #positions_68_array = []

    faces = detector(gray, 1)#The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    #detector 函數的第二個參數是指定反取樣（unsample）的次數，如果圖片太小的時候，將其設為 1 可讓程式偵較容易測出更多的人臉。但是会更慢

    #win = dlib.image_window()

    #win.set_image(frame)

    #不取灰度
    #faces = detector(frame, 0)

    for k, d in enumerate(faces):
        shape = predictor(frame, d)
        landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])

    #landmarks = np.matrix([[p.x, p.y] for p in predictor(img, faces[0]).parts()])

        for num in range(49,68):
            cv2.circle(frame, (shape.parts()[num-1].x, shape.parts()[num-1].y), 1, (0, 255, 0), -1)#1图片画板 2圆心 3半径 4颜色 5线条宽度 -1为实心

            cv2.line(frame,(shape.parts()[num-1].x, shape.parts()[num-1].y),(shape.parts()[num].x, shape.parts()[num].y),(255,0,0),1)

            cv2.rectangle(frame,(shape.parts()[48].x-5, shape.parts()[52].y-5),(shape.parts()[54].x+5, shape.parts()[57].y+5),(0,0,255),1)
            '''
            img = frame[shape.parts()[48].x:shape.parts()[54].x,shape.parts()[52].y:shape.parts()[57].y]

            # 转到HSV空间
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # 根据阈值构建掩膜
            mask_red = cv2.inRange(hsv, redLower, redUpper)
            # 腐蚀操作
            mask_red = cv2.erode(mask_red, None, iterations=2)
            # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
            mask_red = cv2.dilate(mask_red, None, iterations=2)

            mask = mask_red

            result = cv2.bitwise_and(img, img, mask=mask_red)



            #win.add_overlay(shape)
            '''
        cv2.imshow('frame', frame)
        #cv2.imshow('red',result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q pressed")
            break

        '''
        for idx, point in enumerate(landmarks):
            # 68点的坐标
            pos = (point[0, 0], point[0, 1])
            #加入列表中
            positions_68_array.append(pos)

            #建立一个新列表，存放嘴唇特征点,可写入CSV文件，为之后深度学习作准备
            positions_lip_array = []

            # 将点 49-68 写入
            
            for i in range(48, 68):
                
                positions_lip_array.append(positions_68_array[i][0])
                positions_lip_array.append(positions_68_array[i][1])
                
                #将点连线
                cv2.line(frame, point[i][0], point[i][1], (0,255,0), 3)
        '''



