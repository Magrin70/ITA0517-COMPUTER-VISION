import cv2
import numpy as np
img = np.zeros((400,400,3), dtype=np.uint8)
cv2.rectangle(img,(20,20),(180,180),(0,0,255),-1)
cv2.rectangle(img,(220,20),(380,180),(0,255,0),-1)
cv2.rectangle(img,(20,220),(180,380),(255,0,0),-1)
cv2.rectangle(img,(220,220),(380,380),(0,255,255),-1)
cv2.imshow("Four Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()