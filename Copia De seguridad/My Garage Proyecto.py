from tkinter import *

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

    foto2=PhotoImage(file="Garage2.gif")
    f=Label(win3,image=foto2)
    f.pack(anchor=CENTER)

    b5=Button(win3, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=retro2)
    b5.place(x=10, y=10)

    win3.mainloop()

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
    global lfa_win
    win2.withdraw()
    lfa_win=Toplevel()
    lfa_win.title("App Grafica")
    lfa_win.geometry("1200x650+85+20")
    lfa_win.configure(bg="Gray19")
    lfa_win.iconbitmap("icono.ico")

    Imagen=PhotoImage(file="Frontal1+Marco.gif")#imagen secundaria
    fondo=PhotoImage(file="Garage2.gif")
    Lf=Label(lfa_win, image=fondo)
    Lf.pack(anchor=CENTER)
    Li=Label(lfa_win, image=Imagen)
    Li.place(x=375, y=200)
    
    b4=Button(lfa_win, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lfa_Close)
    b4.place(x=10, y=10)

    lfa_win.mainloop()

    

#Cierre de Ventana des autos

def Lfa_Close():
    lfa_win.withdraw()
    ventana_2()




#Ligado a Game
def Ir_pista():
    global swin
    win4.withdraw() #cerrar ventana 3
    swin=Toplevel()
    swin.title("App Grafica")
    swin.geometry("1200x650+85+20")
    swin.iconbitmap("icono.ico")


    Imagen=PhotoImage(file="LFA2D.png")#imagen secundaria
    fondo=PhotoImage(file="222.gif")
    Lf=Label(swin, image=fondo)
    Lf.pack(anchor=CENTER)
    Li=Label(swin, image=Imagen)
    Li.place(x=50, y=560)

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

    subwin2.mainloop()







    



ventana_1()
        

        


