import tkinter as tk
from tkinter import ttk

#define function
def greet():
    print("hello world")

#define window
root=tk.Tk()

#add component
#Note: pack by default let's component stick in the center of the top of parent window - horizontally and not vertically
# or the component created previously - by default side ="top"
#note fill option- helps the widget to take up reserved space - options->x,y,both
#expand option helps to get more reserved space
greet_button=ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side='left',fill='both',expand=True)

quit_button=ttk.Button(root,text="quit",command=root.destroy)
quit_button.pack(side='left')

#run window
root.mainloop()
