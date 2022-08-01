# GUI - Graphical User Interface
# Tkinder
# Importamoa el modulo de tkinder
import Tkinder as tk

# creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600*400')
# Cambiamos el nombre de la ventana
ventana.title('Nueva Ventana')
# Iniciamos la ventana ( esta linea la ejecutamos al final)
# si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
