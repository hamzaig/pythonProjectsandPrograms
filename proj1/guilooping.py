import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Looping")

labels=["Name","Age","Gender"]

for i in range(len(labels)):
    # current_label="Label"+str(i)
    current_label=ttk.Label(window,text=labels[i])
    current_label.grid(row=i,column=0,sticky=tk.W)

name_var=tk.StringVar()

user_info={
    'name':tk.StringVar(),
    "age":tk.StringVar(),
    "gender":tk.StringVar()
}

counter=0
for i in user_info:
    current_entrybox=ttk.Entry(window,width=15,textvariable=user_info[i])
    current_entrybox.grid(row=counter,column=1)
    counter+=1


def submit():
    for i,j in user_info.items():
        print(user_info[i].get())

submit_button=ttk.Button(window,text="Submit",command=submit)
submit_button.grid(row=(len(labels)+1),column=1)




window.mainloop()