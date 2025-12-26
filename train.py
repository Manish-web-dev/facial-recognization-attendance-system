from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  
import mysql.connector 
import cv2
import os
import numpy as np

class Train:
    
    def __init__(self, root): 
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=10,y=0,width=1530,height=45)

        img_top = Image.open("Images/download.jpg")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=280)

        ##### Train Button #####
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=337,width=1530,height=112)


        img_bottom = Image.open("Images/people.jpg")
        img_bottom = img_bottom.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)   

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=450, width=1530, height=220)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            if cv2.waitKey(1)==13:  # 13 is Enter key
                break
        ids=np.array(ids)

        #=================Train the classifier and save=======================
        cv2.destroyAllWindows()
        
        try:
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
        except Exception as err:
            messagebox.showerror("Error",f"Training Failed: {str(err)}",parent=self.root)

       



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()