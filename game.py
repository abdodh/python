from tkinter import *
#from tkinter import ttk
from random import *
def linux():
    root = Tk()
    root.geometry('300x300')
    root.title('dehini abdo')
    def main():
        print(dd1.set(randrange(10)))
    def uu1():
        print(dd2.set(randrange(10)))
    def uu2():
        print(dd3.set(randrange(10)))
    def uu3():
        print(dd4.set(randrange(10)))
    def uu4():
        print(dd5.set(randrange(10)))
    def uu5():
        print(dd6.set(randrange(10)))
    def uu6():
        print(dd7.set(randrange(10)))
    def uu7():
        print(dd8.set(randrange(10)))
    def uu8():
        print(dd9.set(randrange(10)))
    def koko():
        print(dd1.set(""))
        print(dd2.set(""))
        print(dd3.set(""))
        print(dd4.set(""))
        print(dd5.set(""))
        print(dd6.set(""))
        print(dd7.set(""))
        print(dd8.set(""))
        print(dd9.set(""))


    dd1 = StringVar()
    dd2 = StringVar()
    dd3 = StringVar()
    dd4 = StringVar()
    dd5 = StringVar()
    dd6 = StringVar()
    dd7 = StringVar()
    dd8 = StringVar()
    dd9 = StringVar()
    ##########################"
    dd77 = StringVar()
    #########################
    oop = Button(root,text='',textvariable=dd1,command=main)
    oop.place(x=0, y=0, width=80, height=80)
    lolo = Button(root,text='',textvariable=dd2,command=uu1)
    lolo.place(x=0, y=80, width=80, height=80)
    mp = Button(root,text='',textvariable=dd3,command=uu2)
    mp.place(x=0, y=160, width=80, height=80)
    ##################################"
    op = Button(root,text='',textvariable=dd4,command=uu3)
    op.place(x=80, y=0, width=80, height=80)
    llo = Button(root,text='',textvariable=dd5,command=uu4)
    llo.place(x=80, y=80, width=80, height=80)
    p = Button(root,text='',textvariable=dd6,command=uu5)
    p.place(x=80, y=160, width=80, height=80)
    ################################"
    oo = Button(root,text='',textvariable=dd7,command=uu6)
    oo.place(x=160, y=0, width=80, height=80)
    lol = Button(root,text='',textvariable=dd8,command=uu7)
    lol.place(x=160, y=80, width=80, height=80)
    mps = Button(root,text='',textvariable=dd9,command=uu8)
    mps.place(x=160, y=160, width=80, height=80)
    ########################################"
    mpsss = Label(root, text='clear ====>')
    mpsss.place(x=50, y=245)

    mpss = Button(root,text='clear',textvariable=dd77,command=koko)
    mpss.place(x=180, y=245, width=50, height=20)

linux()
mainloop()






































