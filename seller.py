from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql
import base64

class login3:
    def __init__(self, root):
     self.root = root
     self.root.title('books_WORLD')
     self.root.geometry("1000x600+0+0")
     self.root.resizable(False, False)

     Frame_details = Frame(self.root, bg="pink")
     Frame_details.place(x=0, y=0, height=600, width=1000)

     self.Icon = ImageTk.PhotoImage(Image.open(r"D:\Python miniproject\logo4.png"))
     self.Icon_photo = Label(Frame_details, image=self.Icon).place(x=420,y=50)

     title = Label(Frame_details, text="@SHELFTONS", font=("Goudy old style", 20, "bold"),fg="black",bg="pink").grid(row=0,column=0)

     desc1 = Label(Frame_details, text="\"Satisfy Your Thirst of Reading Here\"",
                     font=("Goudy old style", 20, "bold"),fg="yellow",bg="pink").grid(row=0,column=2)

     lb1_bname = Label(Frame_details, text="Book Name:-", font=("Goudy old style", 15, "bold"), fg="red",bg="PINK").grid(row=1,column=0)
     self.txt_bname = Entry(Frame_details,width=20, font=("times new roman", 15), bg="white")
     self.txt_bname.grid(row=1,column=1)

     lb2_bauthor = Label(Frame_details, text="Author:-", font=("Goudy old style", 15, "bold"), fg="red",bg="PINK").grid(row=2,column=0)
     self.txt_bauthor = Entry(Frame_details,width=20, font=("times new roman", 15), bg="white")
     self.txt_bauthor.grid(row=2,column=1)

     lb3_isbn = Label(Frame_details, text="ISBN:-", font=("Goudy old style", 15, "bold"), fg="red",bg="PINK").grid(row=3,column=0)
     self.txt_isbn = Entry(Frame_details,width=20, font=("times new roman", 15), bg="white")
     self.txt_isbn.grid(row=3,column=1)

     lb4_cost = Label(Frame_details, text="Cost:-", font=("Goudy old style", 15, "bold"), fg="red",bg="PINK").grid(row=4,column=0)
     self.txt_cost = Entry(Frame_details,width=20, font=("times new roman", 15), bg="white")
     self.txt_cost.grid(row=4,column=1)

     lb5_image = Label(Frame_details, text="Image:-", font=("Goudy old style", 15, "bold"), fg="red", bg="PINK").grid(row=5, column=0)
     self.button = Button(Frame_details,font=("Goudy old style", 15, "bold"),fg="PINK", bg="black", text="Browse A file", command=self.fileDailogg)
     self.button.grid(column=1,row=5)

     UPDATE = Button(Frame_details,command=self.UPDATEE_function, text="UPDATE", fg="blue", bg="PINK",
                     font=("times new roman", 15)).grid(row=6, column=0)

     back = Button(Frame_details, command=self.back_function1, text="back to login", fg="BLUE", bg="PINK",
                       font=("times new roman", 15)).grid(row=6,column=1)



    def fileDailogg(self):
     self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg",".jpg"),("png",".png")))
     print(self.fileName)
     with open(self.fileName, "rb") as image_file:
          self.data = base64.b64encode(image_file.read())

    def UPDATEE_function(self):
        if self.txt_bname.get() == "" or self.txt_bauthor.get()=="" or self.txt_isbn.get()=="" or self.txt_cost.get()=="" :
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
          con = mysql.connector.connect(host="localhost",user="root",passwd="",database="GUI")
          cur = con.cursor(buffered=True)
          st = "INSERT INTO detailss (name,author,isbn,cost,image) VALUES ( %s, %s, %s, %s, %s)"
          print(type(self.data))
          vals = (self.txt_bname.get(), self.txt_bauthor.get(),self.txt_isbn.get(),self.txt_cost.get(),self.data)
          cur.execute(st,vals)
          con.commit()
          con.close()
          messagebox.showinfo("welcome", "UPLOAD SUCCESSFUL", parent=self.root)

    def back_function1(self):
        self.root.destroy()
        import login2





     
root = Tk()
obj = login3(root)
root.mainloop()