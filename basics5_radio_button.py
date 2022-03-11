#Radio button
import tkinter
from tkinter import IntVar

root=tkinter.Tk()
root.title('Radio Button')
root.iconbitmap('thinking.ico')
root.geometry("350x350")
root.resizable(0,0)

#Define functions
def make_label():
    '''Print to the screen'''
    if number.get()==1:
        num_label=tkinter.Label(output_frame,text=1)
    elif number.get()==2:
        num_label=tkinter.Label(output_frame,text=2)
    num_label.pack()
#Define Frames

input_frame=tkinter.LabelFrame(root,text="Your terrritory",width=350,height=50)
output_frame=tkinter.Frame(root,width=350,height=300)
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10))

#Add widgets
#Define Radiobuttons
#define a variable to store value of radiobutton
number=IntVar()
#set initial value
number.set(1)
radio_1=tkinter.Radiobutton(input_frame,text="Print the number one",variable=number,value=1)
radio_2=tkinter.Radiobutton(input_frame,text="Print the number two",variable=number,value=2)
print_button=tkinter.Button(input_frame,text="Print the number",command=make_label)


radio_1.grid(row=0,column=0,padx=10,pady=10)
radio_2.grid(row=0,column=1,padx=10,pady=10)
print_button.grid(row=1,column=0,columnspan=2,padx=10,pady=(0,10))

#run mainloop
root.mainloop()

