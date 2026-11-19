import cv2
img = cv2.imread("image.jpg")
cv2.putText(img, "Computer Vision", (30,60),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()