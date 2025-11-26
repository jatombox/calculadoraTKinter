# CALCULATOR_PROJECT/main.py

import tkinter as tk
from tkinter import ttk
from core.operations import CalculatorLogic

class CalculatorGUI:
    """
    Clase que representa la Interfaz Gráfica de la Calculadora.
    """
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Modular (Tkinter)")
        
        # Instancia de la lógica de la calculadora
        self.logic = CalculatorLogic()
        
        # Variable para almacenar la expresión actual
        self.current_expression = ""
        
        # Configuración de la pantalla de visualización
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(master, textvariable=self.display_var, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
        
        # Definición de los botones
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0) # Botón de limpiar
        ]
        
        # Creación de los botones
        for (text, row, col) in buttons:
            if text == '=':
                button = ttk.Button(master, text=text, command=self.calculate_result)
            elif text == 'C':
                button = ttk.Button(master, text=text, command=self.clear_display)
            else:
                button = ttk.Button(master, text=text, command=lambda t=text: self.button_click(t))
            
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            
        # Configuración de la expansión de la cuadrícula
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, text):
        """Maneja el clic en los botones numéricos y operadores."""
        self.current_expression += text
        self.display_var.set(self.current_expression)

    def clear_display(self):
        """Limpia la pantalla y la expresión actual."""
        self.current_expression = ""
        self.display_var.set("")

    def calculate_result(self):
        """
        Calcula el resultado de la expresión actual utilizando la lógica modular.
        """
        try:
            # Usamos el método calculate de la lógica
            result = self.logic.calculate(self.current_expression)
            
            # Mostrar el resultado
            self.display_var.set(str(result))
            
            # Preparar para la siguiente operación
            if "Error" not in str(result):
                self.current_expression = str(result)
            else:
                self.current_expression = ""
                
        except Exception as e:
            self.display_var.set("Error")
            self.current_expression = ""

if __name__ == '__main__':
    # El programa funciona cuando se ejecuta el main.py
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
