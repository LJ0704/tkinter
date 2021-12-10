from tkinter import *
#on/off buttons
root=Tk()
root.title('Internal Lights')
root.iconbitmap('G:\My Drive\HAL internship\GUI.ico')
root.geometry("500x300")

# creating label
my_label = Label(root,text="The Switch is on")
my_label.pack(pady=20)

#Define Our images
on = PhotoImage(file="GUI\on.png")
off= PhotoImage(file="GUI\off.png")

#creating a button
on_button = Button(root,image=on)
on_button.pack(pady=50)
root.mainloop()

