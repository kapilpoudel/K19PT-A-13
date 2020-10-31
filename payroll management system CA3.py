# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:34:33 2020

@author: kapil
"""
from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("1350x700")
root.configure(background="darkcyan")
root.title("Employee Payroll Management System | Developed by Shailendra Pradhan")

#DECLARING VARIABLE 
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()
t14 = StringVar()  



#FUNCTIONS 
def Validate():
    if t1.get() == "":
        messagebox.showinfo('INFORMATION','Please enter EmployeeID')
    elif t2.get() == "":
        messagebox.showinfo('INFORMATION','Please enter First Name')
    elif t3.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Last Name')
    elif t4.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Email')
    elif len(t5.get()) != 10:
        messagebox.showinfo('INFORMATION','Please enter 10 digit Contact No')
    elif t6.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Age') 
    elif t7.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Gender')
    elif t8.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Designation')
    elif t9.get() == "":
        messagebox.showinfo('INFORMATION','Please enter DOB') 
    elif t11.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Month')
    elif t12.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Year')
    elif t13.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Salary')
    elif t14.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Deduction')
    else:
         messagebox.showinfo('INFORMATION','Submitted Successfully')
      
def ClearAll():
    
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END) 
    t4.delete(0,END)
    t5.delete(0,END)
    t6.delete(0,END)
    t7.delete(0,END)
    t8.delete(0,END)
    t9.delete(0,END)
    t10.delete(0.0,END)
    t11.delete(0,END)
    t12.delete(0,END)
    t13.delete(0,END)
    t14.delete(0,END)
    
def Display():
    
    if t1.get() == "":
        messagebox.showinfo('INFORMATION','Please enter EmployeeID')
    elif t2.get() == "":
        messagebox.showinfo('INFORMATION','Please enter First Name')
    elif t3.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Last Name')
    elif t4.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Email')
    elif len(t5.get()) != 10:
        messagebox.showinfo('INFORMATION','Please enter 10 digit Contact No')
    elif t6.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Age') 
    elif t7.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Gender')
    elif t8.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Designation')
    elif t9.get() == "":
        messagebox.showinfo('INFORMATION','Please enter DOB') 
    elif t11.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Month')
    elif t12.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Year')
    elif t13.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Salary')
    elif t14.get() == "":
        messagebox.showinfo('INFORMATION','Please enter Deduction')
    else:
        v1=t1.get()
        v2=t2.get()
        v3=t3.get()
        v4=t4.get()
        v5=t5.get()
        v8=t8.get()
        v11=t11.get()
        v12=t12.get()
        v13=int(t13.get())
        v14=int(t14.get())
        
        d1=Label(frame3,text="Employee ID: "+v1,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d1.place(x=200,y=50)
        d2=Label(frame3,text="Employee Designation: "+v8,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d2.place(x=200,y=80)
        d3=Label(frame3,text="Employee Name: "+v2+" "+v3,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d3.place(x=200,y=110)
        d4=Label(frame3,text="MM/YYYY: "+v11+"/"+v12,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d4.place(x=200,y=140)
        d5=Label(frame3,text="Employee Contact No: "+v5,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d5.place(x=200,y=170)
        d6=Label(frame3,text="Employee email: "+v4,font=("times new roman",12,"italic bold"),bg="lightsalmon")
        d6.place(x=200,y=200)
    
        net_payable=str(v13-v14)
    
        d7=Label(frame3,text="Net Payable Salary: "+net_payable,font=("times new roman",12,"italic bold"),bg="salmon")
        d7.place(x=200,y=260)
            
    
    
    
        
def Validate_contact(t5):
    if t5.isdigit():
        return True
    elif t5 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Contact No should be DIGITS')
        return False
def Validate_age(t6):
    if t6.isdigit():
        return True
    elif t6 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Age should be DIGITS')
        return False
    
def Validate_month(t11):
    if t11.isdigit():
        return True
    elif t11 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Month should be DIGITS')
        return False
    
def Validate_year(t12):
    if t12.isdigit():
        return True
    elif t12 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Year should be DIGITS')
        return False

def Validate_salary(t13):
    if t13.isdigit():
        return True
    elif t13 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Salary should be DIGITS')
        return False
   
def Validate_deduction(t14):
    if t14.isdigit():
        return True
    elif t14 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','Deduction should be DIGITS')
        return False
   
def Validate_employee(t1):
    if t1.isdigit():
        return True
    elif t1 == "":
        return True
    else:
        messagebox.showinfo('INFORMATION','EmployeeID should be DIGITS')
        return False
    




#FRAME0
frame0=Frame(root,bd=2,relief="ridge",bg="palegreen")
frame0.place(x=50,y=5,width=1260,height=45)
title0=Label(root,text="Employee Payroll Management System",font=("times new roman",25,"bold underline"),bg="palegreen")
title0.place(x=450,y=8)

#FRAME1
frame1=Frame(root,bd=2,relief="ridge")
frame1.place(x=50,y=50,width=650,height=620)
#TITLE1
title1=Label(frame1,text="Employee Details",font=("times new roman",18,"bold underline"))
title1.place(x=230,y=0)

#LINE1
lb1=Label(frame1,text="Employee ID",font=("times new roman",12,"bold"))
lb1.place(x=220,y=80)
t1=Entry(frame1,width=20,bg="lightgreen",textvariable=t1)
t1.place(x=360,y=85)
employee = root.register(Validate_employee)
t1.config(validate="key", validatecommand=(employee, '%P'))

#LINE2
lb2=Label(frame1,text="First Name",font=("times new roman",12,"bold"))
lb2.place(x=20,y=140)
t2=Entry(frame1,width=30,bg="lightgreen",textvariable=t2)
t2.place(x=140,y=145)

lb3=Label(frame1,text="Last Name",font=("times new roman",12,"bold"))
lb3.place(x=360,y=140)
t3=Entry(frame1,width=20,bg="lightgreen",textvariable=t3)
t3.place(x=500,y=145)

#LINE3
lb4=Label(frame1,text="Email",font=("times new roman",12,"bold"))
lb4.place(x=20,y=200)
t4=Entry(frame1,width=30,bg="lightgreen",textvariable=t4)
t4.place(x=140,y=205)

lb5=Label(frame1,text="Contact No",font=("times new roman",12,"bold"))
lb5.place(x=360,y=200)
t5=Entry(frame1,width=20,bg="lightgreen",textvariable=t5)
t5.place(x=500,y=205)
contact_no = root.register(Validate_contact)
t5.config(validate="key", validatecommand=(contact_no, '%P'))

#LINE4
lb6=Label(frame1,text="Age",font=("times new roman",12,"bold"))
lb6.place(x=20,y=260)
t6=Entry(frame1,width=30,bg="lightgreen",textvariable=t6)
t6.place(x=140,y=265)
age = root.register(Validate_age)
t6.config(validate="key", validatecommand=(age, '%P'))

lb7=Label(frame1,text="Gender",font=("times new roman",12,"bold"))
lb7.place(x=360,y=260)
t7=Entry(frame1,width=20,bg="lightgreen",textvariable=t7)
t7.place(x=500,y=265)

#LINE5
lb8=Label(frame1,text="Designation",font=("times new roman",12,"bold"))
lb8.place(x=20,y=340)
t8=Entry(frame1,width=30,bg="lightgreen",textvariable=t8)
t8.place(x=140,y=345)

lb9=Label(frame1,text="DOB",font=("times new roman",12,"bold"))
lb9.place(x=360,y=340)
t9=Entry(frame1,width=20,bg="lightgreen",textvariable=t9)
t9.place(x=500,y=345)

#LINE6
lb10=Label(frame1,text="Address",font=("times new roman",12,"bold"))
lb10.place(x=20,y=420)
t10=Text(frame1,height=7,width=50,bg="lightgreen")
t10.place(x=140,y=420)


#FRAME2
frame2=Frame(root,bd=2,relief="ridge")
frame2.place(x=700,y=50,width=610,height=320)
title2=Label(frame2,text="Employee Salary Details",font=("times new roman",18,"bold underline"))
title2.place(x=150,y=0)

#LINE1
lb11=Label(frame2,text="Month",font=("times new roman",12,"bold"))
lb11.place(x=20,y=140)
t11=Entry(frame2,width=20,bg="lightgreen",textvariable=t11)
t11.place(x=100,y=145)
month = root.register(Validate_month)
t11.config(validate="key", validatecommand=(month, '%P'))

lb12=Label(frame2,text="Year",font=("times new roman",12,"bold"))
lb12.place(x=300,y=140)
t12=Entry(frame2,width=20,bg="lightgreen",textvariable=t12)
t12.place(x=440,y=145)
year = root.register(Validate_year)
t12.config(validate="key", validatecommand=(year, '%P'))


#LINE2
lb13=Label(frame2,text="Salary",font=("times new roman",12,"bold"))
lb13.place(x=20,y=200)
t13=Entry(frame2,width=20,bg="lightgreen",textvariable=t13)
t13.place(x=100,y=205)
salary = root.register(Validate_salary)
t13.config(validate="key", validatecommand=(salary, '%P'))

lb14=Label(frame2,text="Deduction",font=("times new roman",12,"bold"))
lb14.place(x=300,y=200)
t14=Entry(frame2,width=20,bg="lightgreen",textvariable=t14)
t14.place(x=440,y=205)
deduction = root.register(Validate_deduction)
t14.config(validate="key", validatecommand=(deduction, '%P'))

#LINE3
submit=Button(frame2,text="SUBMIT", bg="lime",command = Validate)
submit.place(x=100,y=260)
clear=Button(frame2,text="CLEAR", bg="lime",command = ClearAll)
clear.place(x=300,y=260)
print0=Button(frame2,text="DISPLAY RECIEPT", bg="lime",command = Display)
print0.place(x=450,y=260)



#FRAME3
frame3=Frame(root,bd=2,relief="ridge")
frame3.place(x=700,y=370,width=610,height=300)
title3=Label(frame3,text="Salary Reciept",font=("times new roman",18,"bold underline"))
title3.place(x=200,y=0)

root.mainloop()