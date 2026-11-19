import cv2
img = cv2.imread("image.jpg")
cv2.rectangle(img, (50,50), (250,200), (0,255,0), 3)
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()