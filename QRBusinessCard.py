import tkinter as tk
import qrcode
import png
import tracemalloc
# from tkinter import *
from tkinter import messagebox,filedialog,PhotoImage,Tk,ttk,Frame,Label,Button,Entry,Text,StringVar,mainloop,RIDGE
from resizeimage import resizeimage
from PIL import Image, ImageTk


class QGen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR")
        self.root.resizable(False, False)
        style = ttk.Style()
        style.configure("BW.TLabel", background="orange")
        p1 = PhotoImage(file='logo/notepad.png')
        # Icon set for program window
        self.root.iconphoto(False, p1)

        self.var_regno = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_dept = tk.StringVar()
        self.download_Path = tk.StringVar()

        entryFrame = ttk.Frame(self.root, relief=RIDGE, style='BW.TLabel')
        entryFrame.place(x=50, y=100, width=500, height=380)

        title = ttk.Label(self.root, text="QR Business Card", font=("times new roman", 40), style="BW.TLabel").place(x=0, y=0, relwidth=1)
        title1 = Label(entryFrame, text="Details", font=("goudy old style", 20), bg='#043256',
                       fg='white').place(x=0,y=0,relwidth=1)

        lbl_code = Label(entryFrame, text="Name :", font=("times new roman", 15, 'bold'), bg='orange').place(x=20,y=60)
        lbl_name = Label(entryFrame, text="Company :", font=("times new roman", 15, 'bold'), bg='orange').place(x=20, y=100)
        lbl_dept = Label(entryFrame, text="E-mail :", font=("times new roman", 15, 'bold'), bg='orange').place(x=20,y=140)
        lbl_phno = Label(entryFrame, text="Tel. Number :", font=("times new roman", 15, 'bold'), bg='orange').place(x=20,y=180)
        lbl_folder = Label(entryFrame, text="Choose Folder : ", font=("times new roman", 15), bg='orange').place(x=20,y=220)

        txt_code = Entry(entryFrame, textvariable=self.var_regno, font=("times new roman", 15), bg='white').place(x=200,y=60)
        txt_name = Entry(entryFrame, textvariable=self.var_name, font=("times new roman", 15), bg='white').place(x=200,
                                                                                                                 y=100)
        txt_dept = Entry(entryFrame, textvariable=self.var_dept, font=("times new roman", 15), bg='white').place(x=200,
                                                                                                                 y=140)
        txt_phno = Entry(entryFrame, textvariable=self.var_phone, font=("times new roman", 15), bg='white').place(x=200,
                                                                                                                  y=180)
        txt_path = Entry(entryFrame, textvariable=self.download_Path, font=("times new roman", 15), bg='white').place(x=200,
                                                                                                                      y=220,
                                                                                                                      width=295)
        btn_gen = Button(entryFrame, text='Generate QR', command=self.gen, font=("times new roman", 18, 'bold'),bg='#2196f3',
                         fg='white').place(x=70, y=280, width=180, height=30)
        btn_clr = Button(entryFrame, text='Clear', command=self.clr, font=("times new roman", 18, 'bold'), bg='#607d8b',
                         fg='white').place(x=300, y=280, width=120, height=30)
        btn_dir = Button(entryFrame, text='download folder', command=self.Browse, font=("times new roman", 13, 'bold'), bg='#607d8b',
                         fg='white').place(x=300, y=250, width=180, height=20)
        btn_them = Button(entryFrame, text="Generate", command=self.gen,font=("times new roman", 13, 'bold'), bg='#607d8b',
                         fg='white').place(x=70, y=280, width=180, height=30)

        self.msg = ''
        self.lbl_msg = Label(entryFrame, text=self.msg, font=("times new roman", 20), bg='orange', fg='green')
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        qrFrame = Frame(self.root, bd=2, relief=RIDGE, bg='orange')
        qrFrame.place(x=600, y=100, width=250, height=380)
        title2 = Label(qrFrame, text="QR Code", font=("goudy old style", 20), bg='#043256', fg='white').place(x=0, y=0,
                                                                                                              relwidth=1)

        self.qrc = Label(qrFrame, text='No QR Code \nAvailable', font=('times new roman', 15), bg='#60bbf0', fg='white',
                         bd=1, relief=RIDGE)
        self.qrc.place(x=35, y=100, width=180, height=180)
# CLEAR StringVar
    def clr(self):
        self.var_regno.set('')
        self.var_name.set('')
        self.var_dept.set('')
        self.var_phone.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qrc.config(image='')
        self.download_Path.set('')

# SET DOWNLOAD DIRECTORY
    def Browse(self):
        download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.download_Path.set(download_Directory)
# DATA INPUTS VARIATIONS
    def gen(self):
        if self.var_regno.get() == '' or self.var_name.get() == '' or self.var_dept.get() == '' or self.var_phone.get() == '':
            self.msg = 'All Fields are Required !!'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data = (
                f"Name : {self.var_regno.get()}\nCompany : {self.var_name.get()}\nE-mail : {self.var_dept.get()}\nTel. Number : {self.var_phone.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code.save(self.download_Path.get() + '.png')
            qr_code.show(str(self.var_regno.get()))

            qr_code = resizeimage.resize_cover(qr_code, [180, 180])

            self.img = ImageTk.PhotoImage(qr_code)
            self.qrc.config(image=self.img)

            self.msg = "QR Code Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg, fg='green')

# LOOP IT
if __name__ == '__main__':
    root = tk.Tk()
    o = QGen(root)
    root.mainloop()
else:
    print('Client exit!')
