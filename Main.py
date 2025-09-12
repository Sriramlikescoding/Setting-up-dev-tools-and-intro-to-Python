
#import tkinter
#another way to import from import tkindar library
from datetime import date
from tkinter import *
window = Tk()
window.title("My first tkinter project")
window.geometry("600x600")
label = Label(text = 'Hello world', fg="white", bg= 'Black', height=1, width=300)
label.pack()
nameLabel = Label(text = "Full Name", bg= "red")
nameLabel.pack()
NameInput = Entry()
NameInput.pack()
def display():
    Name = NameInput.get()
    global Message
    Message = "Welcome To The Application \n Today's date is\n"
    greet = "Hello "+ Name + "\n"
    textBox.insert(END,greet)
    textBox.insert(END,Message)
    textBox.insert(END,date.today())
    
textBox = Text(height=4)
textBox.pack()
button = Button(text = "Begin", command=display, height=1,bg="yellow",fg="green")
button.pack()
window.mainloop()
