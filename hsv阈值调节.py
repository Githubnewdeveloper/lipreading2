import cv2
import numpy as np

def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('hl', 'result', 0,   179, nothing)
cv2.createTrackbar('hu', 'result', 179, 179, nothing)
cv2.createTrackbar('sl', 'result', 0,   255, nothing)
cv2.createTrackbar('su', 'result', 255, 255, nothing)
cv2.createTrackbar('vl', 'result', 0,   255, nothing)
cv2.createTrackbar('vu', 'result', 255, 255, nothing)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    (flag, frame) = cap.read()

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'result')
    hu = cv2.getTrackbarPos('hu', 'result')
    sl = cv2.getTrackbarPos('sl', 'result')
    su = cv2.getTrackbarPos('su', 'result')
    vl = cv2.getTrackbarPos('vl', 'result')
    vu = cv2.getTrackbarPos('vu', 'result')

    # Converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])
    mask = cv2.inRange(hsv, lower, upper)

    (contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("result", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
