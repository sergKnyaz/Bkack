from tkinter import *

root=Tk()
root.geometry('500x500')

cardImg=[]
for img in range(4):
    cardImg.append(PhotoImage(file='cards_52\cards_1.jpg'))

root.mainloop