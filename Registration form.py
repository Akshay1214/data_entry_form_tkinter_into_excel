from datetime import datetime
from openpyxl import *
from tkinter import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as pd

root = Tk()
root.geometry('500x500')
root.title("Data Entry Form")

label_0 = Label(root, text="Data Entry Form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Place",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Mumbai','Pune', 'Chandigargh', 'Banglore', 'Hyderabad', 'Chennai', 'Coimbatore', 'Other'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select Your Place') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Specialist",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(root, text="A.I. Engineer", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root, text="M.L. Engineer", variable=var2).place(x=350,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()