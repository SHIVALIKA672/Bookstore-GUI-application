from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

class login2:
    def __init__(self, root):
        self.root = root
        self.root.title('BOOKS_WORLD')
        self.root.geometry("1000x500+0+0")
        self.root.resizable(False, False)
         

root = Tk()
obj = login2(root)
root.mainloop()