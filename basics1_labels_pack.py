#2-Example-Labels and Pack
#Add labels and pack on the basic window created
import tkinter
from tkinter import BOTH

#Define window
root=tkinter.Tk()
root.title('Label Basics')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='pink')

#create widget
name_label_1=tkinter.Label(root,text='Hello, my name is Joey')
name_label_1.pack()

name_label_2=tkinter.Label(root,text='Hello, my name is Linda',font=('Arial',22,'bold'))
name_label_2.pack()

name_label_3=tkinter.Label(root,text="Hello, my name is Anu")
name_label_3.config(font=('Cambria',10))
name_label_3.config(bg='#ff0000')

name_label_3.pack(padx=10,pady=50)

#padding, internal padding, one -sided padding,anchor
name_label_4=tkinter.Label(root,text='Hello, my name is Paul',font=('Arial',15,'bold'),bg='green')
name_label_4.pack(pady=(0,10),ipadx=50,ipady=10,anchor='w')

#fill, expand-True,
name_label_5=tkinter.Label(root,text='Hello, my name is John',font=('Arial',12,'bold'),bg='#123456',fg='#FFFFFF')
name_label_5.pack(fill=BOTH,expand=True)
#main loop
root.mainloop()