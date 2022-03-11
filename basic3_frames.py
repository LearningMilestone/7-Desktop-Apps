#Frames for complex window layouts
import tkinter
from tkinter import BOTH

#Define windwo
root=tkinter.Tk()
root.title('Frames')
root.iconbitmap('thinking.ico')
root.geometry('500x500')

#Example of why to use frames -- can't use more than one geometry manager at the same time
# name_label=tkinter.Label(root,text="Submit your name")
# name_label.pack()
# name_button=tkinter.Button(root,text='Submit your Name')
# name_button.grid(row=0,column=1)

#Define frames
pack_frame=tkinter.Frame(root,bg='red')
grid_frame1=tkinter.Frame(root,bg='blue')
grid_frame2=tkinter.LabelFrame(root,text="Layout Basics",borderwidth=5)


pack_frame.pack(fill=BOTH,expand=True)
grid_frame1.pack(fill='x')
grid_frame2.pack(fill=BOTH,expand=True,padx=10,pady=10)

#Pack Frame
tkinter.Label(pack_frame,text="text").pack()
tkinter.Label(pack_frame,text="text").pack()
tkinter.Label(pack_frame,text="text").pack()

#Grid frame 1 Layout
tkinter.Label(grid_frame1,text="text").grid(row=0,column=0)
tkinter.Label(grid_frame1,text="text").grid(row=1,column=1)
tkinter.Label(grid_frame1,text="text").grid(row=2,column=2)
#tkinter.Label(grid_frame1,text="texttexttexttexttexttexexttexttexttexttexttexttext").grid(row=3,column=0)

#Grid frame 2Layout
tkinter.Label(grid_frame2,text="texttexttexttexttexttexexttexttexttexttexttexttext").grid(row=3,column=0)

#mainloop
root.mainloop()