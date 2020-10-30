


"""Made by Rno-31 -> Utkarsh Agrawal (11902308)"""


from tkinter import *
import pandas as pd
import os


def saveChanges(pos):
    save_status=authenticate_entire()
    if(save_status == True):
        datatable= pd.read_csv("allocationtable.csv")
        datatable.drop(pos, inplace=True)
        datatabletemp = pd.DataFrame([[regno_auth, name_auth, supid_auth, supname_auth, topic_auth]], columns=["regno", "name", "supid", "supname", "topic"])
        datatable = datatable.append(datatabletemp,ignore_index=True)
        datatable.to_csv("allocationtable.csv",index=None)
        print_label.config(text="changes saved")
        messagebox.showinfo("message","changes saved")


def authenticate_entire():
    global regno_auth
    global name_auth
    global supid_auth
    global supname_auth
    global topic_auth
    
    regno_auth=regno_result.get()
    name_auth=name_result.get()
    supid_auth=supid_result.get()
    supname_auth=supname_result.get()
    topic_auth=topic_result.get()
    
    print(name_auth)
    if(regno_auth=="" or name_auth=="" or supid_auth=="" or supname_auth=="" or topic_auth==""):
        print_label.config(text="Fill all the fields")
        return False
    elif(not reg.isdigit() or not (len(str(reg))==8)):
        print_label.config(text="Enter valid registration number")
        return False
    elif(not(name_auth[0].isalpha())):
        print_label.config(text="student name should start with alphabet")
        return False
    elif(not(supname_auth[0].isalpha())):
        print_label.config(text="supervisor name should start with alphabet")
        return False
    if((' ' in supid_auth) == True):
        print_label.config(text="id should not contain any space")
        return False
    
    return True
        
    
    
def resultPage(pos):
    global result_screen
    result_screen = Toplevel()
    result_screen.title("Edit screen")
    result_screen.geometry("500x400")
    
    global regno_result
    global name_result
    global supid_result
    global supname_result
    global topic_result
    global print_label
    
    regno_result=StringVar()
    name_result=StringVar()
    supid_result=StringVar()
    supname_result=StringVar()
    topic_result=StringVar()
    
    frame1=Frame(result_screen,bg="green")
    frame1.place(x=40,y=40)
    
    regno_label=Label(frame1,text="reg no",font=("Courier", 13),width=40,bg="green").pack()
    regno_entry=Entry(frame1, bd=4, textvariable=regno_result)
    regno_entry.pack()
    
    name_label=Label(frame1,text="name",font=("Courier", 13),bg="green").pack()
    name_entry=Entry(frame1, bd=4, textvariable=name_result)
    name_entry.pack()
    
    supid_label=Label(frame1,text="supervisor id",font=("Courier", 13),bg="green").pack()
    supid_entry=Entry(frame1, bd=4, textvariable=supid_result)
    supid_entry.pack()
    
    supname_label=Label(frame1,text="supervisor name",font=("Courier", 13),bg="green").pack()
    supname_entry=Entry(frame1, bd=4, textvariable=supname_result)
    supname_entry.pack()
    
    topic_label=Label(frame1,text="topic alloted",font=("Courier", 13),bg="green").pack()
    topic_entry=Entry(frame1, bd=4, textvariable=topic_result)
    topic_entry.pack()    
    
    space = Label(frame1,text="", bg="green").pack()
    
    edit_button=Button(frame1, text="save changes", command = lambda:saveChanges(pos), bg="orange")
    edit_button.pack()
    
    print_label=Label(frame1, text="",font=("Courier", 12), bg="green")
    print_label.pack()
    
    datatable= pd.read_csv("allocationtable.csv")
    regno_result.set(datatable["regno"][pos])
    name_result.set(datatable["name"][pos])
    supid_result.set(datatable["supid"][pos])
    supname_result.set(datatable["supname"][pos])
    topic_result.set(datatable["topic"][pos])


def auth_regno():
    global reg
    reg=regno_main.get()
    if(reg==""):
        disp.config(text="Fill registration number in provided field")
        return False
    elif(not reg.isdigit() or not (len(str(reg))==8)):
        disp.config(text="Enter valid registration number")
        return False
    else:
        return True
    
    
def searchButton():
    search_status = auth_regno()
    if (search_status==True):
        count=-1
        search_position=-1
        datatable= pd.read_csv("allocationtable.csv")
        for i in datatable["regno"]:
            count+=1
            if(reg == str(i)):
                search_position=count
                break
            
        if (search_position>-1):
            resultPage(search_position)
        else:
            disp.config(text="registration number not found")


def delete():
    delete_status = auth_regno()
    if(delete_status==True):
        count=-1
        delete_position=-1
        datatable= pd.read_csv("allocationtable.csv")
        for i in datatable["regno"]:
            count+=1
            if(reg==str(i)):
                delete_position=count
                break
        if(delete_position>-1):
            datatable.drop(delete_position,inplace=True)
            datatable.to_csv("allocationtable.csv",index=None)
            disp.config(text="Deleted")
        else:
            disp.config(text="registration number not found")
            

def mainPage():
    global root
    root=Tk()
    root.title("Supervisor allocation portal for LPU")
    root.geometry("300x300") 
    global regno_main
    global disp
    regno_main = StringVar()
    search_label=Label(root,text="Enter registration number", height=3, width=100, font=("signboard",15), bg="purple").pack()
    spacing_label1=Label(root,text="", height=1, width=100).pack()
    search_entry=Entry(root, bd=4, textvariable=regno_main).pack()
    spacing_label2=Label(root,text="", height=1, width=100).pack()
    search_button=Button(root,text="search and open",bg="yellow", command = searchButton).pack()
    spacing_label3=Label(root,text="", height=1, width=100).pack()
    delete_button=Button(root, text="delete", bg="orange", command=delete).pack()
    disp=Label(root, height=1, width=100)
    disp.pack()
    root.mainloop()
 
mainPage()