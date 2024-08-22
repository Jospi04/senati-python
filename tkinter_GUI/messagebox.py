# Importamos el TKINTER
import tkinter as tk
# Importamos los messabox
from tkinter import messagebox
# Importamos un modulo del archivo principal y usar todo
from modulos.principal import *
# Creamos una funcion para mostar mensajes
def mensajeInfo():
    messagebox.showinfo("Mensaje","Esto es un mensaja de info")
def mensajeError():
    messagebox.showerror("Mensaje","Esto es un error")
def mensajeAdvertencia():
    messagebox.showwarning(title ="Mensaje",message="pipi")
    ventana.destroy()
    abrirVentanaPrincipal()
    
# Inicializamos la clase TK()
ventana = tk.Tk()
# Menciono el nombre de la ventana
ventana.title("Senati")
# Icono de ventana
ventana.iconbitmap("icons/favicon.ico")
# Tamaño de la ventana
ventana.geometry("350x450")
# El usuario no permite modificar la ventana
ventana.resizable(False,False)
#agregando botones
boton1 =tk.Button(ventana, text="Info", width=10,height=5, command= mensajeInfo)
boton1.grid(row=0,column=0,padx=50,pady=30)
boton2 =tk.Button(ventana, text="Error", width=10,height=5, command= mensajeError)
boton2.grid(row=0,column=1,padx=50,pady=30)
boton3 =tk.Button(ventana, text="Advertencia", width=10,height=5, command=mensajeAdvertencia)
boton3.grid(row=1,column=0,padx=50,pady=30)
boton4 =tk.Button(ventana, text="B4", width=10,height=5)
boton4.grid(row=1,column=1,padx=50,pady=30)
# Color del fondo de la ventana
ventana.config(bg="#0859aa")
# Transparencia
ventana.wm_attributes("-alpha",0.9)
# Mantener la ventana abierta

ventana.mainloop()