import cv2
import numpy as np

#Videocapture
video = cv2.VideoCapture("../../../../snelweg.mp4")
i = 1
def roi(video, vertices):
	maskz = np.zeros_like(video)
	cv2.fillPoly(maskz, vertices, 255)
	masked = cv2.bitwise_and(video, maskz)
	return masked
	
while True:
	#Read
    ret, orig_frame = video.read()
    
    #Nieuwe laag om op te drawen
    line_image = np.copy(orig_frame) * 0  
    if not ret:
        video = cv2.VideoCapture("../../../../snelweg.mp4")
        continue
 
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    #HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Kleur geel
    low_yellow = np.array([18, 94, 140], dtype=np.uint8)
    up_yellow = np.array([48, 255, 255], dtype=np.uint8)
    #Kleur wit
    low_white = np.array([0,0,165], dtype=np.uint8)
    up_white = np.array([255,255,255], dtype=np.uint8)
    #Inrages
    mask1 = cv2.inRange(hsv, low_yellow, up_yellow)
    mask2 = cv2.inRange(hsv, low_white, up_white)
    #Merge
    mask = cv2.bitwise_or(mask1, mask2)
    #Check
    target = cv2.bitwise_and(frame,frame, mask=mask)
    #Canny
    edges = cv2.Canny(target, 75, 150)
    vertices = np.array([[200,1000],[200,600],[500,400],[1500,400],[1800,600],[1800,1000],
                         ], np.int32)
    edges = roi(edges,[vertices])
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=100)
    cv2.polylines(frame,[vertices],True,(0,255,255))
    
    if lines is not None:
        for line in lines:
			#HEEL VEEL LINES FIX DIT LATER XDDD
            x1, y1, x2, y2 = line[1]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[2]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[3]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[4]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[5]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[6]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[7]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[8]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            x1, y1, x2, y2 = line[9]
            cv2.line(line_image, (x1, y1), (x2, y2), (48, 255, 255), 20)
            
			
            
            
            lines_edges = cv2.addWeighted(frame, 1, line_image, 1, 0)
    
	cv2.namedWindow("frameOutput", cv2.WINDOW_NORMAL)
	cv2.namedWindow("edgesOutput", cv2.WINDOW_NORMAL)
	frameR = cv2.resize(lines_edges, (800,600))
	
	edgesR = cv2.resize(edges, (800,600))
	
    cv2.imshow("frameOutput", frameR)
    cv2.imshow("edgesOutput", edgesR)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
video.release()
cv2.destroyAllWindows()
