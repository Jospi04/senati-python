# Importamos el tkinter
import tkinter as tk #Alias al Tkinter

def abrirVentanaPrincipal():
    ventana2 =tk.Tk()
    ventana2.title("Sistema Principal")
    ventana2.geometry("500x700")
    ventana2.resizable(False,False)
    
#Creando las variables
    numTarjeta = tk.StringVar()
    codigo= tk.StringVar()

# creando la esrtuctura
    label_n_tarjeta = tk.Label(ventana2, text="N° Tarjeta", font =("Arial",15,"bold"))
    label_n_tarjeta.grid(row=0,column=0,padx=80,pady=10)
    label_n_codigo = tk.Label(ventana2, text="Codigo", font =("Arial",15,"bold"))
    label_n_codigo.grid(row=0,column=1,padx=80,pady=10)
# Creando la estructura parte 02
    txtTarjeta = tk.Entry(ventana2,textvariable=numTarjeta,font =("Arial",12))
    txtTarjeta.grid(row=1,column=0,padx=10)
    txtCodigo= tk.Entry(ventana2,textvariable=codigo,font =("Arial",12))
    txtCodigo.grid(row=1,column=1,padx=10) 
    
# Creando la estructura parte 03

    label_n_calcular = tk.Label(ventana2, text="CALCULAR", font =("Arial",15,"bold"))
    label_n_calcular.grid(row=2,column=0,padx=80,pady=10)
    txtcalcular = tk.Entry(ventana2,textvariable=label_n_calcular,font =("Arial",12))
    txtcalcular.grid(row=3,column=0,padx=10)

    ventana2.mainloop() # Poner siempre al ultimo

abrirVentanaPrincipal()