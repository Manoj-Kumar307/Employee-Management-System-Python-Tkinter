from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.geometry('930x478')
root.resizable(0,0)
root.title("Empolyee login page")
img = Image.open(r"C:\Users\MANOJ KUMAR\Desktop\manoj.png")
img = img.resize((932, 478))

photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo)
label.pack()
# ---------------- Employee Details ----------------

# Name
Label(root, text="Employee Name",
      font=("Arial", 12, "bold"),
      bg="white").place(x=80, y=10)

name_entry = Entry(root, font=("Arial", 12), width=25)
name_entry.place(x=80, y=40)

# Employee ID
Label(root, text="Employee ID",
      font=("Arial", 12, "bold"),
      bg="white").place(x=80, y=90)

id_entry = Entry(root, font=("Arial", 12), width=25)
id_entry.place(x=80, y=120)

# Age
Label(root, text="Age",
      font=("Arial", 12, "bold"),
      bg="white").place(x=80, y=150)

age_entry = Entry(root, font=("Arial", 12), width=25)
age_entry.place(x=80, y=180)

# Salary
Label(root, text="Salary",
      font=("Arial", 12, "bold"),
      bg="white").place(x=80, y=210)

salary_entry = Entry(root, font=("Arial", 12), width=25)
salary_entry.place(x=80, y=240)

# Department
Label(root, text="Department",
      font=("Arial", 12, "bold"),
      bg="white").place(x=80, y=280)

department_entry = Entry(root, font=("Arial", 12), width=25)
department_entry.place(x=80, y=310)


# ---------------- Add Employee Function ----------------

def add_employee():

    name = name_entry.get()
    employee_id = id_entry.get()
    age = age_entry.get()
    salary = salary_entry.get()
    department = department_entry.get()

    print("Employee Added")
    print("----------------------")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Age:", age)
    print("Salary:", salary)
    print("Department:", department)

    # Clear the fields
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    age_entry.delete(0, END)
    salary_entry.delete(0, END)
    department_entry.delete(0, END)


# Add Employee Button
Button(root,
       text="Add Employee",
       font=("Arial", 12, "bold"),
       bg="green",
       fg="white",
       command=add_employee).place(x=650, y=415)


Label(root,text="User name").pack()
username = Entry(root)
username.pack()


root.mainloop()