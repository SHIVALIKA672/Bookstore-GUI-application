from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

''' mainly used pithon libraries for GUI are:-1)kivy 2)Qt 3)wxPython 4)Tkinter

Tkinter:- its an inbuilt pithon module used to create simple GUI apps:(most commonly used) '''


class login1:
    def __init__(self, root):
        self.root = root
        self.root.title('books_WORLD')
        self.root.geometry("1000x500+0+0")
        self.root.resizable(False, False)


        # now for login frame ->
        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=0, y=0, height=600, width=1000)

        self.Icon = ImageTk.PhotoImage(Image.open(r"D:\Python miniproject\logo4.png"))
        self.Icon_photo = Label(Frame_login, image=self.Icon).place(x=400,y=50)
        

        title = Label(Frame_login, text="@SHELFTONS", font=("Goudy old style", 20, "bold"),fg="black",bg="pink").grid(row=0,column=0)

        desc1 = Label(Frame_login, text="                             \"Satisfy Your Thirst of Reading Here\"",
                     font=("Goudy old style", 20, "bold"),fg="yellow",bg="pink").grid(row=0,column=2)

        desc2_1 = Label(Frame_login, text="Get your favourite books",
                     font=("Goudy old style", 15, "bold"),fg="blue",bg="pink").place(x=10,y=100)
        desc2_2 = Label(Frame_login, text="At your doorstep!",
                     font=("Goudy old style", 15, "bold"),fg="blue",bg="pink").place(x=10,y=130)

        desc3 = Label(Frame_login, text="A room without books is a Body without Soul",
                     font=("Goudy old style", 13, "bold"),fg="black",bg="pink").place(x=10,y=160)




        Pagelogin = Button(Frame_login, command=self.open_function, text="Explore Now", fg="red", bg="white",
                       font=("times new roman", 15)).place(x=100,y=200)


        

        # DEFINING FUNCTIONS -> 
    def open_function(self):
        self.root.destroy()
        import login2

 

root = Tk()
obj = login1(root)
root.mainloop()
