import cv2
import numpy as np

img = cv2.imread("tomb-raider-cover.jpg")
edges = cv2.Canny(img, 200, 300)
cv2.imshow("image", img)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
