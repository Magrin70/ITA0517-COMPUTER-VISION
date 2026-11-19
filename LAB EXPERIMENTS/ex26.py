import cv2
v = cv2.VideoCapture("video.mp4")
frames = []
while True:
    ok, f = v.read()
    if not ok: break
    frames.append(f)
v.release()
for f in frames[::-1]:
    cv2.imshow("Reverse Video", f)
    if cv2.waitKey(30) == ord("q"): break
cv2.destroyAllWindows()