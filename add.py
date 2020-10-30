


"""Made by Rno-59 -> Mohit Sharma (11906579)"""


#import all modules 
from tkinter import*
from tkinter  import messagebox
import pandas as pd
#import regular expression and os 
import re 
import os
# we use Tk class to create the main window 
    
#call back function for validation user  RegNo
def validate_regno(user_regno):
    if user_regno.isdigit():
        return True
    elif user_regno == "":
        return True
    else:
        messagebox.showinfo('Information', 'only Digits are allowed for regno')
        return False
    
    
def addButton():
    fullName=v_fName.get()
    RegNo=v_regNo.get()
    SupervisorName=v_supName.get()
    supId=v_supid.get()
    Topic=v_topic.get()

    
    data= pd.read_csv("allocationtable.csv")
    temp = pd.DataFrame([[RegNo,fullName,supId,SupervisorName,Topic]], columns=["regno", "name", "supid", "supname", "topic"])
    data = data.append(temp,ignore_index=True)
    data.to_csv("allocationtable.csv",index=None)


#Funcation for Validating all other user input fields
def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo('Information','Please Enter Full Name to proceed')
    elif v_regNo.get()== "":
        messagebox.showinfo('Information','Please Enter RegNo to proceed')
    elif len(v_regNo.get())!=8:
        messagebox.showinfo('Information','Please Enter Eight digit RegNo')
    elif v_supName.get()=="":
        messagebox.showinfo('Information','Please Enter Supervisor full Name')
    elif v_supid.get()== "":
        messagebox.showinfo('Information','Please Enter supervisor reg. No RegNo to proceed')
    elif v_topic.get()== "":
        messagebox.showinfo('Information','Please enter Topic')
    else:
        addButton()

#functions to clear all user input in fields
def clearAllFields():
    v_fName.set("")
    v_regNo.set("")
    v_supName.set("")
    v_supregNo.set("")
    v_emailId.set("")
    v_topic.set("")

def editButton():
    os.system("editanddelete.py")
    
def listButton():
    os.system("list.py")    
    
window=Tk()
window.title("Welcome to User Registration Screen")
window.geometry('500x500')
window.configure(background="light blue")
v_fName=StringVar()
v_regNo=StringVar()
v_supName=StringVar()
v_supid=StringVar()
v_topic=StringVar()


lb_heading=Label(window,text="Add Details",width=20,font=("bold",20),bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="Student Full Name",width=20,font=("bold",10),bg="light blue")
lb_fullname.place(x=90,y=100)
#Entry allows to fill any kind of character in string
entry_fullname=Entry(window,textvariable=v_fName)
entry_fullname.place(x=230,y=100)
lb_regNo=Label(window,text="Reg. No.",width=20,font=("bold",10),bg="light blue")
lb_regNo.place(x=90,y=125)
entry_regNo=Entry(window,textvariable=v_regNo)
entry_regNo.place(x=230,y=130)
entry_regNo.config(validate="key",validatecommand=("valid_regNo",'%p'))
lb_supName=Label(window,text="Supervisor Name",width=20,font=("bold",10),bg="light blue")
lb_supName.place(x=90,y=155)
entry_supName=Entry(window ,textvariable=v_supName)
entry_supName.place(x=230,y=160)
lb_topic=Label(window,text="Supervisor Id",width=20,font=("bold",10),bg="light blue")
lb_topic.place(x=80,y=190)
entry_topic=Entry(window,textvariable=v_supid)
entry_topic.place(x=230,y=195)
lb_topic=Label(window,text="Topic",width=20,font=("bold",10),bg="light blue")
lb_topic.place(x=80,y=220)
entry_topic=Entry(window,textvariable=v_topic)
entry_topic.place(x=230,y=220)
btn_add=Button(window,text="ADD",command=validateAllFields, bg="dark blue",fg="white",font=("bold",10)).place(x=250,y=270)
btn_edit=Button(window,text="EDIT Or DELETE", command=editButton, bg="dark blue", fg="white",font=("bold",10)).place(x=100,y=330)
btn_clear=Button(window,text="CLEAR",bg="dark blue",fg="white",font=("bold",10)).place(x=260,y=330)
btn_list=Button(window,text="LIST", command=listButton, bg="dark blue",fg="white",font=("bold",10)).place(x=350,y=330)
window.mainloop()




         
    

