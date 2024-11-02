from tkinter import *
from PIL import Image, ImageTk
import os
from Course import courseClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        # Load the logo image
        logo_path = "images/logo_p.png"
        if os.path.exists(logo_path):
            self.logo_dash = ImageTk.PhotoImage(file=logo_path)
       
        # Title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        
        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=250, y=70, width=1340, height=100)
        
        # Buttons
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_student.place(x=240, y=5, width=200, height=40)
        
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_result.place(x=460, y=5, width=200, height=40)
        
        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_view.place(x=680, y=5, width=200, height=40)
        
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_logout.place(x=900, y=5, width=200, height=40)
        
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_exit.place(x=1120, y=5, width=200, height=40)
        
        # Background Image
        bg_img_path = "images/bg.png"
        if os.path.exists(bg_img_path):
            self.bg_img = Image.open(bg_img_path)
            # Increased height to 450
            self.bg_img = self.bg_img.resize((920, 450), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            
            # Display Background Image
            self.lbl_bg = Label(self.root, image=self.bg_img)
            self.lbl_bg.place(x=650, y=180, width=920, height=500)
        
        # Statistics Labels
        self.lbl_course = Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b05", fg="white")
        self.lbl_course.place(x=630, y=690, width=300, height=100)
        
        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=950, y=690, width=300, height=100)
        
        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1270, y=690, width=300, height=100)
        
        # Footer
        footer = Label(self.root, text="Student Result Management System\nContact Us for any Technical Issue: 8318388719", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
        
    def add_course(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=courseClass(self.new_win)  

        
        

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()     