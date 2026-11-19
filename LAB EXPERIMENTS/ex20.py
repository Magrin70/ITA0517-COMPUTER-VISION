import cv2

img = cv2.imread("image.jpg")
template = cv2.imread("template.jpg")

if img is None:
    print("image.jpg not found")
elif template is None:
    print("template.jpg not found. Please add it to the folder.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, temp_gray, cv2.TM_CCOEFF_NORMED)
    _, _, _, point = cv2.minMaxLoc(result)

    h, w = temp_gray.shape
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (0, 255, 0), 2)

    cv2.imshow("Matched Object", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()