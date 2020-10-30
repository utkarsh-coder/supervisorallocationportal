


""""Made by Rno-20 -> Sankaramaddi nirmal kumar reddy (11901406)"""


from tkinter import *
from pandas import *
import os


def showList():
    list = Tk()
    list.geometry("1000x1000")
    listbox = Listbox(list, height=50, width=150, bg="light blue")
    list.configure(background="red")
    
    datatable= read_csv("allocationtable.csv")
    length = len(datatable["regno"])
    j=0
    for i in range(0,length):
        if (validateBeforePrint(i)):
            listbox.insert(j, "Regno.= "+str(datatable["regno"][i])+"     Name= "+str(datatable["name"][i])+
                           "     Supervisor id= "+str(datatable["supid"][i])+ "     Supervisor name= "+str(datatable["supname"][i])+
                           "     Topic= "+str(datatable["topic"][i]))
            listbox.insert(j+1, " ")
            j=j+2
        
    listbox.pack()
    list.mainloop()
        
    
def validateBeforePrint(x):
    datatablecheck= read_csv("allocationtable.csv")
    if(str(datatablecheck["regno"][x]).isdigit()==False):
        return False
    if(str(datatablecheck["supid"][x]).isdigit()==False):
        return False
    
    return True

showList()