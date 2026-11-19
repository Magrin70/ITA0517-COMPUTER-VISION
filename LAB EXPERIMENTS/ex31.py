import cv2
img = cv2.imread("image.jpg", 0)
_, out = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Segmentation", out)
cv2.waitKey(0)
cv2.destroyAllWindows()