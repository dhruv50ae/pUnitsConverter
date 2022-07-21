from tkinter import *

window = Tk()
window.minsize(200, 200)

window.title("Miles to kilometer converter")

kilometers = 0

def converter():
    oldNum = int(milesInput.get())
    newNum = oldNum * 1.60934
    kMLabel["text"] = f"{newNum} kilometers"

milesInput = Entry(width=10)
milesInput.grid(row=0, column=1)

milesLabel = Label(text="Miles to")
milesLabel.grid(row=0, column=2)

kMLabel = Label(text="0 Kilometers")
kMLabel.grid(row=1, column=1)

button = Button(text="Convert", command=converter)
button.grid(row=1, column=2)



window.mainloop()