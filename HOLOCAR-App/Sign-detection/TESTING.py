import cv2

source = cv2.imread("/source/of/your_stop_sign")
template = cv2.imread("our/template")
(tempH, tempW) = template.shape[:2]

result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF)
(minVal, maxVal, minLoc, (x, y)) = cv2.minMaxLoc(result)

cv2.rectangle(source, (x, y), (x + tempW, y + tempH), (0, 255, 0), 2)

cv2.imshow("source", source)
cv2.imshow("template", template)
cv2.waitKey(0)
