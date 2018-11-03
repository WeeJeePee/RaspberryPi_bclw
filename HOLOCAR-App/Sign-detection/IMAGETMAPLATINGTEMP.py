import numpy as np
import cv2
import glob

X_data=[]
files = glob.glob ('C:/Users/amuly/Pictures/Saved Pictures/template/*.jpg')

img=cv2.imread('C:/Users/amuly/Pictures/Saved Pictures/teeth.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for myfile in files:
    temp=cv2.imread(myfile)   
    w,h=temp.shape[:-1]
    res=cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
    threshold=0.86
    loc=np.where(res>=threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)


cv2.imshow('Detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


