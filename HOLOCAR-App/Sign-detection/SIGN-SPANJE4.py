import cv2
import numpy as np

cap = cv2.VideoCapture("../../Video/template-matching/spanje/section-spanje3.mp4")
template = cv2.imread("../../Video/template-matching/spanje/image177.png", cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread("../../Video/template-matching/spanje/image176.png", cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread("../../Video/template-matching/spanje/image186.png", cv2.IMREAD_GRAYSCALE)
template4 = cv2.imread("../../Video/template-matching/spanje/image183.png", cv2.IMREAD_GRAYSCALE)

out = cv2.VideoWriter('sign-spanje4.mp4', -1, 20.0, (800,400))

w, h = template.shape[::-1]
w2, h2 = template.shape[::-1]
w3, h3 = template.shape[::-1]
w4, h4 = template.shape[::-1]

number1 = False

while True:
    _, frame = cap.read()
    out.write(frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    number1 = 0
    number2 = 0
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
 
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 3)
        number1 = 1;
        overlaySource = cv2.imread("../../Afbeeldingen/TrainingData/50km.png")
        overlay = cv2.resize(overlaySource, (50,100))
        rows,cols,channels = overlay.shape
		
        overlay=cv2.addWeighted(frame[250:250+rows, 250:250+cols],0.5,overlay,0.5,0)
        if number1 == 1 and number2 == 0:
			frame[20:20+rows, 20:20+cols ] = overlay
        else:
			frame[40:40+rows, 20:20+cols ] = overlay
			
		
        cv2.putText(frame,'60KM',(pt[0] + 10 + w, pt[1] + h), font, 1, (255,0,0), 1)
        

    result2 = cv2.matchTemplate(gray_frame, template2, cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(result2 >= 0.7)
    
    for pt in zip(*loc2[::-1]):
		cv2.rectangle(frame, pt, (pt[0] + w2, pt[1] + h2), (0, 80, 255), 3)
		number1 = 1;
		overlaySource = cv2.imread("../../Afbeeldingen/TrainingData/50km.png")
		overlay = cv2.resize(overlaySource, (50,100))
		rows,cols,channels = overlay.shape
		
		overlay=cv2.addWeighted(frame[250:250+rows, 250:250+cols],0.5,overlay,0.5,0)
		if number1 == 1 and number2 == 0:
			frame[20:20+rows, 20:20+cols ] = overlay
		else:
			frame[40:40+rows, 20:20+cols ] = overlay
		cv2.putText(frame,'Turn',(pt[0] + 10 + w, pt[1] + h), font, 1, (0,80,255), 1)
		
    result3 = cv2.matchTemplate(gray_frame, template3, cv2.TM_CCOEFF_NORMED)
    loc3 = np.where(result3 >= 0.7)
    
    for pt in zip(*loc3[::-1]):
		cv2.rectangle(frame, pt, (pt[0] + w3, pt[1] + h3), (0, 60, 255), 3)
		number2 = 1
		overlaySource = cv2.imread("../../Afbeeldingen/TrainingData/50km.png")
		overlay = cv2.resize(overlaySource, (100,100))
		rows,cols,channels = overlay.shape
		
		overlay=cv2.addWeighted(frame[250:250+rows, 250:250+cols],0.5,overlay,0.5,0)
		frame[20:20+rows, 120:120+cols ] = overlay
		cv2.putText(frame,'Turn',(pt[0] - 120 + w, pt[1] + h), font, 1, (0,80,255), 1)
	
    result4 = cv2.matchTemplate(gray_frame, template4, cv2.TM_CCOEFF_NORMED)
    loc4 = np.where(result4 >= 0.7)
    
    for pt in zip(*loc4[::-1]):
		cv2.rectangle(frame, pt, (pt[0] + w4, pt[1] + h4), (255, 0, 0), 3)
		number2 = 1
		overlaySource = cv2.imread("../../Afbeeldingen/TrainingData/50km.png")
		overlay = cv2.resize(overlaySource, (100,100))
		rows,cols,channels = overlay.shape
		
		overlay=cv2.addWeighted(frame[250:250+rows, 250:250+cols],0.5,overlay,0.5,0)
		frame[20:20+rows, 20:20+cols ] = overlay
		cv2.putText(frame,'60KM',(pt[0] - 120 + w, pt[1] + h), font, 1, (255,0,0), 1)
    
    
	
    frameR = cv2.resize(frame, (800,400))
 
    cv2.imshow("Frame", frameR)
    
    print number1
 
    key = cv2.waitKey(1)
 
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
 
cap.release()
out.release()
cv2.destroyAllWindows()
