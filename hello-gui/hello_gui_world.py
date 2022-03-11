import tkinter
from tkinter import BOTH, StringVar

#create window
root=tkinter.Tk()
root.title('Hello GUI World')
root.iconbitmap('wave.ico')
root.geometry('350x400')
root.resizable(0,0)

#Define fonts & Colors
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
font_color="#ffffff"

#Add bg color to the window
root.config(bg=root_color)

#Define Functions

def print_greeting():
    '''Say hello to the user'''
    if case_style.get()=="normal":
      text_entry=name.get()
      text_label=tkinter.Label(output_frame,text=f"Hello {text_entry}",bg=output_color)
      text_label.pack()
    elif case_style.get()=="upper":
        text_entry=name.get()
        text_label=tkinter.Label(output_frame,text=f"HELLO {text_entry.upper()}",bg=output_color)
        text_label.pack()


#Add Frames
input_frame=tkinter.LabelFrame(root,bg=input_color)
output_frame=tkinter.LabelFrame(root,bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10,pady=(0,10),fill=BOTH,expand=True)


#Add  name and submit button widgets
name=tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button=tkinter.Button(input_frame,text="Submit",command=print_greeting)
name.grid(row=0,column=0,padx=10,pady=10)
submit_button.grid(row=0,column=1,padx=10,pady=10,ipadx=20)
name.insert(0, 'Enter your Name')

#Add radio button to choose letter case style
case_style=StringVar()
case_style.set("normal")

normal_case_button = tkinter.Radiobutton(input_frame, text="Normal Case",
                                    variable=case_style, value='normal', bg=input_color)

upper_case_button = tkinter.Radiobutton(input_frame, text="Upper Case",
                                        variable=case_style, value='upper', bg=input_color)

normal_case_button.grid(row=1,column=0,pady=10)
upper_case_button.grid(row=1,column=1)

#add an image
smile_image=tkinter.PhotoImage(file='smile.png')
smile_label=tkinter.Label(output_frame,image=smile_image,bg=output_color)
smile_label.pack()

#run mainloop
root.mainloop()

