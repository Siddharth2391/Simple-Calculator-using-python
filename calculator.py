from tkinter import *
import tkinter.messagebox as msg
import math

def click(event):
    a=event.widget.cget("text")
    
    if a=='=':
        if strvr.get().isdigit():
            value=int(strvr.get())
        else:
            value=eval(userin.get())
        strvr.set(value)
        userin.update()
    elif a=='sqr':
        a=strvr.get()
        cube=int(a)*int(a)
        strvr.set(cube)
        userin.update()
    elif a=='CE':
        v=strvr.set('') 
        userin.update()
    elif a=='cube':
        a=strvr.get()
        cube=int(a)*int(a)*int(a)
        strvr.set(cube)
        userin.update()
    elif a=='sqrt':
        a=strvr.get()
        cube=math.sqrt(float(a))
        strvr.set(cube)
        userin.update()
    else:
        strvr.set(strvr.get() + a)
        userin.update()
    
def showinfo():
    a=msg.showinfo('About us','This app develop by Siddharth Dyamgond\ncopyright@2022')

def basic():
    app.geometry('330x498')
    app.resizable(0,0)
    app.title('Calculator')
    icon=PhotoImage(file='res/cal.png')
    app.iconphoto(False,icon)
    footer=Label(text='Calculator created by Siddharth Dyamgond',font='lucida 8 bold',fg='tomato',bg='black',pady=6).pack(side=BOTTOM,fill=X)
    mymenu=Menu(app)
    mymenu.add_command(label='About',command=showinfo)
    mymenu.add_command(label='Quit',command=quit)
    app.config(menu=mymenu)

def struc():
    f=Frame(app)
    myfont='Times 15 bold'
    global userin
    userin=Entry(f,textvar=strvr,font='Times 22',relief=FLAT)
    userin.grid(row=0,columnspan=4,ipadx=20)
    #1
    bt=Button(f,text='+',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=1,column=0)
    bt.bind('<Button>',click)
    bt=Button(f,text='-',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=1,column=1)
    bt.bind('<Button>',click)
    bt=Button(f,text='/',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=1,column=2)
    bt.bind('<Button>',click)
    bt=Button(f,text='*',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=1,column=3)
    bt.bind('<Button>',click)
    #2
    bt=Button(f,text='7',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=2,column=0)
    bt.bind('<Button>',click)
    bt=Button(f,text='8',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=2,column=1)
    bt.bind('<Button>',click)
    bt=Button(f,text='9',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=2,column=2)
    bt.bind('<Button>',click)
    bt=Button(f,text='%',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.bind('<Button>',click)
    bt.grid(row=2,column=3)
    #3
    bt=Button(f,text='6',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=3,column=0)
    bt.bind('<Button>',click)
    bt=Button(f,text='5',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=3,column=1)
    bt.bind('<Button>',click)
    bt=Button(f,text='4',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=3,column=2)
    bt.bind('<Button>',click)
    bt=Button(f,text='sqr',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=3,column=3)
    bt.bind('<Button>',click)
    #4
    bt=Button(f,text='1',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=4,column=0)
    bt.bind('<Button>',click)
    bt=Button(f,text='2',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=4,column=1)
    bt.bind('<Button>',click)
    bt=Button(f,text='3',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=4,column=2)
    bt.bind('<Button>',click)
    bt=Button(f,text='sqrt',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=4,column=3)
    bt.bind('<Button>',click)
    #4
    bt=Button(f,text='CE',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=5,column=0)
    bt.bind('<Button>',click)
    bt=Button(f,text='0',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=5,column=1)
    bt.bind('<Button>',click)
    bt=Button(f,text='=',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=5,column=2)
    bt.bind('<Button>',click)
    bt=Button(f,text='cube',font=myfont,relief=FLAT,width=6,height=3,borderwidth=0,activebackground='grey')
    bt.grid(row=5,column=3)
    bt.bind('<Button>',click)
    f.pack()
   
app =Tk()
basic()
strvr=StringVar()
struc()
app.mainloop()