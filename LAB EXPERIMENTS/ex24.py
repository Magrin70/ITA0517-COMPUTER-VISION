import cv2
import numpy as np
img = cv2.imread("image.jpg", 0)
k = np.ones((5,5), np.uint8)
out = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)
cv2.imshow("Black Hat", out)
cv2.waitKey(0)
cv2.destroyAllWindows()