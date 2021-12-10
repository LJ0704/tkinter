from tkinter import *

root = Tk() #creating label widget
e = Entry(root, width=50, bg="purple", fg="white", borderwidth='5')
e.pack()
def myClick():
    myLabel = Label(root, text="Hello "+e.get())
    myLabel.pack()
#showing it in screen 
myButton = Button(root, text="Enter you name",command=myClick,fg="blue", bg="yellow")
myButton.pack()

root.mainloop()
