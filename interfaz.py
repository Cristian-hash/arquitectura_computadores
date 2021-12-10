import tkinter 
ventana= tkinter.Tk()

#tamaño de la ventana
ventana.geometry("900x600")

#etiqueta TITULO y Posicion
etiqueta = tkinter.Label(ventana,text = "POSTCAST", bg="blue")
etiqueta.pack()



ventana.mainloop()