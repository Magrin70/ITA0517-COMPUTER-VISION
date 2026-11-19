import cv2
v = cv2.VideoCapture("video.mp4")
bg = cv2.createBackgroundSubtractorMOG2()
while True:
    ok, frame = v.read()
    if not ok: break
    foreground = bg.apply(frame)
    cv2.imshow("Background Subtraction", foreground)
    if cv2.waitKey(30) == ord("q"): break
v.release()