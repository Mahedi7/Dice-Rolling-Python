from tkinter import *
import random

root=Tk()
root.title("Roll Dice")
root.geometry("300x300")

label = Label(root, font=('helvetica', 200, 'bold'),bg='yellow', fg='black', text='')

def rolldice():
    dice=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
button = Button(root, font=('helvetica', 10, 'bold'), text='Roll Dice', bg= 'green', command=rolldice)
button.pack()

root.mainloop()
