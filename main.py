from tkinter import *

def clickedB():
    myLabel["text"] = input.get()

window = Tk()
window.minsize(500, 300)
window.config(padx=100, pady=100)

myLabel = Label(text="I am a label", font=("Arial", 24, "bold"))
myLabel.grid(column=0, row=0)

myLabel["text"] = "New Text"
myLabel.config(text="This is some new text")

myButton = Button(text="Click", command = clickedB )
myButton.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()
