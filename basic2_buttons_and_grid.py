#Buttons and grid
import tkinter

#Define window
root=tkinter.Tk()
root.title('Button Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)

#define layout
name_button=tkinter.Button(root,text='Say Hello')
name_button.grid(row=0,column=0)
# name_button.grid(row=2,column=2)

time_button=tkinter.Button(root,text="Tell Time",bg="#00FFFF")
time_button.grid(row=0,column=1)

place_button=tkinter.Button(root,text="Tell location",bg="#FF00FF",activebackground="#0F0F0F",activeforeground="white")
place_button.grid(row=0,column=2,padx=10,pady=10,ipadx=15)

day_button=tkinter.Button(root,text="Tell Day",bg="black",fg="white",borderwidth=5)
day_button.grid(row=1,column=0,columnspan=3)
#using sticky to compass button-similar to anchor
# day_button.grid(row=1,column=0,columnspan=3,sticky="w")
# day_button.grid(row=1,column=0,columnspan=3,sticky="e")
#to expand it across the whole space available- in this case 3 columns
day_button.grid(row=1,column=0,columnspan=3,sticky="we")

#grouping buttons
test_button_1=tkinter.Button(root,text='test')
test_button_2=tkinter.Button(root,text='test')
test_button_3=tkinter.Button(root,text='test')
test_button_4=tkinter.Button(root,text='test')
test_button_5=tkinter.Button(root,text='test')
test_button_6=tkinter.Button(root,text='test')

#this generates odd spacing as third button is in center of column 3 which is big because of third button--temporary fix is sticky

test_button_1.grid(row=2,column=0,padx=5,pady=5)
test_button_2.grid(row=2,column=1,padx=5,pady=5)
# test_button_3.grid(row=2,column=2,padx=5,pady=5)
test_button_3.grid(row=2,column=2,padx=5,pady=5,sticky='w')
test_button_4.grid(row=3,column=0,padx=5,pady=5)
test_button_5.grid(row=3,column=1,padx=5,pady=5)
# test_button_6.grid(row=3,column=2,padx=5,pady=5)
test_button_6.grid(row=3,column=2,padx=5,pady=5,sticky='w')








#main loop
root.mainloop()