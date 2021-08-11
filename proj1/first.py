import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

window=tk.Tk()
window.title("My First Python Project")

name_label=ttk.Label(window,text="Name: ")
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(window,text="Email: ")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(window,text="Age: ")
age_label.grid(row=2,column=0,sticky=tk.W)


name_var=tk.StringVar()
name_entrybox=ttk.Entry(window,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)

name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(window,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(window,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(window,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

user_type=tk.StringVar()

radio_button1=ttk.Radiobutton(window,text="Student",value="Student",variable=user_type)
radio_button1.grid(row=4,column=0)

radio_button2=ttk.Radiobutton(window,text="Teacher",value="Teacher",variable=user_type)
radio_button2.grid(row=4,column=1)

chkbutton_var=tk.IntVar()
checkbutton=ttk.Checkbutton(window,text="Check if you want to subscribe to our newsletter",variable=chkbutton_var)
checkbutton.grid(row=5,columnspan=4)


# def action():
#     username=name_var.get()
#     email=email_var.get()
#     age=age_var.get()
#     gender=gender_var.get()
#     user_types=user_type.get()
#     if chkbutton_var.get():
#         subscribed="Yes"
#     else:
#         subscribed="No"
#     print(username,email,age,gender,user_types,subscribed)

#     with open("project.txt",'a') as f:
#         f.write(f"{username} {email} {age} {gender} {user_types} {subscribed} \n")

#     name_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)

#     name_label.configure(foreground="Blue")

def action():
    username=name_var.get()
    email=email_var.get()
    age=age_var.get()
    gender=gender_var.get()
    user_types=user_type.get()
    if chkbutton_var.get():
        subscribed="Yes"
    else:
        subscribed="No"

    with open("project.csv","a",newline="") as f:
        dict_writer=DictWriter(f,fieldnames=["Username","Email","age","Gender","User Type","Subcription Status"])
        if os.stat("project.csv").st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            "Username":username,
            "Email":email,
            "age":age,
            "Gender":gender,
            "User Type":user_types,
            "Subcription Status":subscribed
        })


    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    name_label.configure(foreground="Blue")

submit_button=ttk.Button(window,text="Submit",command=action)
submit_button.grid(row=6,column=0)




window.mainloop()




