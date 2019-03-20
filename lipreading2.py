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

#保存图片计数
i = 0

#遍历每一帧
while(isOpened):

    # 读取5张图片
    if i == 5:
        break
    else:
        i = i + 1

    (flag, frame) = cap.read()

    # 取灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 1)#The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    #detector 函數的第二個參數是指定反取樣（unsample）的次數，如果圖片太小的時候，將其設為 1 可讓程式偵較容易測出更多的人臉。但是会更慢

    for k, d in enumerate(faces):#enumerate函数，生成带编号的
        #预测器
        shape = predictor(frame, d)
        #标志点
        landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])

        img = frame[(shape.parts()[52].y - 5):(shape.parts()[57].y + 5),(shape.parts()[48].x - 5):(shape.parts()[54].x + 5)]
        #嘴唇的标志点为49-67
        #for num in range(49,68):
            #cv2.circle(frame, (shape.parts()[num-1].x, shape.parts()[num-1].y), 1, (0, 255, 0), -1)#1图片画板 2圆心 3半径 4颜色 5线条宽度 -1为实心

            #cv2.line(frame,(shape.parts()[num-1].x, shape.parts()[num-1].y),(shape.parts()[num].x, shape.parts()[num].y),(255,0,0),1)#连线

            #cv2.rectangle(frame,(shape.parts()[48].x-5, shape.parts()[52].y-5),(shape.parts()[54].x+5, shape.parts()[57].y+5),(0,0,255),1)#画方框

            #img = frame[(shape.parts()[52].y-5):(shape.parts()[57].y+5),(shape.parts()[48].x-5):(shape.parts()[54].x+5)]

        cv2.imshow('frame', img)

        fileName = 'img' + str(i) + '.jpg'
        print(fileName)
        if flag == True:
            cv2.imwrite(fileName, img, [cv2.IMWRITE_JPEG_QUALITY, 100])  # 1文件名，2内容，3保存的图片质量

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q pressed")
            break


