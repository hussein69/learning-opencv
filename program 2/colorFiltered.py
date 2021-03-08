import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerRed = np.array([0,0,100])
    upperRed = np.array([0,0,255])

    mask = cv2.inRange(frame, lowerRed, upperRed)
    res = cv2.bitwise_and(frame, frame, mask = mask)


    cv2.imshow("res", res)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
