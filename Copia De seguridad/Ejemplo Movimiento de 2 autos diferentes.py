from tkinter import *
from tkinter import ttk
import time
import winsound
global swin
global s

s=1


if (s==1):
    a=0

    def Iniciar():
        global a
        global s
        if a<=11:
            print(a)
            time.sleep(.1)
            z.set(a)
            a=a+1
            if(a==1):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=20, y=560)
            if(a==2):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=120, y=560)
            if(a==3):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=220, y=560)
            if(a==4):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=320, y=560)
            if(a==5):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=420, y=560)

    #inecesario
            if(a==6):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=520, y=560)
            if(a==7):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=620, y=560)
            if(a==8):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=720, y=560)
            if(a==9):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=820, y=560)
            if(a==10):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=920, y=560)
            if(a==11):
                winsound.Beep(2500, 2000)
                winsound.PlaySound('Prueba4.wav', winsound.SND_FILENAME)
            c.after(50,Iniciar)

           
    def salir():
        pass



    swin=Tk()
    swin.title("App Grafica")
    swin.geometry("1200x650+85+20")
    swin.iconbitmap("icono.ico")
    swin.configure(bg="Purple4")


    fondo=PhotoImage(file="222.gif")#Fondo
    Lf=Label(swin, image=fondo)
    Lf.pack(anchor=CENTER)

    foto=PhotoImage(file="LFA2D.png")#Auto
    Ab=Label(swin,bg="Purple4", image=foto)
    #Ab.place(x=50, y=560)


    Semaforo=PhotoImage(file="Semaforo H.gif")#Femaforo
    SL=Label(swin, image=Semaforo)
    SL.place(x=500, y=10)

    b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
    b1.place(x=700, y=10)

    b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
    b2.place(x=700, y=55)



    #primera prueba velocimetro
    z =IntVar()
    c = Entry(swin, textvariable = z)
    c.config(bg = "cyan", font = ("verdana",25))
    c.place(x=10, y=10, width =60, height=50)


    swin.mainloop()
    a+1
#------------------------------------------------------------------------------------------------------------------#
if (s==2):
    a=0

    def Iniciar():
        global a
        if a<=11:
            print(a)
            time.sleep(.1)
            z.set(a)
            a=a+1
            if(a==1):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=20, y=560)
            if(a==2):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=120, y=560)
            if(a==3):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=220, y=560)
            if(a==4):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=320, y=560)
            if(a==5):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=420, y=560)

    #inecesario
            if(a==6):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=520, y=560)
            if(a==7):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=620, y=560)
            if(a==8):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=720, y=560)
            if(a==9):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=820, y=560)
            if(a==10):
                Ab.image = foto
                Ab.config(image=foto)
                Ab.place(x=920, y=560)
            if(a==11):
                winsound.Beep(2500, 2000)
                winsound.PlaySound('Prueba4.wav', winsound.SND_FILENAME)
            c.after(50,Iniciar)

           
    def salir():
        pass



    swin=Tk()
    swin.title("App Grafica")
    swin.geometry("1200x650+85+20")
    swin.iconbitmap("icono.ico")
    swin.configure(bg="Purple4")


    fondo=PhotoImage(file="222.gif")#Fondo
    Lf=Label(swin, image=fondo)
    Lf.pack(anchor=CENTER)

    foto=PhotoImage(file="Ferrari 2D.gif")#Auto
    Ab=Label(swin,bg="Purple4", image=foto)
    #Ab.place(x=50, y=560)


    Semaforo=PhotoImage(file="Semaforo H.gif")#Femaforo
    SL=Label(swin, image=Semaforo)
    SL.place(x=500, y=10)

    b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
    b1.place(x=700, y=10)

    b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
    b2.place(x=700, y=55)



    #primera prueba velocimetro
    z =IntVar()
    c = Entry(swin, textvariable = z)
    c.config(bg = "cyan", font = ("verdana",25))
    c.place(x=10, y=10, width =60, height=50)


    swin.mainloop()



