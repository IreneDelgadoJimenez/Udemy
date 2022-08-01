import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400*450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo ultilizamos para obtener el valor del input
        self.entrada_texto = tk.stringVar()
        # Creamos los componentes
        self._creacion_componentes()
    # Metodos de clase
    # Metodo para crear los componentes#
    def _creacion_componentes(self):
        # Creamos un frame para ver la caja de texto
         entrada_frame = tk.Frame(self,width=400)





if __name__ == '__main__':
    calculadora = Calculadora
    calculadora.mainloop()

