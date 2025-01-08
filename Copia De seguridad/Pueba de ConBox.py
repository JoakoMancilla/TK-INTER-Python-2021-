
from tkinter import *
from tkinter import ttk

def Ver():
    dato = combo.get()
    if(dato=='frente'):
        conte.image=Image
        conte.config(image=Image)
        conte.place(x=80, y=80)
    if(dato=='lado Izquierdo'):
        conte.image=Image1
        conte.config(image=Image1)
        conte.place(x=80, y=80)
    if(dato=='lado derecho'):
        conte.image=Image2
        conte.config(image=Image2)
        conte.place(x=80, y=80)
    if(dato=='posterior'):
        conte.image=Image3
        conte.config(image=Image3)
        conte.place(x=80, y=80)

lfa_win=Tk()
lfa_win.title("App Grafica")
lfa_win.geometry("1200x650+85+20")
lfa_win.configure(bg="Gray19")
lfa_win.iconbitmap("icono.ico")

fondo=PhotoImage(file="Garage2.gif")
Lf=Label(lfa_win, image=fondo)
Lf.pack(anchor=CENTER)


t=Label (lfa_win, text="Selecione la vista que desea ver")
t.place(x=100, y=50)

combo = ttk.Combobox(lfa_win)
combo.place(x=100, y=100)
combo['value']=('Frente','lado Izquierdo','lado derechto','posterior')

b=Button(lfa_win, text="ver", command=Ver)
b.place(x=30, y=30)

Image=PhotoImage(file="Frontal1+Marco.gif")
Image1=PhotoImage(file="Lateral1+Marco.gif")
Image2=PhotoImage(file="Lateral2+Marco.gif")
Image3=PhotoImage(file="Trasera+Marco.gif")
conte=Button(lfa_win,bg="red",width=250,height=250,font=('helvica'))

    
    

lfa_win.mainloop()





