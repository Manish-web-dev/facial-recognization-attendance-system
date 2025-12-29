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
        self.root.title("Face Recognition Attendance System")
        self.root.config(bg="#0d1b2a")
        
        # Resolve assets directory and load images
        self.assets_dir = os.path.join(os.path.dirname(__file__), "Images")
        
        # Load background
        try:
            imgbg = Image.open(os.path.join(self.assets_dir, "background.png"))
            imgbg = imgbg.resize((1530, 790), Image.Resampling.LANCZOS)
            self.photobg = ImageTk.PhotoImage(imgbg)
            bg_lbl = Label(self.root, image=self.photobg)
            bg_lbl.place(x=0, y=0, width=1530, height=790)
        except:
            pass
        
        # Page title at top
        title_lbl = Label(self.root,
                  text="FACE RECOGNIZATION ATTENDANCE SYSTEM",
                  font=("times new roman", 28, "bold"),
                  bg="#0d1b2a", fg="#00bfff")
        title_lbl.place(x=0, y=10, width=1530, height=40)

        # Main container
        self.create_grid_layout()
    
    def load_image(self, filename, width, height):
        """Load and resize image from Images folder"""
        try:
            path = os.path.join(self.assets_dir, filename)
            img = Image.open(path)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return None
    
    def create_grid_layout(self):
        """Create 3x3 grid of buttons with dark cyberpunk theme"""
        # Grid configuration: spacing and sizing
        start_x = 80
        start_y = 60
        cell_width = 460
        cell_height = 230
        padding = 10
        
        # Define grid items: (row, col, image_file, button_text, command)
        grid_items = [
            # Row 0
            (0, 0, "student details.png", "STUDENT DETAILS", self.student_details),
            (0, 1, "facedetect.png", "FACE DETECTOR", self.face_data),
            (0, 2, "attendance.png", "ATTENDANCE", lambda: None),
            # Row 1
            (1, 0, "train.png", "TRAIN DATA", self.train_data),
            (1, 1, "help.png", "HELP DESK", lambda: None),
            (1, 2, "photos.png", "PHOTOS", self.open_img),
            # Row 2
            (2, 0, "student details.png", "DEVELOPER", lambda: None),
            (2, 1, "student details.png", "DEVELOPER", lambda: None),
            (2, 2, "exit.png", "EXIT", self.on_exit),
        ]
        
        # Create each grid cell
        for row, col, img_file, btn_text, cmd in grid_items:
            x = start_x + col * (cell_width + padding)
            y = start_y + row * (cell_height + padding)
            
            # Load image
            photo = self.load_image(img_file, cell_width, cell_height)
            
            # Create frame for the cell
            cell_frame = Frame(self.root, bg="#0d1b2a", highlightbackground="#00bfff", highlightthickness=2)
            cell_frame.place(x=x, y=y, width=cell_width, height=cell_height)
            
            # Add image if loaded
            if photo:
                img_lbl = Label(cell_frame, image=photo, bg="#0d1b2a")
                img_lbl.image = photo
                img_lbl.place(x=0, y=0, width=cell_width, height=cell_height)
            
            # Add button label/overlay
            btn = Button(cell_frame, text=btn_text, command=cmd, cursor="hand2",
                        font=("Segoe UI", 11, "bold"), bg="#1a3a52", fg="#00bfff",
                        activebackground="#0d5a7a", activeforeground="#00ffff",
                        relief=FLAT, bd=0, padx=5, pady=5)
            btn.place(x=0, y=cell_height-40, width=cell_width, height=40)

    def on_exit(self):
        """Exit application"""
        self.root.quit()

    def open_img(self):
        """Open the photos/data folder"""
        if os.path.exists("Data"):
            os.startfile("Data")
        else:
            os.startfile(self.assets_dir)

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