import tkinter 
from tkinter import Button, Label, Tk

frame = Tk()

frame.geometry("300x300+100+100")
myText = Label(frame, text='Hello World')
def display_hello(): 
    myText.pack()
def remove_hello():
    myText.pack_forget()

hello_button = Button(frame, text="hello Button", command = display_hello)
hello_button.pack()
forget_button = Button(frame, text="Remove Button", command = remove_hello)
forget_button.pack()

print("Hello world")
frame.mainloop()