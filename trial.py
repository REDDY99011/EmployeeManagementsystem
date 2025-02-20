from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee1.db")

root = Tk()
root.title("Employee Management System")
root.geometry("1920x1200+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

# Entries Frame

entries_frame=Frame(root,bg="#534c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0, columnspan=2,padx=10,pady=20,sticky="w")

lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10)
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16))
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10)
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",16))
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lbldoj=Label(entries_frame,text="doj",font=("Calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10)
txtDOJ=Entry(entries_frame,textvariable=doj,font=("Calibri",16))
txtDOJ.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblemail=Label(entries_frame,text="email",font=("Calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10)
txtemail=Entry(entries_frame,textvariable=email,font=("Calibri",16))
txtemail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblGender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w") 
comboGender=ttk.Combobox(entries_frame,font=("Calibri",16),width=28,textvariable=gender,state="readonly")
comboGender['values'] = ("Male","Female")
comboGender.grid(row=3, column=1, padx=10,pady=10,sticky="w")  

lblContact=Label(entries_frame,text="Contact",font=("Calibri",16),bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10)
txtContact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

lblAddress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtAddress=Text(entries_frame,width=85,height=4,font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=10,padx=10,sticky="w")

def getData(event):
    selected_row = tv.focus()
    data =tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    #email.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END, row[7])
    
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()==""or txtAge.get()=="" or txtDOJ.get()=="" or txtemail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(
        1.0,END)=="":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return 
    
    db.insert(txtName.get(),txtAge.get(),txtDOJ.get(), txtemail.get(), comboGender.get(), txtContact.get(), txtAddress.get(
        1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()
    
    
def update_employee():
    if txtName.get()=="" or txtAge.get() == "" or txtDOJ.get() == "" or txtemail.get() == "" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(
        1.0,END)=="":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return 
    
    db.update(row[0],txtName.get(),txtAge.get(),txtDOJ.get(), txtemail.get(), comboGender.get(), txtContact.get(),
    txtAddress.get(
        1.0,END))
    messagebox.showinfo("Success","Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)


btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("calibri", 16 ,"bold"),fg="white",
              bg="#16a085",bd=0).grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("calibri", 16 ,"bold"),fg="white",
              bg="#2980b9",bd=0).grid(row=0,column=1,padx="10")

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("calibri", 16 ,"bold"),fg="white",
              bg="#c0392b",bd=0).grid(row=0,column=2,padx="10")

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",width=15,font=("calibri", 16 ,"bold"),fg="white",
              bg="#f39c12",bd=0).grid(row=0,column=3,padx="10")


# Table Frame

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=450, width=1450, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri', 18),
                rowheight=50) # Modify the font of the body 
style.configure("mystyle.Treeview.Heading", font=('Calibri',18))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1", text="ID")
#tv.column("1",width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
#tv.column("1",width=10)
tv.heading("4", text="D.O.B")
#tv.column("1",width=5)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
#tv.column("1",width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X) 

displayAll()
root.mainloop()