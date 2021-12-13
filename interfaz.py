import tkinter
from tkinter import *
from tkinter import filedialog
#raiz
raiz= tkinter.Tk()
raiz.title=("AC")
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
miImagen=PhotoImage(file="icono.png")
Imagen=miImagen.subsample(4,4)
Label(miFrame,image=Imagen).place(x=0,y=0)

#------------------------------------------------------------------
#miImagen=PhotoImage(file="icono.png")
#miImagen.place(x=200,y=0)

tituloPrincipal=Label(miFrame, text="PROYECTO ARQUITECTURA DE COMPUTADORES",fg="black",font=("Comic Sans MS",16))
tituloPrincipal.place(x=180,y=50)




#TODAS LAS ETIQUETAS

etiquetaVozATexto=Label(miFrame, text="1-Voz a texto",fg="black",font=("Comic Sans MS",12))
etiquetaVozATexto.place(x=20,y=160)

etiquetaBuscarArchivo=Label(miFrame, text="2-Abrir Archivo",fg="black",font=("Comic Sans MS",12))
etiquetaBuscarArchivo.place(x=20,y=200)

etiquetaOperaciones=Label(miFrame, text="3-Operaciones",fg="black",font=("Comic Sans MS",12))
etiquetaOperaciones.place(x=20,y=300)

#etiqueta donde salga el nombre del archivo
etiquetaTitulo=Label(miFrame, text="Titulo del PDF",fg="black",font=("Comic Sans MS",12))
etiquetaTitulo.place(x=600,y=120)


#TODAS LAS CAJAS DE TEXTO

#la mas pequeña
cajaTextoVozaTexto = Entry(miFrame)
cajaTextoVozaTexto.place(x=150,y=160)

#CAJA DE TEXTO(la mas grande de la derecha),como comentario
cajaTexto = tkinter.Text(miFrame)
cajaTexto.place(x=500,y=150,width=270,height=300)



#TODOS LAS BOTONES

# BOTON DEL MICRO 
botonMicro=Button(miFrame,text = 'Grabar !')
botonMicro.place(x=280,y=160) 

#BOTONES

botonPlay=Button(miFrame,text =     'Play !   ')
botonPlay.place(x=20,y=330) 

botonEliminar=Button(miFrame,text = 'Eliminar!')
botonEliminar.place(x=80,y=330) 

botonBuscar=Button(miFrame,text =   'Buscar!  ')
botonBuscar.place(x=140,y=330) 

botonListar=Button(miFrame,text =   'Listar!  ')
botonListar.place(x=200,y=330) 




#BOTON ABRIR ARCHIVOS
def test():
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
    fichero = filedialog.asksaveasfile(title="Guardar un archivo", mode="r+")
    if fichero is not None:
        fichero.write("Texto")
        fichero.close()

Button(miFrame, text="Click", command=test).place(x=150,y=200)

raiz.mainloop()


