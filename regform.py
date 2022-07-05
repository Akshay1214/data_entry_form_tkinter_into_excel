from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv

root = Tk()
root.geometry('520x540')
root.title("Data Entry Form")
root.configure(background='grey')

#defining function msg() using messagebox
def msg():
    select = var.get()
    if(select == 1 or select == 2):
        # get the index of the last character in the widget,if it is zero,it is empty
        if (e1.index("end") == 0):
            mb.showwarning('Missing details', 'Enter your First Name')
        elif(e2.index("end") == 0):
            mb.showwarning('Missing details', 'Enter your Last Name')
        elif(e3.index("end") == 0):
            mb.showwarning('Missing details', 'Enter your Email Id')
        else:
            mb.showinfo('Success', 'Registration done successfully')
    else:
            mb.showinfo('Missing details', 'Enter your gender')

#exporting entered data
def save():
    g = var.get()
    course = cvar.get()
    db = dob.get_date()
    d = db.strftime('%d/%m/%Y')
    now = datetime.datetime.now()
    if(g==1):
        gender ='Male'
    else:
        gender ='Female'

    #save data in csv file
    with open('data_file.xlsx', 'a') as fs:
        w = csv.writer(fs, dialect='excel-tab')
        w.writerow([now.strftime("%d-%m-%Y %H:%M"), e1.get(),e2.get(),e3.get(),d,gender,course])
        fs.close()

def saveinfo():
    save()
    msg()

# creating labels and entry widgets
l1 = Label(root, text="Data Entry Form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
l1.place(x=70,y=50)
l2 = Label(root, text="Full Name",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l2.place(x=70,y=130)
e1 = Entry(root,width=30,bd=2)
e1.place(x=240,y=130)
l3 = Label(root, text="Email ID",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l3.place(x=70,y=180)
e2 = Entry(root,width=30,bd=2)
e2.place(x=240,y=180)
l4 = Label(root, text="Date Of Birth",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l4.place(x=70,y=230)

# dateEntry -Date selection entry with drop-down calendar
dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
dob.place(x=240,y=230)

l5 = Label(root, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='grey')
l5.place(x=70,y=280)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
r1.place(x=235,y=280)
r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='grey')
r2.place(x=315,y=280)

l6 = Label(root, text="Contact Number",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l6.place(x=70,y=320)
e3 = Entry(root,width=30,bd=2)
e3.place(x=240,y=320)
l7 = Label(root, text="Select Place",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l7.place(x=70,y=370)

# create a dropdown menu with the OptionMenu widget
cvar = StringVar()
cvar.set("Select Place")
option = ("Mumbai", "Pune", "Chandigarh", "Banglore", "Chennai", "Coimbatore", "Patna", "Lucknow", "Ahmedabad", "Other")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=365,width=190)

# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
b1.place(x=120,y=440)
b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
b2.place(x=320,y=440)

root.mainloop()



# from datetime import datetime
# from openpyxl import *
# from tkinter import *
# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook
# import pandas as pd

# root = Tk()
# root.geometry('500x500')
# root.title("Data Entry Form")

# label_0 = Label(root, text="Data Entry Form",width=20,font=("bold", 20))
# label_0.place(x=90,y=53)


# label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
# label_1.place(x=80,y=130)

# entry_1 = Entry(root)
# entry_1.place(x=240,y=130)

# label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
# label_2.place(x=68,y=180)

# entry_2 = Entry(root)
# entry_2.place(x=240,y=180)

# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

# label_4 = Label(root, text="Place",width=20,font=("bold", 10))
# label_4.place(x=70,y=280)

# list1 = ['Mumbai','Pune', 'Chandigargh', 'Banglore', 'Hyderabad', 'Chennai', 'Coimbatore', 'Other'];
# c=StringVar()
# droplist=OptionMenu(root,c, *list1)
# droplist.config(width=15)
# c.set('Select Your Place') 
# droplist.place(x=240,y=280)

# label_4 = Label(root, text="Specialist",width=20,font=("bold", 10))
# label_4.place(x=85,y=330)
# var1 = IntVar()
# Checkbutton(root, text="A.I. Engineer", variable=var1).place(x=235,y=330)
# var2 = IntVar()
# Checkbutton(root, text="M.L. Engineer", variable=var2).place(x=350,y=330)

# Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# root.mainloop()