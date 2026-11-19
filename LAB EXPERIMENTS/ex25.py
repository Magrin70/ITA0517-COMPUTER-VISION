import cv2
img = cv2.imread("image.jpg")
temp = cv2.imread("watch.jpg")
if img is None or temp is None:
    print("Keep image.jpg and watch.jpg in this folder")
else:
    r = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    _, _, _, p = cv2.minMaxLoc(r)
    h, w = temp.shape[:2]
    cv2.rectangle(img, p, (p[0]+w, p[1]+h), (0,255,0), 2)
    cv2.imshow("Object", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()