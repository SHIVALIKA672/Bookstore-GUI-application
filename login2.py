from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

class login2:
    def __init__(self, root):
        self.root = root
        self.root.title('books_WORLD')
        self.root.geometry("1000x600+0+0")
        self.root.resizable(False, False)

        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=0, y=0, height=600, width=1000)

        self.Icon = ImageTk.PhotoImage(Image.open(r"D:\Python miniproject\logo4.png"))
        self.Icon_photo = Label(Frame_login, image=self.Icon).place(x=400,y=50)

        title = Label(Frame_login, text="@SHELFTONS", font=("Goudy old style", 20, "bold"),fg="black",bg="pink").grid(row=0,column=0)

        desc1 = Label(Frame_login, text="                       \"Satisfy Your Thirst of Reading Here\"",
                     font=("Goudy old style", 20, "bold"),fg="yellow",bg="pink").grid(row=0,column=2)

        desc2 = Label(Frame_login, text="login here!!",
                     font=("Goudy old style", 20, "bold"),fg="blue",bg="pink").place(x=60,y=160)


        lb1_user = Label(Frame_login, text="User Name:-", font=("Goudy old style", 15, "bold"), fg="black",
                         bg="pink").place(x=30,y=200)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=30,y=230)

        lb2_userp = Label(Frame_login, text="Password:-", font=("Goudy old style", 15, "bold"), fg="black",
                          bg="pink").place(x=30,y=260)
        self.txt_userp = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_userp.place(x=30,y=290)

        desc1 = Label(Frame_login, text="New Member?",
                     font=("Goudy old style", 20, "bold"),fg="green",bg="pink").place(x=70,y=500)

        registerNow = Button(Frame_login,command=self.REG_function, text="Register Now", fg="red", bg="pink",
                       font=("times new roman", 20)).place(x=270,y=490)

        Login = Button(Frame_login,command=self.login_function, text="Login", fg="blue", bg="pink",
                       font=("times new roman", 15)).place(x=80,y=320)

    def REG_function(self):
        self.root.destroy()
        import register

    def login_function(self):
        if self.txt_userp.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        elif self.txt_userp.get() == "ADMIN" or self.txt_user.get() == "@seller":
            self.root.destroy()
            import seller 
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="GUI")
            cur = con.cursor(buffered=True)
            st = "select * from userss where username=%s and password=%s"
            vals = (self.txt_user.get(), self.txt_userp.get())
            cur.execute(st,vals)
            rows = cur.fetchone()
            if rows == None:
             messagebox.showerror("error", "INVALID USER NAME/PASSWORD", parent=self.root)
            else:
             messagebox.showinfo("welcom", "WELCOME", parent=self.root)
             self.root.destroy()
             import user    
            con.commit()
            con.close()

root = Tk()
obj = login2(root)
root.mainloop()
