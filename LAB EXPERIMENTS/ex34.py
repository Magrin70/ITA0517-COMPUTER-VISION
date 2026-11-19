import cv2
img = cv2.imread("image.jpg")
cv2.circle(img, (150,150), 70, (0,0,255), 3)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()