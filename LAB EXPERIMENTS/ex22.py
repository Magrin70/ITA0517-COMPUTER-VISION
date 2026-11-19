import cv2
import numpy as np
img = cv2.imread("image.jpg", 0)
k = np.ones((5,5), np.uint8)
out = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
cv2.imshow("Closing", out)
cv2.waitKey(0)
cv2.destroyAllWindows()