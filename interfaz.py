import tkinter
from tkinter import *
from tkinter import filedialog
#raiz
raiz= tkinter.Tk()
raiz.title=("PROYECTO ARQUITECTURA DE COMPUTADORES")
#cambiar el icono
raiz.iconbitmap("podcast.ico")
#tamaño de la raiz
raiz.geometry("900x600")
raiz.config(bg="black")

#Frame
miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="white")
miFrame.config(width="890",height="590")
miFrame.config(bd=35)
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")



#aun no sale imagen
miImagen=PhotoImage(file="icono2.png")
Label(miFrame,image=miImagen).place(x=5,y=5)

#------------------------------------------------------------------
#miImagen=PhotoImage(file="icono.png")
#miImagen.place(x=200,y=0)


tituloPrincipal=Label(miFrame, text="POTCAST",fg="black",font=("Comic Sans MS",18))
tituloPrincipal.place(x=400,y=0)


#TITULO
etiquetaTitulo=Label(miFrame, text="titulo",fg="black",font=("Comic Sans MS",12))
etiquetaTitulo.place(x=600,y=120)

etiquetaBuscarArchivo=Label(miFrame, text="Abrir Archivo",fg="black",font=("Comic Sans MS",12))
etiquetaBuscarArchivo.place(x=80,y=160)
#CAJA DE TEXTO,como comentario
cajaTexto = tkinter.Text(miFrame)
cajaTexto.place(x=500,y=150,width=270,height=300)


#
#cajaTexto = tkinter.Entry(miFrame)
#cajaTexto.place(x=500,y=150,width=270,height=300)




#etiqueta TITULO y Posicion
#etiqueta = tkinter.Label(raiz,text = "POSTCAST", bg="blue")
#etiqueta.pack()
raiz.mainloop()



##def test():
    # *Ventana de elección de color
    # color = colorchooser.askcolor(title="Elige un color")
    # print(color)
    # *Devuelve la dirección del archivo(ruta completa)
    # initialdir -> Presupone desde que unidad abrir
    # filetypes -> Filtro de archivos
    # fichero = filedialog.askopenfilename(title="Abrir un fichero", initialdir="C:", filetypes=(("Fichero de texto","*.txt"),("Fichero de texto avanzado","*.txt2"),("Todos los ficheros posibles","*,*")))
    # print(fichero)
    # *Equivale a open("ruta","w")
    # mode -> formato de abrir el archivo
##   fichero = filedialog.asksaveasfile(miFrame,title="Guardar un archivo", mode="r+")
##  if fichero is not None:
##     fichero.write("Texto de relleno").place(x=20,y=20)
##     #faltaria dimensionarlo
##    fichero.close()
##Button(raiz, text="Click", command=test).pack()