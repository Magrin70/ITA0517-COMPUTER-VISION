import cv2
v = cv2.VideoCapture("video.mp4")
bg = cv2.createBackgroundSubtractorMOG2()
while True:
    ok, frame = v.read()
    if not ok: break
    mask = bg.apply(frame)
    out = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Foreground", out)
    if cv2.waitKey(30) == ord("q"): break
v.release()
cv2.destroyAllWindows()