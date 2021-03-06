import cv2
import numpy as np
import glob
from os import listdir
from os.path import isfile, join

cap = cv2.VideoCapture("../../Video/template-matching/netherlands_enschede/enschede.mp4")
template = [cv2.imread(file) for file in glob.glob("../../Video/template-matching/netherlands_enschede/image*.png")]

 
w, h = template.shape[::-1]
 
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
 
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
	
	
	
    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1)
 
    if key == "q":
        break
 
cap.release()
cv2.destroyAllWindows()
