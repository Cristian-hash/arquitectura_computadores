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
Label(miFrame,image=miImagen).place(x=5,y=5)

#------------------------------------------------------------------
#miImagen=PhotoImage(file="icono.png")
#miImagen.place(x=200,y=0)


tituloPrincipal=Label(miFrame, text="PROYECTO ARQUITECTURA DE COMPUTADORES",fg="black",font=("Comic Sans MS",18))
tituloPrincipal.place(x=100,y=0)


#TITULO
etiquetaTitulo=Label(miFrame, text="Nombre del Archivo",fg="black",font=("Comic Sans MS",12))
etiquetaTitulo.place(x=600,y=120)

etiquetaBuscarArchivo=Label(miFrame, text="Abrir Archivo",fg="black",font=("Comic Sans MS",12))
etiquetaBuscarArchivo.place(x=20,y=160)
#CAJA DE TEXTO,como comentario
cajaTexto = tkinter.Text(miFrame)
cajaTexto.place(x=500,y=150,width=270,height=300)


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

Button(miFrame, text="Click", command=test).place(x=180,y=160)

raiz.mainloop()


