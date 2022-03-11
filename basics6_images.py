#Images
import tkinter
from PIL import ImageTk,Image

root=tkinter.Tk()
root.title('Images')
root.iconbitmap('thinking.ico')
root.geometry("700x700")

#Define functions

def make_image():
    '''Display jpg image on GUI using pillow'''
    #keep a reference to variable using global
    global cat_image
    cat_image=ImageTk.PhotoImage(Image.open('cat.jpg'))
    cat_label=tkinter.Label(root,image=cat_image)
    cat_label.pack()

#Basics- works for png - does not work for jpeg
#adding images is a multistep process
#first create image
my_image=tkinter.PhotoImage(file='shield.png')
#this wont work
#my_image.pack()

#second-put image created on a label
my_label=tkinter.Label(root, image=my_image)

#pack the label
my_label.pack()

#you can put image on a button too
my_button=tkinter.Button(root,image=my_image)
my_button.pack()

#steps for jpg image
#this wont work
#cat_image=tkinter.PhotoImage(file='cat.jpg')
#cat_label=tkinter.Label(root,cat_image)
#cat_label.pack()

#Using PIL for jpg will help with jpg image display
# cat_image=ImageTk.PhotoImage(Image.open('cat.jpg'))
# cat_label=tkinter.Label(root,image=cat_image)
# cat_label.pack()
#defining above into a function
make_image()


#mainloop
root.mainloop()