import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
smiles = c.detectMultiScale(gray, 1.7, 20)
for x,y,w,h in smiles:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
cv2.imshow("Smile", img)
cv2.waitKey(0)
cv2.destroyAllWindows()