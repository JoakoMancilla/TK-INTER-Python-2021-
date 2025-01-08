from tkinter import *
from tkinter import ttk
import time
import winsound
global swin
global S
global a
global z


S = 0

#Intro
#------------------------------------------------------------------------------------------------------------------------------------------------#
global nombre
def ventana_1():
    global nombre
    global ventana
    global c
    ventana=Tk()
    ventana.title("App Grafica")
    ventana.geometry("1200x650+80+20")
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

    fondo=PhotoImage(file="Logo Universidad.gif")
    bf=Label(ventana, image=fondo)
    bf.place(x=10,y=10)
    
    ventana.mainloop()


#Menu De Inicio
#------------------------------------------------------------------------------------------------------------------------------------------------#

def ventana_2():
    global c
    global win
    global ventana
    nombre=c.get()
    if (nombre=="Player 1"):
        ventana.withdraw() #cerrar ventana 1
        win=Toplevel()
        win.title("App Grafica")
        win.geometry("1200x650+80+20")
        win.configure(bg="Gray19")
        win.iconbitmap("icono.ico")
        winsound.PlaySound('Menu song 1', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    
        foto1=PhotoImage(file="original.gif")
        F=Label(win,image=foto1)
        F.pack(anchor=CENTER)

        iBoton1=PhotoImage(file="Aauto.gif")
        b1=Button(win,bg="Purple",image=iBoton1, command=Autos).place(x=900, y=250)

        iBoton2=PhotoImage(file="Personalizar 2.gif")
        b2=Button(win,bg="Purple",image=iBoton2, command=Taller).place(x=900, y=350)
    
        iBoton3=PhotoImage(file="Correr.gif")
        b3=Button(win,bg="Purple",image=iBoton3, command=Game).place(x=900, y=450)

        b4=Button(win, text="Cerrar Aplicacion",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=killV)
        b4.place(x=10, y=10)


        #x = IntVar() #1 si, 0 no
        #y = IntVar() #1 si, 0 no

        Label(win,width=20, height=1, text= "Musica",bg="Orange2").place(x=500,y=10)
        Radiobutton(win, text="Mute",bg="Orange2", value=1, command=MuteMusicMenu).place(x=590, y=35)
        Radiobutton(win, text="Play",bg="Orange2",value=0, command=MusicMenu).place(x=500, y=35)
    
    
    

        #monitor=Label(win)
        #monitor.pack()
        win.mainloop()

    else:
        t1=Label(ventana, text="Nombre Del Jugador Incorrecto", font="Unispace", bg="brown3",fg="white" )
        t1.place(x=450, y=450)
        c.delete(0,END)
        



#selector de autos
#------------------------------------------------------------------------------------------------------------------------------------------------#
def Autos():
    global win2
    win.withdraw() #cerrar ventana 2
    win2=Toplevel()
    win2.title("App Grafica")
    win2.geometry("1200x650+80+20")
    win2.configure(bg="Gray19")
    win2.iconbitmap("icono.ico")

    foto1=PhotoImage(file="Seleccion de auto.gif")
    F=Label(win2,image=foto1)
    F.pack(anchor=CENTER)

    b=Button(win2, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=retro1)
    b.place(x=10, y=10)

    b1=Button(win2, text="Lexus",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lexus)
    b1.place(x=500, y=500)

    b1=Button(win2, text="Ferrari",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Ferrari)
    b1.place(x=100, y=500)

    b1=Button(win2, text="Gtr",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=GTR)
    b1.place(x=900, y=500)
    
    win2.mainloop()


#Prestaciones
#------------------------------------------------------------------------------------------------------------------------------------------------#
def Taller():
    global win3
    win.withdraw() #cerrar ventana 2
    win3=Toplevel()
    win3.title("App Grafica")
    win3.geometry("1200x650+80+20")
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

#Audios
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Sonidos de Motor    
def Sonido1():
        winsound.PlaySound('LfaEngine.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
def Sonido2():
        winsound.PlaySound('Turbo Engine.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
def Sonido3():
        winsound.PlaySound('V10.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)

#musica menu
def MusicMenu():
    winsound.PlaySound('Menu song 1', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
def MuteMusicMenu():
    winsound.PlaySound(None, winsound.SND_LOOP)



#Juego
#------------------------------------------------------------------------------------------------------------------------------------------------#
def Game():
    global win4
    win.withdraw() #cerrar ventana 2
    win4=Toplevel()
    win4.title("App Grafica")
    win4.geometry("1200x650+80+20")
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

    b9=Button(win4, text="Direccion",fg="White",font="Unispace", bg="SkyBlue3", width=30, height=2, command=Direccion)
    b9.place(x=450, y=400)

    win4.mainloop()



#Cierres
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Cierre de ventanas principales
def retro1():
    MuteMusicMenu()
    win2.withdraw()
    ventana_2()
    
def retro2():
    MuteMusicMenu()
    win3.withdraw()
    ventana_2()
    
def retro3():
    MuteMusicMenu()
    win4.withdraw()
    ventana_2()
    
#Cierre de sub ventanas
def CerrarPista():
    MuteMusicMenu()
    swin.withdraw()
    ventana_2()
    
def Velo_Close():
    MuteMusicMenu()
    subwin2.withdraw()
    ventana_2()
    
#Cierre de Ventana des autos
def Lfa_Close():
    MuteMusicMenu()
    global S
    S = S * 0
    win_L.withdraw()
    ventana_2()
    
def Seleccion1():
    MuteMusicMenu()
    global S
    S = S * 0
    S = S + 1
    win_L.withdraw()
    ventana_2()
    
def Seleccion2():
    MuteMusicMenu()
    global S
    S = S * 0
    S = S + 2
    win_L.withdraw()
    ventana_2()

def Seleccion3():
    MuteMusicMenu()
    global S
    S = S * 0
    S = S + 3
    win_L.withdraw()
    ventana_2()
    
#Cerrar APP
def killV():
    MuteMusicMenu()
    win.destroy()


#Catalogo de Autos
#------------------------------------------------------------------------------------------------------------------------------------------------#
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
    win_L.geometry("1200x650+80+20")
    win_L.configure(bg="Gray19")
    win_L.iconbitmap("icono.ico")

    fondo=PhotoImage(file="Garage.gif")
    Lf=Label(win_L, image=fondo)
    Lf.pack(anchor=CENTER)


    t=Label (win_L, text="Selecione la vista que desea ver")
    t.place(x=515, y=100)

    combo = ttk.Combobox(win_L)
    combo.place(x=550, y=550)
    combo['value']=('Frente','Lado Izquierdo','Lado Derecho','Posterior')
    combo.set('Frente')

    b=Button(win_L, text="ver 📷", command=Ver)
    b.place(x=500, y=550)

    r=Button (win_L, text="Selecionar Vehiculo",bg="Orange2",height=2,command=Seleccion1)
    r.place(x=545, y=10)

    imagen_frontal=PhotoImage(file="Frontal1+Marco.gif")
    imagen_Izquierda=PhotoImage(file="Lateral1+Marco.gif")
    imagen_Derecha=PhotoImage(file="Lateral2+Marco.gif")
    imagen_trasera=PhotoImage(file="Trasera+Marco.gif")
    conte=Button(win_L,bg="Black",font=('helvica'))

    b4=Button(win_L, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lfa_Close)
    b4.place(x=10, y=10)

    win_L.mainloop()

    
#Ferrari
def Ferrari():
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
    win_L.geometry("1200x650+80+20")
    win_L.configure(bg="Gray19")
    win_L.iconbitmap("icono.ico")

    fondo=PhotoImage(file="Garage.gif")
    Lf=Label(win_L, image=fondo)
    Lf.pack(anchor=CENTER)


    t=Label (win_L, text="Selecione la vista que desea ver")
    t.place(x=515, y=100)

    combo = ttk.Combobox(win_L)
    combo.place(x=550, y=550)
    combo['value']=('Frente','Lado Izquierdo','Lado Derecho','Posterior')
    combo.set('Frente')

    b=Button(win_L, text="ver 📷", command=Ver)
    b.place(x=500, y=550)

    r=Button (win_L, text="Selecionar Vehiculo",bg="Orange2",height=2,command=Seleccion2)
    r.place(x=545, y=10)

    imagen_frontal=PhotoImage(file="1 Ferrari.gif")
    imagen_Izquierda=PhotoImage(file="2 Ferrari.gif")
    imagen_Derecha=PhotoImage(file="3 Ferrari.gif")
    imagen_trasera=PhotoImage(file="4 Ferrari.gif")
    conte=Button(win_L,bg="Black",font=('helvica'))

    b4=Button(win_L, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lfa_Close)
    b4.place(x=10, y=10)

    win_L.mainloop()


#Gtr
def GTR():
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
    win_L.geometry("1200x650+80+20")
    win_L.configure(bg="Gray19")
    win_L.iconbitmap("icono.ico")

    fondo=PhotoImage(file="Garage.gif")
    Lf=Label(win_L, image=fondo)
    Lf.pack(anchor=CENTER)


    t=Label (win_L, text="Selecione la vista que desea ver")
    t.place(x=515, y=100)

    combo = ttk.Combobox(win_L)
    combo.place(x=550, y=550)
    combo['value']=('Frente','Lado Izquierdo','Lado Derecho','Posterior')
    combo.set('Frente')

    b=Button(win_L, text="ver 📷", command=Ver)
    b.place(x=500, y=550)

    r=Button (win_L, text="Selecionar Vehiculo",bg="Orange2",height=2,command=Seleccion3)
    r.place(x=545, y=10)

    imagen_frontal=PhotoImage(file="gtr 1.gif")
    imagen_Izquierda=PhotoImage(file="gtr 2.gif")
    imagen_Derecha=PhotoImage(file="gtr 3.gif")
    imagen_trasera=PhotoImage(file="gtr 4.gif")
    conte=Button(win_L,bg="Black",font=('helvica'))

    b4=Button(win_L, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Lfa_Close)
    b4.place(x=10, y=10)

    win_L.mainloop()


#Juegos
#------------------------------------------------------------------------------------------------------------------------------------------------#
def Ir_pista():
    win4.withdraw()
    global swin
    global a

    #MINI
    if(S==0):
        
        a=0
        def Iniciar():
            global a
            if (a<=11):
                print(a)
                time.sleep(.5)
                z.set(a)
                a=a+1
                if(a==1):
                    winsound.PlaySound('LfaEngine.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
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
                    winsound.PlaySound('Frenado.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
                    
    
                e.after(50,Iniciar)
                

           
        def salir():
            swin.withdraw()
            ventana_2()



        swin=Toplevel()
        swin.title("App Grafica")
        swin.geometry("1200x650+85+20")
        swin.iconbitmap("icono.ico")
        swin.configure(bg="Purple4")


        fondo=PhotoImage(file="222.gif")#Fondo
        Lf=Label(swin, image=fondo)
        Lf.pack(anchor=CENTER)

        foto=PhotoImage(file="Auto Predeterminado.gif")#Auto
        Ab=Label(swin,bg="Purple4", image=foto)
        #Ab.place(x=50, y=560)


        Semaforo=PhotoImage(file="Semaforo H.gif")#Femaforo
        SL=Label(swin,bg="Purple4", image=Semaforo)
        SL.place(x=500, y=10)

        b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
        b1.place(x=700, y=10)

        b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
        b2.place(x=700, y=55)

        t=Label (swin, text="⚠ ADVERTENCIA: no seleciono vehiculo ⚠")
        t.place(x=400, y=130)
        t.configure(bg="Brown3",fg="Grey20",font="Unispace", width=40, height=1)

        z =IntVar()
        e = Entry(swin, textvariable = z)
        e.config(bg ="Orange2", font = ("verdana",25))
        e.place(x=420, y=30, width =60, height=50)


        swin.mainloop()
    

    #Lexus
    if(S==1):
        a=0
        def Iniciar():
            global a
            if a<=11:
                print(a)
                time.sleep(.1)
                z.set(a)
                a=a+1
                if(a==1):
                    winsound.PlaySound('V10.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
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
                    winsound.PlaySound('Frenado.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
    
                e.after(50,Iniciar)
                

           
        def salir():
            swin.withdraw()
            ventana_2()



        swin=Toplevel()
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
        SL=Label(swin,bg="Purple4", image=Semaforo)
        SL.place(x=500, y=10)

        b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
        b1.place(x=700, y=10)

        b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
        b2.place(x=700, y=55)

        z =IntVar()
        e = Entry(swin, textvariable = z)
        e.config(bg ="Orange2", font = ("verdana",25))
        e.place(x=420, y=30, width =60, height=50)


        swin.mainloop()
        
#ferrari
    if(S==2):
        a=0
        def Iniciar():
            global a
            
            if a<=11:
                print(a)
                time.sleep(.1)
                z.set(a)
                a=a+1
                if(a==1):
                    winsound.PlaySound('V10.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
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
                    winsound.PlaySound('Frenado.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
                e.after(50,Iniciar)
                

           
        def salir():
            swin.withdraw()
            ventana_2()



        swin=Toplevel()
        swin.title("App Grafica")
        swin.geometry("1200x650+80+20")
        swin.iconbitmap("icono.ico")
        swin.configure(bg="Purple4")


        fondo=PhotoImage(file="222.gif")#Fondo
        Lf=Label(swin, image=fondo)
        Lf.pack(anchor=CENTER)

        foto=PhotoImage(file="Ferrari 2D.gif")#Auto
        Ab=Label(swin,bg="Purple4", image=foto)
        #Ab.place(x=50, y=560)


        Semaforo=PhotoImage(file="Semaforo H.gif")#Semaforo
        SL=Label(swin,bg="Purple4", image=Semaforo)
        SL.place(x=500, y=10)

        b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
        b1.place(x=700, y=10)

        b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
        b2.place(x=700, y=55)



       
        z =IntVar()
        e = Entry(swin, textvariable = z)
        e.config(bg = "Orange2", font = ("verdana",25))
        e.place(x=420, y=30, width =60, height=50)


        swin.mainloop()


    if(S==0):
        Seleccion1()


#Nissan 
    if(S==3):
        a=0
        def Iniciar():
            global a
            
            if a<=11:
                print(a)
                time.sleep(.1)
                z.set(a)
                a=a+1
                if(a==1):
                    winsound.PlaySound('Turbo Engine.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
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
                    winsound.PlaySound('Frenado.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
                e.after(50,Iniciar)
                

           
        def salir():
            swin.withdraw()
            ventana_2()



        swin=Toplevel()
        swin.title("App Grafica")
        swin.geometry("1200x650+80+20")
        swin.iconbitmap("icono.ico")
        swin.configure(bg="Purple4")


        fondo=PhotoImage(file="222.gif")#Fondo
        Lf=Label(swin, image=fondo)
        Lf.pack(anchor=CENTER)

        foto=PhotoImage(file="gtr m.gif")#Auto
        Ab=Label(swin,bg="Purple4", image=foto)
        #Ab.place(x=50, y=560)


        Semaforo=PhotoImage(file="Semaforo H.gif")#Semaforo
        SL=Label(swin,bg="Purple4", image=Semaforo)
        SL.place(x=500, y=10)

        b1=Button(swin, text="",bg="Green4",width=5, height=2, command=Iniciar)
        b1.place(x=700, y=10)

        b2=Button(swin, text="",bg="Red",width=5, height=2, command=salir)
        b2.place(x=700, y=55)



       
        z =IntVar()
        e = Entry(swin, textvariable = z)
        e.config(bg = "Orange2", font = ("verdana",25))
        e.place(x=420, y=30, width =60, height=50)


        swin.mainloop()

#Velocimetro
def velocimetro():
    global a
    global z
    global e
    a=0
    def IniciarV():
            global a
            if a<=130:
                print(a)
                time.sleep(.5)
                z.set(a)
                a=a+10
                if(a==10):
                    winsound.PlaySound('V10.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
                if(a==20):
                    pass
                if(a==30):
                    pass
                if(a==40):
                    pass
                if(a==50):
                    pass
                if(a==60):
                    pass          
                if(a==70):
                    pass    
                if(a==80):
                    pass
                if(a==90):
                    pass
                if(a==100):
                    pass
                if(a==110):
                    pass
                if(a==120):
                    pass
                if(a==130):
                    winsound.PlaySound('Frenado.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
                    Label(subwin2,width=12, height=1, text= "Vel Maxima!",bg="red",fg="white",font="Unispace").place(x=650,y=60)
                e.after(50,IniciarV)
    
    global subwin2
    win4.withdraw()
    subwin2=Toplevel()
    subwin2.title("App Grafica")
    subwin2.geometry("1200x650+80+20")
    subwin2.iconbitmap("icono.ico")
    
    fondo=PhotoImage(file="Velocimetro InteractivoV2.png")
    Lf=Label(subwin2, image=fondo)
    Lf.pack(anchor=CENTER)
    
    b=Button(subwin2, text="Volver Atras",fg="White",font="Unispace", bg="Red2", width=20, height=2, command=Velo_Close)
    b.place(x=10, y=10)


    b1=Button(subwin2,text="▷",font="Unispace",bg="green4",width=5, height=2, command=IniciarV)
    b1.place(x=250, y=450)

    z =IntVar()
    e = Entry(subwin2, textvariable = z)
    e.config(bg = "Grey86", font = ("verdana",25))
    e.place(x=575, y=57, width =60, height=50)


    subwin2.mainloop()

#Direccion
#------------------------------------------------------------------------------------------------------------------------------------------------#
def Direccion():
    win4.withdraw()
    MuteMusicMenu()
    print("2")
    winsound.PlaySound('Calle', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    

    a=0
    def Iniciar():
        winsound.PlaySound('Claxon', winsound.SND_FILENAME)
        
        winsound.PlaySound('Calle', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
        
        
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

    #foto=PhotoImage(file="cocheb.gif")#Auto
    #Ab=Label(swin,bg="grey", image=foto)
    #Ab.place(x=50, y=560)

    foto1=PhotoImage(file="Principal1.gif")#Auto
    Ab=Label(swin,bg="grey", image=foto1)


    Semaforo=PhotoImage(file="ford.gif")#Femaforo
    SL=Label(swin,bg="Purple4", image=Semaforo)
    SL.place(x=500, y=10)

    t5=Label(swin, text="Mueva la barra para elegir Cariil", font="Unispace", bg="grey21",fg="white" )
    t5.place(x=450, y=500)

    n2=IntVar()
    escala = Scale(swin, from_=1, to=3, variable=n2, length=300, resolution=1,orient='vertical',bg="grey21",fg="White",command=esquivar)
    escala.place(x=10, y=170) 

    b1=Button(swin, text="📣",bg="Green4",width=5, height=2, command=Iniciar)
    b1.place(x=700, y=10)

    b2=Button(swin, text="❎",bg="Red",width=5, height=2, command=salir)
    b2.place(x=700, y=55)


    swin.mainloop()

    def salir():
        swin.withdraw()
        ventana_2()




ventana_1()

