from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql
import base64

class userHome:
    def __init__(self, root):
     self.root = root
     self.root.title('books_WORLD')
     self.root.geometry("1000x600+0+0")
     self.root.resizable(False, False)

     Frame_home1 = Frame(self.root, bg="pink")
     Frame_home1.place(x=0, y=0, height=50, width=1000)

     Frame_home2 = Frame(self.root, bg="coral")
     Frame_home2.place(x=220, y=60, height=550, width=1000)

     self.txt_search = Entry(Frame_home2,width=23, font=("times new roman", 15), bg="white")
     self.txt_search.place(x=290,y=20)

     self.txt_bname = StringVar()
     self.txt_bauthor = StringVar()
     self.txt_cost = StringVar()

     self.Frame_image = Frame(Frame_home2, bg="white")
     self.Frame_image.place(x=300, y=50, height=295 ,width=200)
     self.txt_one = Entry(Frame_home2, textvariable=self.txt_bname, width=40, font=("times new roman", 15), bg="white")
     self.txt_one.place(x=200,y=350)
     self.txt_two = Entry(Frame_home2, textvariable=self.txt_bauthor, width=20, font=("times new roman", 15), bg="white")
     self.txt_two.place(x=300,y=380)
     self.txt_three = Entry(Frame_home2, textvariable=self.txt_cost, width=20, font=("times new roman", 15), bg="white")
     self.txt_three.place(x=300,y=410)


     search = Button(Frame_home2,comman=self.fetchone1_function, text="search", fg="blue", bg="coral",
                       font=("times new roman", 14)).place(x=530,y=15)

     buy = Button(Frame_home2,command=self.buy_function, text="Buy now", fg="blue", bg="coral",
                       font=("times new roman", 20)).place(x=340,y=450)



     Frame_home3 = Frame(self.root, bg="aqua")
     Frame_home3.place(x=0, y=60, height=550, width=210)

     title = Label(Frame_home1, text="@SHELFTONS", font=("Goudy old style", 20, "bold"),fg="black",bg="pink").grid(row=0,column=0)

     desc1 = Label(Frame_home1, text="\"Satisfy Your Thirst of Reading Here\"",
                     font=("Goudy old style", 20, "bold"),fg="yellow",bg="pink").place(x=400,y=0)

     desc2 = Label(Frame_home3, text="CATEGORY",
                     font=("Goudy old style", 20, "bold"),fg="black",bg="aqua").grid(row=0,column=0)

     Novel = Button(Frame_home3, text="Novel", fg="red", bg="aqua",
                       font=("times new roman", 20)).place(x=0,y=50)

     Biograhies = Button(Frame_home3, text="Biographies", fg="red", bg="aqua",
                       font=("times new roman", 20)).place(x=0,y=110)

     StoryBooks = Button(Frame_home3, text="kids", fg="red", bg="aqua",
                       font=("times new roman", 20)).place(x=0,y=170)


     logout = Button(Frame_home3,command=self.logout_function, text="LogOut", fg="black", bg="aqua",
                       font=("times new roman", 20)).place(x=0,y=460)

     self.Icon = ImageTk.PhotoImage(Image.open(r"D:\Python miniproject\logo.jpeg"))
     self.Icon_photo = Label(Frame_home3, image=self.Icon).place(x=0,y=260)




    def logout_function(self):
        self.root.destroy()
        import login2

    def buy_function(self):
        if self.txt_search.get() == "":
            messagebox.showerror("error", "Invalid Try !", parent=self.root)
        else:
                messagebox.showinfo("error", "Succesfully placed your order :)", parent=self.root)
        

    def fetchone1_function(self):
         if self.txt_search.get() == "":
            messagebox.showerror("error", "search field empty", parent=self.root)
         else:
            con = pymysql.connect(host="localhost", user="root", password="", database="GUI")
            cur = con.cursor()
            print(self.txt_search.get())
            cur.execute("SELECT * FROM detailss WHERE name=%s",
                        (self.txt_search.get()))
            rows = cur.fetchone()
            if rows != None:
                self.txt_bname.set(rows[0])
                self.txt_bauthor.set(rows[1])
                self.txt_cost.set(rows[3])
                BLOBimage = rows[4]
                print(type(BLOBimage))
                self.write_file(r"D:\Python miniproject\book.jpg", BLOBimage)
                self.ph1 = ImageTk.PhotoImage(Image.open(r"D:\Python miniproject\book.jpg"))
                self.ph1_photo = Label(self.Frame_image, image=self.ph1).grid(row=0, column=0)
            else:
                messagebox.showerror("error", " Not found!", parent=self.root)

    def make_image(self, path, blob):
     print(type(blob))
     self.write_file(blob, path)

    def write_file(self , filename, data):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, "wb") as fh:
            fh.write(base64.decodebytes(data))


root = Tk()
obj = userHome(root)
root.mainloop()