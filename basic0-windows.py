#window basics
#In this example
import tkinter

#define window
root=tkinter.Tk()
root.title('Window Basics')
root.iconbitmap('thinking.ico')
root.geometry('400x300')
root.resizable(0,0)
root.config(bg="cyan")

#Second Window
top=tkinter.Toplevel()
top.config(bg='pink')
top.geometry("100x100+400+200")

#run mainloop
root.mainloop()