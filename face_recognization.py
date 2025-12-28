from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  
import mysql.connector 
import cv2
import os
import numpy as np


class Face_Recognization:
    
    def __init__(self, root): 
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=10,y=0,width=1530,height=45)

        img_left = Image.open("Images/camera.jpg")
        img_left = img_left.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=55, width=650, height=700)


        img_right = Image.open("Images/people.jpg")
        img_right = img_right.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right) 

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650, y=55, width=880, height=700)

        # ========== Face Recognition Button ==========
        b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",10,"bold"),bg="red",fg="white")
        b1_1.place(x=350,y=337,width=200,height=40)


    ### Face Recognition Function ###
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="MYSQL@321", database="face_recognization")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Department from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"ID:{id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord.append((x, y, w, h))  
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF
            if key == 13 or cv2.getWindowProperty("Welcome to Face Recognition", cv2.WND_PROP_VISIBLE) < 1:  # 13 is Enter or window closed
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization(root)
    root.mainloop()