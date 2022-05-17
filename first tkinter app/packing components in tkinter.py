import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("600x400")

#create labels
rectangle_1=tk.Label(root,text="Rectangle_1",bg="green",fg="white")
rectangle_1.pack(ipadx=10,ipady=10,fill='x')

rectangle_2=tk.Label(root,text="Rectangle_2",bg="red",fg="white")
rectangle_2.pack(ipadx=10,ipady=10)

root.mainloop()

