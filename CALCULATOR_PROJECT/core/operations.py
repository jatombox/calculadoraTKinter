# CALCULATOR_PROJECT/core/operations.py

class CalculatorLogic:
    """
    Clase que contiene la lógica de las operaciones matemáticas.
    Esto simula la separación de la lógica de negocio.
    """
    
    def __init__(self):
        pass # No se necesita estado interno para una calculadora simple

    def add(self, a, b):
        """Suma dos números."""
        return a + b

    def subtract(self, a, b):
        """Resta dos números."""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b

    def divide(self, a, b):
        """Divide dos números. Maneja la división por cero."""
        if b == 0:
            return "Error: División por cero"
        return a / b

    def calculate(self, expression):
        """
        Evalúa una expresión matemática simple.
        NOTA: Usar eval() es peligroso en producción, pero para este ejercicio
        de calculadora simple y modularidad, se usa para simplificar.
        """
        try:
            # Reemplazar símbolos para que eval() los entienda si es necesario
            # Aunque para +, -, *, / no es estrictamente necesario.
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error: División por cero"
        except Exception:
            return "Error de sintaxis"

# Ejemplo de uso (opcional)
if __name__ == '__main__':
    calc = CalculatorLogic()
    print(f"Suma: 5 + 3 = {calc.add(5, 3)}")
    print(f"División: 10 / 2 = {calc.divide(10, 2)}")
    print(f"División por cero: 10 / 0 = {calc.divide(10, 0)}")
    print(f"Expresión: 2 * (3 + 4) = {calc.calculate('2 * (3 + 4)')}")
