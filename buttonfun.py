from tkinter import *

root = Tk() #creating label widget

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()
#showing it in screen 
myButton = Button(root, text="Hello World!",command=myClick,fg="blue", bg="yellow")

myButton.pack()
root.mainloop()
