from tkinter import *
from tkinter import ttk
import time
import winsound


#Intro
global nombre
def ventana_1():
    global nombre
    global ventana
    global c
    ventana=Tk()
    ventana.title("App Grafica")
    ventana.geometry("1200x650+85+20")
    ventana.iconbitmap("icono.ico")

    foto=PhotoImage(file="Fondo & Logo.gif")
    F=Label(ventana,image=foto)
    F.pack(anchor=CENTER)
    
    nombre =StringVar()
    nombre.set("")
    c=Entry(ventana, textvariable=nombre, width=30)
    c.place(x=600, y=500)
   
    t=Label(ventana, text="Nombre Del Jugador", font="Unispace", bg="VioletRed1",fg="grey20" )
    t.place(x=400, y=500)

    b=Button(ventana, text="entrar",font="Unispace", bg="DarkOrchid",fg="grey20", command=ventana_2)
    b.place(x=550, y=550)
    
    ventana.mainloop()


#Menu De Inicio
def ventana_2():
    global c
    global win
    nombre=str(c.get())
    ventana.withdraw() #cerrar ventana 1
    win=Toplevel()
    win.title("App Grafica")
    win.geometry("1200x650+85+20")
    win.configure(bg="Gray19")
    win.iconbitmap("icono.ico")

    foto1=PhotoImage(file="original.gif")
    F=Label(win,image=foto1)
    F.pack(anchor=CENTER)

    b1=Button(win, text="Autos", bg="Orange2",font="Unispace", width=10, height=4, command=Autos)
    b1.place(x=900, y=250)

    b2=Button(win, text="Gestor de Vehiculos",font="Unispace", bg="Orange3", width=20, height=4, command=Taller)
    b2.place(x=900, y=350)

    b3=Button(win, text="Prueba Tus Modificaciones!",font="Unispace", bg="Orange2", width=27, height=4, command=Game)
    b3.place(x=900, y=450)

    b4=Button(win, text="Cerrar Aplicacion",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=killV)
    b4.place(x=10, y=10)
    
    win.mainloop()





#selector de autos
def Autos():
    global win2
    win.withdraw() #cerrar ventana 2
    win2=Toplevel()
    win2.title("App Grafica")
    win2.geometry("1200x650+85+20")
    win2.configure(bg="Gray19")
    win2.iconbitmap("icono.ico")

    foto1=PhotoImage(file="Seleccion de auto.gif")
    F=Label(win2,image=foto1)
    F.pack(anchor=CENTER)

    b=Button(win2, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=retro1)
    b.place(x=10, y=10)

    b1=Button(win2, text="Lexus",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lexus)
    b1.place(x=500, y=500)

    win2.mainloop()

#Prestaciones
def Taller():
    global win3
    win.withdraw() #cerrar ventana 2
    win3=Toplevel()
    win3.title("App Grafica")
    win3.geometry("1200x650+85+20")
    win3.configure(bg="Gray19")
    win3.iconbitmap("icono.ico")

    foto2=PhotoImage(file="Taller.gif")
    f=Label(win3,image=foto2)
    f.pack(anchor=CENTER)


    t=Label (win3, text="⚠ ADVERTENCIA: Se Reproducira Sonido ⚠")
    t.place(x=400, y=10)
    t.configure(bg="Orange2",fg="Grey20",font="Unispace", width=45, height=2)

    imgBoton1=PhotoImage(file="Motor 1.gif")
    BM1=Button(win3,text="Motor1",bg="Orange4",image=imgBoton1, command=Sonido1).place(x=100, y=200)

    imgBoton2=PhotoImage(file="Motor 2.gif")
    BM2=Button(win3,text="Motor1",bg="Grey83",image=imgBoton2, command=Sonido2).place(x=500, y=200)

    imgBoton3=PhotoImage(file="Motor 3.gif")
    BM3=Button(win3,text="Motor1",bg="Gold",image=imgBoton3, command=Sonido3).place(x=900, y=200)

    b5=Button(win3, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=retro2)
    b5.place(x=10, y=10)


    win3.mainloop()

#Sonidos de motor
    
def Sonido1():
        winsound.PlaySound('LfaEngine.wav', winsound.SND_FILENAME)
def Sonido2():
        winsound.PlaySound('Turbo Engine.wav', winsound.SND_FILENAME)
def Sonido3():
        winsound.PlaySound('V10.wav', winsound.SND_FILENAME)
 

#Juego
def Game():
    global win4
    win.withdraw() #cerrar ventana 2
    win4=Toplevel()
    win4.title("App Grafica")
    win4.geometry("1200x650+85+20")
    win4.configure(bg="Gray19")
    win4.iconbitmap("icono.ico")

    foto3=PhotoImage(file="Track.gif")
    F=Label(win4,image=foto3)
    F.pack(anchor=CENTER)

    b6=Button(win4, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=retro3)
    b6.place(x=10, y=10)

    b7=Button(win4, text="Ir a la Pista",fg="White",font="Unispace", bg="SkyBlue3", width=30, height=2, command=Ir_pista)
    b7.place(x=625, y=500)

    b8=Button(win4, text="Velocimetro",fg="White",font="Unispace", bg="SkyBlue3", width=30, height=2, command=velocimetro)
    b8.place(x=275, y=500)

    win4.mainloop()


