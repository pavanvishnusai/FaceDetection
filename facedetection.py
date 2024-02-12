import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0)
temp = 0

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    
    if type(faces) is tuple :
        print(0)
        temp = 0
    else:
        print(1)
        temp = 1
    k = cv2.waitKey(30) & 0xff
    if k==27:
       break
    if temp == 1 :
        break
cap.release()