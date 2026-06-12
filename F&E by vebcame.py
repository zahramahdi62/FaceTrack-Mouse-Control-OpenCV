#Calling libraries
import cv2
import pyautogui as robot

#Calling haarcascade
face_model = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")

#Reading the image from the camera
loop = True
cam = cv2.VideoCapture(0)
while loop :
    _,img = cam.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_model.detectMultiScale(gray)
    if (len(face)>0):
        x = face[0][0]
        y = face[0][1]
        x2 = x+face[0][2]
        y2 = y+face[0][3]
        gray_face = gray[y:y2,x:x2]
        eye = eye_model.detectMultiScale(gray_face,minSize=(30,30),scaleFactor=1.1,minNeighbors=5)
        imgout = img.copy()
        print ("x:",x,"y:,y")
    out = cv2.rectangle(imgout,(x,y),(x2,y2),(0,250,0),3)
    whith = (250,250,250)
    red = (0,0,250)
    rang = whith
    mouse_x = robot.position().x
    mouse_y = robot.position().y
    if x<200 :
        rang = red
        mouse_x = mouse_x-abs(x-200)
        robot.moveTo(mouse_x,mouse_y,0)
    if x2>450 :
        rang = red
        mouse_x = mouse_x + abs(x-450)
        robot.moveTo(mouse_x,mouse_y,0)
    if y<80 :
        rang = red
        mouse_y = mouse_y-abs(y-80)
        robot.moveTo(mouse_x,mouse_y,0)
    if y>350 :
        rang = red
        mouse_y =mouse_y +abs(y-350)
        robot.moveTo(mouse_x,mouse_y,0)
    out = cv2.rectangle(imgout,(200,80),(450,350),rang,1)
    ic = 0
    for (xe,ye,w,h)in eye :
        ic = 1
        cv2.rectangle(imgout,(xe+x,ye+y),(xe+w+x,ye+h+y),(0,0,250),1)
        if ic == 2 :
            break
        cv2.imshow('axl',out)
        if cv2.waitKey(1) == ord('q') :
            loop = False
            cv2.destroyAllWindows()
            cam.release()
            break
        
    
        