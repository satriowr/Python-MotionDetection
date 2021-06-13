import cv2 

camera = cv2.VideoCapture(0)

while camera.isOpened():
    retrive, frame1 = camera.read()
    retrive, frame2 = camera.read()
    different = cv2.absdiff(frame1, frame2) 
    gray = cv2.cvtColor(different, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshold, None)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    x = 0
    for i in contours:
        if cv2.contourArea(i) < 700 :
            continue
        
        x1, y1, x2, y2 = cv2.boundingRect(i)
        cv2.rectangle(frame1, (x1, y1), (x1+y1, x2+y2), (0, 255, 0), 2)
        x += 1

    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow('Frame', frame1)


