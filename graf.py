from tkinter import *

sdano = []


def go(x):
    global sdano, lblImage, dataImage
    n = 0
    dataImage.pop(x)

    sdano.append(x)
    sdanoIpg = []
    for i in range(len(sdano)):
        sdanoIpg.append(Label(root))
        sdanoIpg[i].place(x=10 + n, y=100)
        n += 8
        sdanoIpg[i]['image'] = cardImg[sdano[i]]
    m=0
    lblImage = []

    for j in range(len(dataImage)):

        lblImage.append(Label(root))
        lblImage[j].place(x=10 + m, y=250)
        m += 8
        lblImage[j].bind('<Button-1>', lambda e, x=j: go(x))
        lblImage[j]['image'] = cardImg[dataImage[j]]
        root.update()


def table():
    pass


root = Tk()
root.geometry('500x500')
fon = PhotoImage(file='cards_52/table.png')
Label(root, image=fon).place(x=-2, y=0)

cardImg = []
for jpg in range(1, 53):
    cardImg.append(PhotoImage(file='cards_52/cards_' + str(jpg) + '.png'))

lblImage = []
dataImage = [i for i in range(52)]


# dataImage.append()
# lblImage.append(Label(root))
# lblImage[i].place(x=10 + n, y=250)
# lblImage[i].bind('<Button-1>', lambda e, x=i: go(x))
# lblImage[i]['image'] = cardImg[dataImage[i]]
print(dataImage)

root.mainloop()
