from tkinter import *
from random import shuffle

class Gui():
    def __init__(self):
        self.cardIpg = []
        self.dataImage=[i for i in range(36)]
        self.lblImage = []
        self.game1=[]
        self.root=Tk()

        
    def table():
        pass

    def win(self):
        self.root.geometry('1000x1000')
        fon = PhotoImage(file='cards_36/table.png')
        fon=fon.zoom(2,2)
        Label(self.root, image=fon).place(x=-2, y=0)

        
        for jpg in range(36):
            self.cardIpg.append(PhotoImage(file='cards_36/cards_' + str(jpg) + '.png'))
            self.cardIpg[jpg]=self.cardIpg[jpg].zoom(3,3)
            self.cardIpg[jpg]=self.cardIpg[jpg].subsample(2,2)
        #shuffle(self.dataImage)
        self.gui()
        self.root.mainloop()

    def go(self,x):
        self.game1.append(self.dataImage[x])
        self.dataImage.pop(x)
        print(self.game1)
        for i in self.lblImage:
            i.destroy()
        self.gui()

    def  go2(self,x):
        maus_x=self.root.winfo_pointerx()-self.root.winfo_rootx()
        maus_y=self.root.winfo_pointery()-self.root.winfo_rooty()
        self.lblImage[x].place(x=maus_x,y=maus_y,anchor=CENTER)
        

    def gui(self):
        shuffle(self.cardIpg)
       
        n=0
        m=0
        self.lblImage=[]

        # self.dataImage.append()
        for i in range(len(self.dataImage)):
            self.lblImage.append(Label(self.root))
            if i<18:
                self.lblImage[i].place(x=10 + n, y=250)
                n+=50
            else:
                self.lblImage[i].place(x=10 + m, y=400)
                m+=50
            #self.lblImage[i].bind('<Button-1>', lambda e, x=i: self.go(x))
            self.lblImage[i].bind('<B1-Motion>', lambda e,x=i: self.go2(x))
            self.lblImage[i]['image'] = self.cardIpg[self.dataImage[i]]
        print(self.dataImage)

a=Gui()
a.win()