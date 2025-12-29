from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  
import mysql.connector 
import cv2
import os

class Student:
    
    def __init__(self, root): 
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # Resolve Images directory
        self.image_dir = os.path.join(os.path.dirname(__file__), "Images")
        
        def load_image(filename, width, height):
            """Load and resize image from Images folder"""
            img_path = os.path.join(self.image_dir, filename)
            if not os.path.exists(img_path):
                print(f"Warning: Image not found at {img_path}")
                return None
            img = Image.open(img_path)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)

        ########## Variables #############
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_radio1=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


# Load and display header images
        self.photoimg1 = load_image("download.jpg", 500, 130)
        if self.photoimg1:
            f_lbl = Label(self.root, image=self.photoimg1)
            f_lbl.place(x=0, y=0, width=500, height=130)
        
        self.photoimg2 = load_image("people.jpg", 500, 130)
        if self.photoimg2:
            f_lbl = Label(self.root, image=self.photoimg2)
            f_lbl.place(x=500, y=0, width=500, height=130)

        self.photoimg3 = load_image("camera.jpg", 500, 130)
        if self.photoimg3:
            f_lbl = Label(self.root, image=self.photoimg3)
            f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background Image 
        self.photoimg = load_image("people.jpg", 1530, 620)
        if self.photoimg:
            bg_img = Label(self.root, image=self.photoimg)
            bg_img.place(x=0, y=130, width=1630, height=620)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",33,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1320,height=500)
        
        #Left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=640,height=480)

        # Image inside student details
        self.photoimgleft = load_image("download.jpg", 720, 130)
        if self.photoimgleft:
            f_lbl = Label(Left_frame, image=self.photoimgleft)
            f_lbl.place(x=0, y=0, width=720, height=130)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=620,height=120)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)

        # course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo.grid(row=0,column=3,padx=2,pady=2,sticky=W)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)

        # year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)

        # semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12 ,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)     
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        sem_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)
        sem_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        sem_combo.current(0)

        #student information
        student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student information",font=("times new roman",12,"bold"))
        student_frame.place(x=10,y=260,width=620,height=180)

        # Student ID
        studentid_label=Label(student_frame,text="Student ID",font=("times new roman",12 ,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=2,sticky=W) 

        studentid_entry=ttk.Entry(student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12 ,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=2,sticky=W)

        # Student Name
        studentname_label=Label(student_frame,text="Student Name",font=("times new roman",12 ,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=2,sticky=W)
        studentname_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12 ,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=2,sticky=W)

        # Class Division
        classdiv_label=Label(student_frame,text="Class Division",font=("times new roman",12 ,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)    

        # classdiv_entry=ttk.Entry(student_frame,textvariable=self.var_div,width=20,font=("times new roman",12 ,"bold"))
        # classdiv_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

        classdiv_combo=ttk.Combobox(student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        classdiv_combo.grid(row=1,column=1,padx=10,pady=2,sticky=W)
        classdiv_combo["values"]=("A","B","C","D")
        classdiv_combo.current(0)

        # Roll Number
        rollno_label=Label(student_frame,text="Roll Number",font=("times new roman",12 ,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=2,sticky=W)
        rollno_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12 ,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=2,sticky=W)

        # Gender
        gender_label=Label(student_frame,text="Gender",font=("times new roman",12 ,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)
       

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo.grid(row=2,column=1,padx=10,pady=2,sticky=W)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)

        # Date of Birth
        dob_label=Label(student_frame,text="D.O.B",font=("times new roman",12 ,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)
        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12 ,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

       
        # Email
        email_label=Label(student_frame,text="Email",font=("times new roman",12 ,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)
        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",12 ,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)


        # Phone No
        phoneno_label=Label(student_frame,text="Phone No",font=("times new roman",12 ,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=2,sticky=W) 
        phoneno_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12 ,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)

         # Address
        address_label=Label(student_frame,text="Address",font=("times new roman",12 ,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=2,sticky=W)
        address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=20,font=("times new roman",12 ,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

        # Teacher Name
        teachername_label=Label(student_frame,text="Teacher Name",font=("times new roman",12 ,"bold"),bg="white")
        teachername_label.grid(row=4,column=2,padx=10,pady=2,sticky=W)
        teachername_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12 ,"bold"))
        teachername_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)


        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)  

        
        radiobtn2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
 
        #button frame
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=0,width=620,height=80) 
        
        # Save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)   

        # Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # Delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2) 

        # Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3) 

        # Test DB Connection button
        test_db_btn=Button(btn_frame,text="Test DB",command=self.test_db_connection,width=16,font=("times new roman",12 ,"bold"),bg="#2e7d32",fg="white")
        test_db_btn.grid(row=0,column=4)

        # Capture Photo Sample button
        take_photo_btn=Button(btn_frame,text="Capture Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0,columnspan=2,pady=5)
       
       # Update Photo Sample button
        update_photo_btn=Button(btn_frame,text="Update Photo Sample",command=self.update_photo_sample,width=35,font=("times new roman",12 ,"bold"),bg="blue",fg="white") 
        update_photo_btn.grid(row=1,column=2,columnspan=2,pady=5)


        #Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=10,width=640,height=480)

        # Image inside student details
        self.photoimgright = load_image("download.jpg", 720, 130)
        if self.photoimgright:
            f_lbl = Label(Right_frame, image=self.photoimgright)
            f_lbl.place(x=0, y=0, width=720, height=130)

        # Search System
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=620,height=70)

        # Search by
        search_label=Label(search_frame,text="Search By",font=("times new roman",12 ,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo.grid(row=0,column=1,padx=2,pady=5, sticky=W)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)

        # Search entry
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12 ,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        # Search button
        search_btn=Button(search_frame,text="Search",command="",width=14,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        showall_btn=Button(search_frame,text="Show All",command="",width=14,font=("times new roman",12 ,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        # Table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=620,height=250)

        # scroll bars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)  
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)  
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=150)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ######### Function to open student details window ##########
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            conn=None
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL@321",database="face_recognization")
                my_cursor=conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (Department, Course, Year, Semester, Student_id, name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    )
                )
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success","Student details saved successfully",parent=self.root)
            except Exception as err:
                messagebox.showerror("Error",f"Due to: {str(err)}",parent=self.root)
            finally:
                if conn:
                    conn.close()


         ########## fetch data ##########
    def fetch_data(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="MYSQL@321", database="face_recognization")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
        except Exception as err:
            messagebox.showerror("Error", f"Error fetching data: {str(err)}", parent=self.root)
        finally:
            if conn:
                conn.close()

    ######get cursor#########
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        
        if len(data) < 15:
            return

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

############# Update function ##############
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            conn=None
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL@321",database="face_recognization")
                    my_cursor=conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", 
                        (   self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    self.fetch_data()
                else:
                    if not update:
                        return
            except Exception as err:
                messagebox.showerror("Error",f"Due to: {str(err)}",parent=self.root)
            finally:
                if conn:
                    conn.close()
    
        
    ########### Delete Function ##############
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL@321",database="face_recognization")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM student WHERE Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else: 
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as err:
                messagebox.showerror("Error",f"Due to: {str(err)}",parent=self.root)


    ############# Reset Function ##############
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    ##########generate data set or take photo sample##########
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL@321",database="face_recognization")
                my_cursor=conn.cursor() 
                
                # Use the actual Student_id from the form
                id = self.var_std_id.get()
                
                my_cursor.execute(
                    "UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", 
                    (   self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load prebuilt model for frontal face
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!")
            except Exception as err:
                messagebox.showerror("Error",f"Due to: {str(err)}",parent=self.root)
            finally:
                if conn:
                    conn.close()




    
    def capture_photo_sample(self):
        messagebox.showinfo("Info","Capture Photo Sample not implemented yet",parent=self.root)

    def update_photo_sample(self):
        messagebox.showinfo("Info","Update Photo Sample not implemented yet",parent=self.root)



        ############ FUNCTION TO TEST DB CONNECTION ##############
    def test_db_connection(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="MYSQL@321", database="face_recognization")
            messagebox.showinfo("Database", "Connection successful.", parent=self.root)
        except Exception as err:
            messagebox.showerror("Database", f"Connection failed: {err}", parent=self.root)
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()