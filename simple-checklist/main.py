import tkinter
from tkinter import END,ANCHOR

#root window
root=tkinter.Tk()
root.title("My Checklist")
root.geometry("400x400")


#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = '#6c1cbc'
button_color = '#e2cff4'
root.config(bg=root_color)

#define functions
def add_item():
    '''add an item to the listbox'''
    list_box.insert(END,list_entry.get())
    list_entry.delete(0,END)

def remove_item():
    '''Remove the selected(ANCHOR) item from the list box'''
    list_box.delete(ANCHOR)

def clear_list():
    '''Remove the all items from the list box'''
    list_box.delete(0,END)

def save_list():
    '''Save all items from the list box in a text file'''
    with open('checklist.txt','w') as f:
        #listbox.get() returns a tuple
        list_tuple=list_box.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+"\n")


def open_list():
    '''Open the list upon starting a program if there is a one'''
    try:
        with open('checklist.txt','r') as f:
            for line in f:
                list_box.insert(END,line)
    except:
        return
#define layout
#create frames
input_frame=tkinter.Frame(root,bg=root_color)
output_frame=tkinter.Frame(root,bg=root_color)
button_frame=tkinter.Frame(root,bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#input frame layout
list_entry=tkinter.Entry(input_frame,width=35,borderwidth=3,font=my_font)
list_addbutton=tkinter.Button(input_frame,text="Add Item",borderwidth=2,font=my_font,bg=button_color,command=add_item)
list_entry.grid(row=0,column=0,padx=5,pady=5)
list_addbutton.grid(row=0,column=1,padx=5, pady=5,ipadx=10)

#output frame layout
my_scrollbar=tkinter.Scrollbar(output_frame)
list_box=tkinter.Listbox(output_frame,width=45,height=15,borderwidth=3,font=my_font,yscrollcommand=my_scrollbar.set)
#link scrollbar to listbox
my_scrollbar.config(command=list_box.yview)

#place on layout
list_box.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1,sticky="NS")

#button frame layout
list_removebutton=tkinter.Button(button_frame,text="Remove Item",borderwidth=2,font=my_font,bg=button_color,command=remove_item)
list_clearbutton=tkinter.Button(button_frame,text="Clear",borderwidth=2,font=my_font,bg=button_color,command=clear_list)
list_savebutton=tkinter.Button(button_frame,text="Save List",borderwidth=2,font=my_font,bg=button_color,command=save_list)
list_quitbutton=tkinter.Button(button_frame,text="Quit",borderwidth=2,font=my_font,bg=button_color,command=root.destroy)

list_removebutton.grid(row=0,column=0,padx=2, pady=10)
list_clearbutton.grid(row=0,column=1,padx=2, pady=10)
list_savebutton.grid(row=0,column=2,padx=2, pady=10)
list_quitbutton.grid(row=0,column=3,padx=2, pady=10)
#open the previous list if available
open_list()
#mainloop
root.mainloop()