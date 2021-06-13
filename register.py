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
        self.root.geometry("900x500+0+0")
        self.root.resizable(False, False)

        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=0, y=0, height=600, width=1000)


        title = Label(Frame_login, text="@SHELFTONS", font=("Goudy old style", 20, "bold"),fg="black",bg="pink").grid(row=0,column=0)

        desc1 = Label(Frame_login, text="              \"Satisfy Your Thirst of Reading Here\"",
                     font=("Goudy old style", 20, "bold"),fg="yellow",bg="pink").grid(row=0,column=2)

        lb1_user = Label(Frame_login, text="User name:-", font=("Goudy old style", 15, "bold"), fg="red",bg="pink").place(x=10, y=40)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=10, y=70 , width=800, height=35)

        lb2_userp = Label(Frame_login, text="Set Password:-", font=("Goudy old style", 15, "bold"), fg="red",bg="pink").place(x=10, y=110)
        self.txt_userp = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_userp.place(x=10, y=140 , width=800, height=35)

        lb3_userp1 = Label(Frame_login, text="Re-entre Password:-", font=("Goudy old style", 15, "bold"), fg="red",bg="pink").place(x=10, y=180)
        self.txt_userp1 = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_userp1.place(x=10, y=210 , width=800, height=35)

        lb4_phoneno = Label(Frame_login, text="Enter Your Phone Number:-", font=("Goudy old style", 15, "bold"), fg="red",bg="pink").place(x=10, y=250)
        self.txt_phoneno = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_phoneno.place(x=10, y=280 , width=800, height=35)

        lb5_age = Label(Frame_login, text="Enter Your age:-", font=("Goudy old style", 15, "bold"), fg="red",bg="pink").place(x=10, y=320)
        self.txt_age = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_age.place(x=10, y=350 , width=800, height=35)

        register = Button(Frame_login,command=self.Register_function, text="          Register          ", fg="green", bg="pink", font=("times new roman", 15)).place( x=10, y=390)
        back = Button(Frame_login,command=self.back_function,  text="back", fg="blue", bg="pink",
                       font=("times new roman", 15)).place(x=10, y=430)

    def back_function(self):
        self.root.destroy()
        import login2

    def Register_function(self):
        if self.txt_user.get() == "" or self.txt_userp.get() == "" or self.txt_userp1.get() == "" or self.txt_phoneno.get() == "" or self.txt_age.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        elif self.txt_userp.get() != self.txt_userp1.get():
             messagebox.showerror("Error","Password does not match",parent = self.root)
        elif int(self.txt_age.get())>100:
                messagebox.showerror("Error","Invalid age!",parent = self.root)
        elif int(self.txt_phoneno.get())<1000000000:
                messagebox.showerror("Error","Invalid contact number!",parent = self.root)
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="GUI")
            cur = con.cursor(buffered=True)
            st = "INSERT INTO userss (username,password,phoneno,age) VALUES (%s, %s, %s, %s)"
            vals = (self.txt_user.get(), self.txt_userp.get(),self.txt_phoneno.get(),self.txt_age.get())
            cur.execute(st,vals)
            con.commit()
            con.close()
            messagebox.showinfo("welcom", "registered SUCCESSFULLY", parent=self.root)        

root = Tk()
obj = login2(root)
root.mainloop()
