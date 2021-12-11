import tkinter
from tkinter import *

#raiz
raiz= tkinter.Tk()
raiz.title=("PROYECTO ARQUITECTURA DE COMPUTADORES")
#cambiar el icono
raiz.iconbitmap("podcast.ico")
#tamaño de la raiz
raiz.geometry("900x600")
raiz.config(bg="black")

#Frame
miFrame=Frame()
miFrame.pack(fill="y")
miFrame.config(bg="white")
miFrame.config(width="890",height="590")
#miFrame.config(bd=35)
#miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")




tituloPrincipal=Label(miFrame, text="POTCAST",fg="black",font=("Comic Sans MS",18))
tituloPrincipal.grid(row=0,column=1)

#aun no sale imagen
miImagen=PhotoImage(file="icono.png")
Label(miFrame,image=miImagen)
miImagen.grid(row=0,column=0)




#etiqueta TITULO y Posicion
#etiqueta = tkinter.Label(raiz,text = "POSTCAST", bg="blue")
#etiqueta.pack()

raiz.mainloop()