import numpy as np
import cv2
from PIL import Image
import pickle

import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load('recognizer/trainningData.yml')
path = 'dataSet'


def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 2, 1, 0, 2)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                          flags=cv2.WINDOW_NORMAL)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        id, conf = rec.predict(gray[y:y + h, x:x + w])

        profile = getProfile(id)
        if (profile != None):
            cv2.cv.PutText(cv2.cv.fromarray(img), "Name:" + str(profile[1]), (x, y + h + 30), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Age:" + str(profile[2]), (x, y + h + 60), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Gender:" + str(profile[3]), (x, y + h + 90), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(img), "Id "+str(profile[0]),(x,y+h+120),font,255)


            # roi_gray = gray[y:y+h, x:x+w]
            # roi_color = img[y:y+h, x:x+w]
    cv2.imshow('img', img)
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()