import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = c.detectMultiScale(gray, 1.1, 4)
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
print("Number of faces:", len(faces))
cv2.imshow("Face Count", img)
cv2.waitKey(0)
cv2.destroyAllWindows()