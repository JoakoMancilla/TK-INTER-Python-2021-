from tkinter import *
import time
import winsound

def Direccion():

    a=0
    def Iniciar():
        winsound.PlaySound('Claxon', winsound.SND_FILENAME|winsound.SND_ASYNC)
        
    def esquivar(value):
        print(value)
        b=escala.get()
        if(b==1):
            Ab.image = foto1
            Ab.config(image=foto1)
            Ab.place(x=420, y=190)
        if(b==2):
            Ab.image = foto1
            Ab.config(image=foto1)
            Ab.place(x=420, y=280)
        if(b==3):
            Ab.image = foto1
            Ab.config(image=foto1)
            Ab.place(x=420, y=360)
       
    def salir():
        swin.withdraw()
        ventana_2()

    swin=Toplevel()
    swin.title("App Grafica")
    swin.geometry("1200x650+85+20")
    swin.iconbitmap("icono.ico")
    swin.configure(bg="Purple4")


    fondo=PhotoImage(file="Carretera.gif")#Fondo
    Lf=Label(swin, image=fondo)
    Lf.pack(anchor=CENTER)

    foto=PhotoImage(file="cocheb.gif")#Auto
    Ab=Label(swin,bg="grey", image=foto)
        #Ab.place(x=50, y=560)
    foto1=PhotoImage(file="Principal1.gif")#Auto
    Ab=Label(swin,bg="grey", image=foto1)


    Semaforo=PhotoImage(file="ford.gif")#Femaforo
    SL=Label(swin,bg="Purple4", image=Semaforo)
    SL.place(x=500, y=10)

    n2=IntVar()
    escala = Scale(swin, from_=1, to=3, variable=n2, length=300, resolution=1,orient='vertical',bg="grey21",fg="White",command=esquivar)
    escala.place(x=10, y=170) 

    b1=Button(swin, text="📣",bg="Green4",width=5, height=2, command=Iniciar)
    b1.place(x=700, y=10)

    b2=Button(swin, text="❎",bg="Red",width=5, height=2, command=salir)
    b2.place(x=700, y=55)

    swin.mainloop()
