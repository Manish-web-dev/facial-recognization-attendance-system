from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # type: ignore
from student import Student
import os
from train import Train
from face_recognization import Face_Recognization

class Face_Recognition_System:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # Resolve assets directory and load images
        assets_dir = os.path.join(os.path.dirname(__file__), "Images")
        
        # Load and resize image  first image
        img1 = Image.open(os.path.join(assets_dir, "download.jpg"))
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Display first image using Label widget
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        # Load and resize image second image
        img2 = Image.open(os.path.join(assets_dir, "people.jpg"))
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Display second image using Label widget
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Load and resize image third image
        img3 = Image.open(os.path.join(assets_dir, "camera.jpg"))
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # Display third image using Label widget
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

         # Background Image 
        imgbg = Image.open(os.path.join(assets_dir, "people.jpg"))
        imgbg = imgbg.resize((1530, 620), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(imgbg)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=130, width=1530, height=620)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student Button 
        imgstd = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgstd = imgstd.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgstd = ImageTk.PhotoImage(imgstd)

        b1=Button(bg_img,image=self.photoimgstd,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=75,width=200,height=200)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1.place(x=200,y=250,width=200,height=40)

        #Detect face Button 
        imgdtc = Image.open(os.path.join(assets_dir, "people.jpg"))
        imgdtc = imgdtc.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgdtc = ImageTk.PhotoImage(imgdtc)

        b2=Button(bg_img,image=self.photoimgdtc,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=75,width=200,height=200)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2.place(x=500,y=250,width=200,height=40)

        #Attendance Button 
        imgatt = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgatt = imgatt.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgatt = ImageTk.PhotoImage(imgatt)

        b3=Button(bg_img,image=self.photoimgatt,cursor="hand2")
        b3.place(x=800,y=75,width=200,height=200)

        b3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b3.place(x=800,y=250,width=200,height=40)

        #Help Button 
        imghelp = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imghelp = imghelp.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimghelp = ImageTk.PhotoImage(imghelp)

        b4=Button(bg_img,image=self.photoimghelp,cursor="hand2")
        b4.place(x=1100,y=75,width=200,height=200)

        b4=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b4.place(x=1100,y=250,width=200,height=40)

        #Train data Button 
        imgtrain = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgtrain = imgtrain.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgtrain = ImageTk.PhotoImage(imgtrain)

        b5=Button(bg_img,image=self.photoimgtrain,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=320,width=200,height=200)

        b5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b5.place(x=200,y=500,width=200,height=40) 

        #Photos Button
        imgphoto = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgphoto = imgphoto.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgphoto = ImageTk.PhotoImage(imgphoto)

        b6=Button(bg_img,image=self.photoimgphoto,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=320,width=200,height=200)

        b6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b6.place(x=500,y=500,width=200,height=40)

        #Developer Button
        imgdev = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgdev = imgdev.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgdev = ImageTk.PhotoImage(imgdev)

        b7=Button(bg_img,image=self.photoimgdev,cursor="hand2")
        b7.place(x=800,y=320,width=200,height=200)

        b7=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b7.place(x=800,y=500,width=200,height=40)


        #Exit Button
        imgexit = Image.open(os.path.join(assets_dir, "camera.jpg"))
        imgexit = imgexit.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgexit = ImageTk.PhotoImage(imgexit)

        b8=Button(bg_img,image=self.photoimgexit,cursor="hand2")
        b8.place(x=1100,y=320,width=200,height=200)

        b8=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b8.place(x=1100,y=500,width=200,height=40)

    def open_img(self):
        os.startfile("Data")

    ############ FUNCTIONS TO OPEN NEW WINDOWS ##############
    
    def student_details(self):  
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):  
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    

    def face_data(self):  
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognization(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()