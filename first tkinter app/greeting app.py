import tkinter as tk
from tkinter import ttk

#define function
def greet():
    #or keyword returns the secod value if the first value is empty(string length is 0)
    print(f"hello {user_name.get() or 'World'}")

#define window
root=tk.Tk()

#add an entry widget

## create a variable - placeholder for the string coming from the linked entry field
user_name=tk.StringVar()

#create name label
name_label=ttk.Label(root,text='Name: ')
name_label.pack(side='left',padx=(0,10))

#create an entry
## text variable field links the entry field to a variable inside a program
name_entry=ttk.Entry(root,width=15,textvariable=user_name)
name_entry.pack(side="left")
#focus helps in typing right away the application is started
name_entry.focus()


#add button

greet_button=ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side='left')

quit_button=ttk.Button(root,text="quit",command=root.destroy)
quit_button.pack(side='right')

#run window
root.mainloop()