#Cerrar APP
def killV():
    win.destroy()
#Cierre de ventanas
def retro1():
    win2.withdraw()
    ventana_2()
def retro2():
    win3.withdraw()
    ventana_2()
def retro3():
    win4.withdraw()
    ventana_2()
    

#Cierre de sub ventanas
def CerrarPista():
    swin.withdraw()
    ventana_2()
def Velo_Close():
    subwin2.withdraw()
    ventana_2()



    
#Catalogo de Autos

#Lexus
    
def Lexus():
    global combo
    def Ver():
        global combo
        dato = combo.get()
        if(dato=='Frente'):
            conte.image=imagen_frontal
            conte.config(image=imagen_frontal)
            conte.place(x=375, y=200)
        if(dato=='Lado Izquierdo'):
            conte.image=imagen_Izquierda
            conte.config(image=imagen_Izquierda)
            conte.place(x=375, y=200)
        if(dato=='Lado Derecho'):
            conte.image=imagen_Derecha
            conte.config(image=imagen_Derecha)
            conte.place(x=375, y=200)
        if(dato=='Posterior'):
            conte.image=imagen_trasera
            conte.config(image=imagen_trasera)
            conte.place(x=375, y=200) 

    global win_L
    win2.withdraw() #cerrar ventana 2
    win_L=Toplevel()
    win_L.title("App Grafica")
    win_L.geometry("1200x650+85+20")
    win_L.configure(bg="Gray19")
    win_L.iconbitmap("icono.ico")

    fondo=PhotoImage(file="Garage.gif")
    Lf=Label(win_L, image=fondo)
    Lf.pack(anchor=CENTER)


    t=Label (win_L, text="Selecione la vista que desea ver")
    t.place(x=550, y=100)

    combo = ttk.Combobox(win_L)
    combo.place(x=550, y=550)
    combo['value']=('Frente','Lado Izquierdo','Lado Derecho','Posterior')
    combo.set('Frente')

    b=Button(win_L, text="ver 📷", command=Ver)
    b.place(x=500, y=550)

    imagen_frontal=PhotoImage(file="Frontal1+Marco.gif")
    imagen_Izquierda=PhotoImage(file="Lateral1+Marco.gif")
    imagen_Derecha=PhotoImage(file="Lateral2+Marco.gif")
    imagen_trasera=PhotoImage(file="Trasera+Marco.gif")
    conte=Button(win_L,bg="Black",font=('helvica'))

    b4=Button(win_L, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lfa_Close)
    b4.place(x=10, y=10)

    win_L.mainloop()
    
   
    



#Cierre de Ventana des autos

def Lfa_Close():
    win_L.withdraw()
    ventana_2()




#Ligado a Game
def Ir_pista():
    global swin
    win4.withdraw() #cerrar ventana 3
    swin=Toplevel()
    swin.title("App Grafica")
    swin.geometry("1200x650+85+20")
    swin.iconbitmap("icono.ico")
    swin.configure(bg="Purple4")


    Imagen=PhotoImage(file="LFA2D.png")#imagen secundaria
    fondo=PhotoImage(file="222.gif")
    Lf=Label(swin, image=fondo)
    Lf.pack(anchor=CENTER)
    Li=Label(swin,bg="Purple4", image=Imagen)
    Li.place(x=50, y=560)

    Semaforo=PhotoImage(file="Semaforo H.gif")
    SL=Label(swin, image=Semaforo)
    SL.place(x=500, y=10)

    b1=Button(swin, text="",bg="Green4",width=5, height=2)
    b1.place(x=700, y=10)

    b2=Button(swin, text="",bg="Red",width=5, height=2)
    b2.place(x=700, y=55)




    b=Button(swin, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=CerrarPista)
    b.place(x=10, y=10)

    swin.mainloop()


def velocimetro():
    global subwin2
    win4.withdraw()
    subwin2=Toplevel()
    subwin2.title("App Grafica")
    subwin2.geometry("1200x650+85+20")
    subwin2.iconbitmap("icono.ico")
    
    fondo=PhotoImage(file="Velocimetro InteractivoV2.png")
    Lf=Label(subwin2, image=fondo)
    Lf.pack(anchor=CENTER)
    
    b=Button(subwin2, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Velo_Close)
    b.place(x=10, y=10)


    b1=Button(subwin2,text="▷",font="Unispace",bg="green4",width=5, height=2, command=Sonido3)
    b1.place(x=250, y=450)





    

    subwin2.mainloop()







    



ventana_1()
        
