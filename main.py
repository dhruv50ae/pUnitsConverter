import tkinter

window = tkinter.Tk()
window.title("Something")
window.minsize(500,300)

FONT = ("Arial", 24, "bold")

myLabel = tkinter.Label(text =  "I am a label", font=FONT)
myLabel.pack()

window.mainloop()