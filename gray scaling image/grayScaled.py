import cv2
import numpy as np
import os


img1 = cv2.imread("gabenweed.jpg", 0)
cv2.imwrite("grayScaled.png", img1)
img2 = cv2.imread("grayScaled.png")
cv2.rectangle(img2, (250,200), (350,300), (0,0,255), -1)
try:
    os.remove("grayScaled.png")
except:
    pass


cv2.imshow("image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
