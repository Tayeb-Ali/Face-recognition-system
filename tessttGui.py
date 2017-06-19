from PyQt4 import QtCore, QtGui
import numpy as np
import cv2
import sqlite3
import os
import cv2
import numpy as np
from PIL import Image
from PyQt4.QtGui import QMessageBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(585, 495)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 380, 211, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.but_Add = QtGui.QPushButton(self.verticalLayoutWidget)
        self.but_Add.setCheckable(False)
        self.but_Add.setObjectName(_fromUtf8("but_Add"))
        self.verticalLayout.addWidget(self.but_Add)
        self.but_Train = QtGui.QPushButton(self.verticalLayoutWidget)
        self.but_Train.setObjectName(_fromUtf8("but_Train"))
        self.verticalLayout.addWidget(self.but_Train)
        self.but_Detact = QtGui.QPushButton(self.verticalLayoutWidget)
        self.but_Detact.setAutoDefault(True)
        self.but_Detact.setDefault(False)
        self.but_Detact.setFlat(False)
        self.but_Detact.setObjectName(_fromUtf8("but_Detact"))
        self.verticalLayout.addWidget(self.but_Detact)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(249, 140, 61, 201))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_3.setEnabled(True)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 140, 191, 201))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.txt_ID = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_ID.setEnabled(True)
        self.txt_ID.setMaxLength(20)
        self.txt_ID.setObjectName(_fromUtf8("txt_ID"))
        self.verticalLayout_3.addWidget(self.txt_ID)
        self.txt_Name = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_Name.setObjectName(_fromUtf8("txt_Name"))
        self.verticalLayout_3.addWidget(self.txt_Name)
        self.txt_Age = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_Age.setObjectName(_fromUtf8("txt_Age"))
        self.verticalLayout_3.addWidget(self.txt_Age)
        self.txt_Gender = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_Gender.setObjectName(_fromUtf8("txt_Gender"))
        self.verticalLayout_3.addWidget(self.txt_Gender)
        self.txt_Any = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.txt_Any.setObjectName(_fromUtf8("txt_Any"))
        self.verticalLayout_3.addWidget(self.txt_Any)
        self.but_Save = QtGui.QPushButton(Dialog)
        self.but_Save.setGeometry(QtCore.QRect(380, 350, 91, 31))
        self.but_Save.setObjectName(_fromUtf8("but_Save"))
        self.but_update = QtGui.QPushButton(Dialog)
        self.but_update.setGeometry(QtCore.QRect(280, 350, 81, 31))
        self.but_update.setObjectName(_fromUtf8("but_update"))
        self.Img_View = QtGui.QGraphicsView(Dialog)
        self.Img_View.setGeometry(QtCore.QRect(0, 0, 231, 171))
        self.Img_View.setObjectName(_fromUtf8("Img_View"))
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_5.raise_()
        self.but_Save.raise_()
        self.but_update.raise_()
        self.Img_View.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        #Button Add Menber Not Save Data
        self.but_Add.setText(_translate("Dialog", "AddNew", None))
        self.but_Add.clicked.connect(self.NewMenber)

        #Button Train The New Face
        self.but_Train.setText(_translate("Dialog", "Triner", None))
        self.but_Train.clicked.connect(self.TrainnerFce)

        #Button Test The Detact And Defin Thr Face
        self.but_Detact.setText(_translate("Dialog", "Detacti", None))

        #The Text Field
        self.label_2.setText(_translate("Dialog", "ID", None))
        self.label_3.setText(_translate("Dialog", "Username", None))
        self.label.setText(_translate("Dialog", "Age", None))
        self.label_4.setText(_translate("Dialog", "Gender", None))
        self.label_5.setText(_translate("Dialog", "Any", None))

        #Button Save Person Data
        self.but_Save.setText(_translate("Dialog", "Save", None))

        #Button Update Date
        self.but_update.setText(_translate("Dialog", "Update", None))

    #Func of Add New Face
    def NewMenber(self):
        try:
            cap = cv2.VideoCapture(0)
            print ("We Select Camera 1")

        except:
            cap = cv2.VideoCapture(1)
            print ("We Select Camera 2")
        faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

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

        #id = raw_input('enter user_id: ')
        id = self.txt_ID.text()
        #name = raw_input('enter user name: ')
        name = self.txt_Name.text()
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
    #End of func Add New Face

    #Func of Trainner Face
    def TrainnerFce(self):

        recognizer = cv2.createLBPHFaceRecognizer();
        path = 'dataSet'

        def getImagesWithID(path):

            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            IDs = []
            for imagePath in imagePaths:
                faceImg = Image.open(imagePath).convert('L');
                faceNp = np.array(faceImg, 'uint8')

                ID = int(os.path.split(imagePath)[-1].split('.')[1])

                faces.append(faceNp)
                print ID
                IDs.append(ID)
                cv2.imshow('trainer', faceNp)

                cv2.waitKey(10)
                if cv2.waitKey() == 10:
                    print "End Trainner"
                    QMessageBox.information( "Message", "End Trainner")

            return IDs, faces

        # paththdb ='dataSet/Thumbs.db'
        try:
            os.remove('dataSet/Thumbs.db')
            print "don"
        except:
            print "is emputy"

        Ids, faces = getImagesWithID(path)
        recognizer.train(faces, np.array(Ids))
        recognizer.save('recognizer/trainningData.yml')
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

