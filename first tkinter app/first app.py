import tkinter as tk
from tkinter import ttk

#create a window
root=tk.Tk()

#create label
#pack puts widgets on window
ttk.Label(root,text="Hello World",padding=(30,10)).pack()

#run your window
root.mainloop()

