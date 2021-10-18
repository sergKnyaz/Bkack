from tkinter import *

class Gui(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl=Label(self,text='enter Pasvord')
        self.inst_lbl.grid(row=0,column=0,columnspan=2,sticky=W)

        self.pw_lbl=Label(self,text='Passvord: ')
        self.pw_lbl.grid(row=1,column=0,sticky=W)

        self.pw_ent=Entry(self)
        self.pw_ent.grid(row=1,column=1,sticky=W)

        self.bttn=Button(self,text='ENTER',command=self.reveal)
        self.bttn.grid(row=2,column=0,sticky=W)

        self.txt=Text(self,width=35,height=5,wrap=WORD)
        self.txt.grid(row=3,column=0,columnspan=2,sticky=W)

    def reveal(self):
        conten=self.pw_ent.get()
        if conten=='12345':
            message='verno'
        else:
            message='neverno'

        self.txt.delete(0.0,END)
        self.txt.insert(0.0,message)

root=Tk()
root.title('fools')
root.geometry('300x150')
app=Gui(root)
root.mainloop()