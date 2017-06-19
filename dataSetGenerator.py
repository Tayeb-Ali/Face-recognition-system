import numpy as np
import cv2
import sqlite3

try:
    cap = cv2.VideoCapture(0)
    print ("We Select Camera 1")
except:
    cap = cv2.VideoCapture(1)
    print ("We Select Camera 2")
faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')


def insertOrUpdate(Id, Name):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE People SET Name=' " + str(Name) + " ' WHERE ID=" + str(Id)
    else:
        cmd = "INSERT INTO People(ID,Name) Values(" + str(Id) + ",' " + str(Name) + " ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()


id = raw_input('enter user_id: ')
name = raw_input('enter user name: ')
insertOrUpdate(id, name)
sampleNum = 0

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1;
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

        cv2.rectangle(img, (x - 50, y - 50), (x + w + 50, y + h + 50), (0, 255, 0), 2)

    cv2.imshow("img", img)

    cv2.waitKey(10)

    if (sampleNum > 20):
        cap.release()
        cv2.destroyAllWindows()
        break