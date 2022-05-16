from tkinter import *
import time
import linecache
import tkinter as tk
import numbers
from time import strftime
from tkinter import filedialog

def valid_data():
    global Empty_flag
    global Warning_label
    global number_flag
    global number_label
    global Label_flag
    


    try:
        (float(R1.get()) and float(R2.get()) and float(VCC.get()))
        print(" a number")
        if(number_flag==True):
            number_label.destroy()
            #number_flag=False
        number_flag=False
    except ValueError:
        print("not a number")
        number_flag=True
        number_label = Label(text="Input Invalid:",fg="RED",font=('Helvetica',11))
        number_label.place(x=60,y=100)



def validation():
    global Empty_flag
    global Warning_label
    global Warning_flag
    global number_flag
    global number_label
    global Label_flag
    
    R1Value=R1.get()
    R2Value=R2.get()
    VCCValue=VCC.get()
    
    if (len(R1Value)==0 or len(R2Value)==0 or len(VCCValue)==0):
        print("Empty")
        Empty_flag=True
        Warning_label = Label(text="Please enter all the Values:",fg="RED",font=('Helvetica',11))
        Warning_label.place(x=60,y=100)
        Warning_flag=True
        
        
    elif(Empty_flag):
        Warning_label.destroy()
        Empty_flag=False
    else:    
        Empty_flag=False
        Warning_flag=False
        if(Warning_flag):
            Warning_label.destroy()
            
            
        
    if(Label_flag):
         label.destroy()
         Label_flag=False
         


def clear():
    global Label_flag
    global number_flag

    R1.delete(0,END)
    R2.delete(0,END)
    VCC.delete(0,END)
    if(Label_flag):
        label.destroy()
        Label_flag=False
    if(number_flag):  
        number_label.destroy()
        number_flag=False
    if(Warning_flag):
        Warning_label.destroy()
        
        
    
def save_info():
    global Label_flag
    global label
    global Empty_flag
    global Warning_label
    global Warning_flag
    global number_flag
  
    
    file = open("Values.txt","w")
    file.truncate(0)
    #file = open(r"F:\USERS\PRAKASH\PROJECTS\data"+timestr,"w")
    R1Value=R1.get()
    R2Value=R2.get()
    VCCValue=VCC.get()


        
    file.write(R1.get())
    file.write("\n")
    file.write(R2.get())
    file.write("\n")
    file.write(VCC.get())
    file.write("\n")
    file.close()
    validation()
    if(Warning_flag==False):
        valid_data()
    
    
    #valid_data()
    if((Empty_flag==False) and (number_flag==False) and (Warning_flag==False)):
        with open('Values.txt', 'r') as byte_reader:
            
            R1_value=float(byte_reader.readline()[0:7])
            print(R1_value)
            
            R2_value=float(byte_reader.readline()[0:7])
            print(R2_value)
            
            VCC_value=float(byte_reader.readline()[0:5])
            print(VCC_value)
            
            Vout=(VCC_value*R2_value)/(R1_value+R2_value)
            print(str(Vout)+ " Volts")
            if(Label_flag):
               label.destroy()
               
            if(Empty_flag==True):
                Warning_label.destroy()
            
            label = Label(app,text=" Vout is:"+ str(Vout)+" Volts",fg="GREEN", font=('Helvetica',15))
            label.place(x=50,y=400)
            Label_flag=True
           
            
           
    
    
    

app = Tk()

app.geometry("500x500")

app.title("APOLLO COMPUTING LABORATORIES")

#app.iconbitmap("acl.ico")

heading = Label(text="VOLTAGE DIVIDER NETWORK",font=('Helvetica',15,"bold"),fg="black",bg="cyan",width="500",height="0")
heading.pack()
timestr = time.strftime("%d.%m.%Y-%H.%M.%S")
"""
image = PhotoImage(file = "al.ico")
image_button = tk.Button(app,image=image)
image_button.place(x=0,y=0)
"""


global Label_flag
global label
global Empty_flag
global Warning_label
global number_flag
global Warning_flag

Warning_flag=False
number_flag=False
Label_flag=False
Empty_flag=False


R1 = Label(text="Enter R1 in Ohms only :",font=('Helvetica',11,"bold"))
R1.place(x=15,y=150)
R1 = Entry(textvariable=R1,width="10")
R1.place(x=200,y=150)


R2 = Label(text="Enter R2 in Ohms only :",font=('Helvetica',11,"bold"))
R2.place(x=15,y=210)
R2 = Entry(textvariable=R2,width="10")
R2.place(x=200,y=210)

VCC = Label(text="Enter VCC in Volts only :",font=('Helvetica',11,"bold"))
VCC.place(x=15,y=270)
VCC = Entry(textvariable=VCC,width="5")
VCC.place(x=200,y=270)

Note = Label(text="NOTE:",font=('Helvetica',12,"bold"))
Note.place(x=10,y=70)
Message = Label(text="Resistor values Limited to 1MEGA OHM Only :",fg="black",font=('Helvetica',12,"bold"))
Message.place(x=62,y=70)

button = Button(app,text="CALCULATE",font=('Helvetica',11,"bold"),command=save_info,width="30",height="2",bg="grey")
button.place(x=15,y=350)
clear = Button(app,text="CLEAR",font=('Helvetica',11,"bold"),command=clear,width="30",height="2",bg="grey")
clear.place(x=15,y=450)

mainloop()
