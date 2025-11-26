# Calculadora Modular con Tkinter

Este proyecto implementa una calculadora simple con interfaz gráfica (GUI) utilizando **Python** y **Tkinter**, siguiendo una estricta **estructura modular** basada en el patrón de directorios solicitado.

## Estructura del Proyecto

La estructura de directorios sigue el patrón de la imagen, adaptado para una aplicación de calculadora:

```
CALCULATOR_PROJECT/
├── core/
│   ├── __init__.py
│   ├── operations.py  <-- Lógica de la calculadora
│   └── models/
│       └── __init__.py
├── main.py            <-- Interfaz Gráfica (GUI) y punto de entrada
└── README.md
```

### Modularidad y Responsabilidades

| Archivo/Módulo | Responsabilidad | Detalle de Implementación |
| :--- | :--- | :--- |
| **`core/operations.py`** | **Lógica de Negocio** | Contiene la clase `CalculatorLogic` con métodos puros para las operaciones (`add`, `subtract`, `multiply`, `divide`) y un método `calculate` para evaluar expresiones. |
| **`main.py`** | **Interfaz Gráfica (GUI)** | Contiene la clase `CalculatorGUI` que construye la interfaz de Tkinter y maneja los eventos de los botones. **Importa** y utiliza la `CalculatorLogic` de `core/operations.py`. |
| **`core/models/`** | **Estructuras de Datos** | En un proyecto CRUD, contendría las clases de modelos de datos. En este caso, se mantiene la estructura para cumplir con el patrón, pero no se utiliza activamente. |

## Ejecución del Proyecto

El programa está diseñado para funcionar al ejecutar el archivo principal, `main.py`.

1.  **Asegúrate de tener Tkinter instalado** (generalmente incluido con Python, pero puede requerir `sudo apt-get install python3-tk` en algunos sistemas Linux).
2.  Navega al directorio `CALCULATOR_PROJECT`.
3.  Ejecuta el archivo principal:

```bash
python3 main.py
```

Al ejecutar `main.py`, se inicializa la interfaz gráfica y se crea una instancia de la lógica de la calculadora, demostrando la correcta separación y modularidad del código.
