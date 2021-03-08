import cv2
import numpy as np


img = cv2.imread("gabenweed.jpg")
cv2.imshow("gaben", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
