import tkinter
# from tkinter import StringVar
from tkinter import ttk, END

root=tkinter.Tk()
root.title("Metric Helper")
root.iconbitmap('ruler.ico')
# root.geometry("350x150")

#Define Colors & Fonts
root_color='#cb7057'
button_color = "#f5cf87"
field_font = ('Cambria', 10)

#Configure Root
root.config(bg=root_color)


#Define Functions
def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
        'femto':10**-15,
        'pico':10**-12,
        'nano':10**-9,
        'micro':10**-6,
        'milli':10**-3,
        'centi':10**-2,
        'deci':10**-1,
        'base value':10**0,
        'deca':10**1,
        'hecto':10**2,
        'kilo':10**3,
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peta':10**15
        }

     #Clear the output field
    output_field.delete(0, END)

    #Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    #Covert to the base unit first
    base_value = start_value*metric_values[start_prefix]
    #Covert to new metric value
    end_value = base_value/metric_values[end_prefix]

    #Update ouput field with answer
    output_field.insert(0, str(end_value))


#Add widgets
input_field=tkinter.Entry(root, width =20,borderwidth=3,font=field_font)
tkinter.Label(root,text="=",bg=root_color,font=field_font).grid(row=0,column=1)
output_field=tkinter.Entry(root, width =20,borderwidth=3,font=field_font)

input_field.grid(row=0,column=0,padx=10,pady=10)
output_field.grid(row=0,column=2,padx=10,pady=10)

input_field.insert(0, 'Enter your quantity')

#Create dropdown for metric values
# Create the list of options
# metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
#                'basevalue', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
# Variable to keep track of the option selected in OptionMenu
# input_choice=StringVar()
# output_choice=StringVar()

# Set the default value of the variable
# input_choice.set('basevalue')
# output_choice.set('basevalue')

# Create the optionmenu widget and pass the options_list and input_choice,output_choice to it.
#using tkinter
# input_dropdown=tkinter.OptionMenu(root,input_choice,*metric_list)
# output_dropdown=tkinter.OptionMenu(root,output_choice,*metric_list)
#
# input_dropdown.grid(row=1,column=0)
# tkinter.Label(root,text="to",bg=root_color,font=field_font).grid(row=1,column=1)
# output_dropdown.grid(row=1,column=2)
#
#using ttk module for modernlooking ui
#create combobox for metric value
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
               'basevalue', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']

input_combobox=ttk.Combobox(root,value=metric_list,font=field_font,justify='center')
tkinter.Label(root,text="to",bg=root_color,font=field_font).grid(row=1,column=1)
output_combobox=ttk.Combobox(root,value=metric_list,font=field_font,justify='center')
input_combobox.grid(row=1,padx=10,pady=10)
output_combobox.grid(row=1,column=2,padx=10,pady=10)

input_combobox.set('basevalue')
output_combobox.set('basevalue')


#create button
convert_button=tkinter.Button(root,text="Convert",bg=button_color,command=convert)
convert_button.grid(row=3,column=0,columnspan=3,pady=20,ipadx=50)


#run mainloop
root.mainloop()