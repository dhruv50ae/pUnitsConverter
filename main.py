from tkinter import *

window = Tk()
window.minsize(500, 300)

myLabel = Label(text="I am a label", font=("Arial", 24, "bold"))
myLabel.pack()

myLabel["text"] = "New Text"
myLabel.config(text="This is some new text")

def clickedB():
    myLabel["text"] = input.get()

myButton = Button(text="Click", command = clickedB )
myButton.pack()

input = Entry(width=10)
input.pack()

window.mainloop()
