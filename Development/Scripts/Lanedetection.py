#Imports
import cv2
import numpy as np

#My versions where
#OpenCV: 3.4.3
#Numpy: 1.15.4
#Python 3.7

#Shows Opencv/Numpy version you're using.
print ("OpenCV version: " + cv2. __version__)
print ("Numpy version: " + np.version.version)
#Videocapture
#Change to 0 if you want to use your first attached webcam.
video = cv2.VideoCapture("../VIDEOS/weg-spanje-2.mp4")

#Define region of interest
def roi(video, vertices):
	maskz = np.zeros_like(video)
	cv2.fillPoly(maskz, vertices, 255)
	masked = cv2.bitwise_and(video, maskz)
	return masked

while True:
	#Read
    ret, orig_frame = video.read()
    
    #Create Draw layer
    line_image = np.copy(orig_frame) * 0  
	
	#Gassianblur
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    
    #Color to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Threshhold for yellow lanes
    low_yellow = np.array([18, 94, 140], dtype=np.uint8)
    up_yellow = np.array([48, 255, 255], dtype=np.uint8)
    
    #Threshold for white lanes
    low_white = np.array([0,0,165], dtype=np.uint8)
    up_white = np.array([255,255,255], dtype=np.uint8)
    
    #Inrages
    mask1 = cv2.inRange(hsv, low_yellow, up_yellow)
    mask2 = cv2.inRange(hsv, low_white, up_white)
    
    #Put these in a single mask
    mask = cv2.bitwise_or(mask1, mask2)
    
    #Check
    target = cv2.bitwise_and(frame,frame, mask=mask)
    
    #Canny
    edges = cv2.Canny(target, 75, 150)
    
    #Region of interest points
    vertices = np.array([[200,650],[450,500],[450,500],[600,425],[750,425],[1250,650],
                         ], np.int32)
        
    edges = roi(edges,[vertices])
    
    #The lines
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=20)
    
    #Uncomment this to see the Region of Interest lines (you can adjust these with the vertices array)
    
    #cv2.polylines(frame,[vertices],True,(0,255,255))
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            #Draw lines
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10) 			
            
            #Overlay
            lines_edges = cv2.addWeighted(frame, 1, line_image, 1, 0)
    
    #Give name to window
    cv2.namedWindow("frameOutput", cv2.WINDOW_NORMAL)
    cv2.namedWindow("edgesOutput", cv2.WINDOW_NORMAL)
    
    #Resize
    frameR = cv2.resize(lines_edges, (1280,720))
    edgesR = cv2.resize(edges, (1280,720))
	
	#Show frame ouput with overlay
    cv2.imshow("frameOutput", frameR)
    #Show canny output
    cv2.imshow("edgesOutput", edgesR)
	
	#Press 'q' to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

#Break all after quit		
video.release()
cv2.destroyAllWindows()
