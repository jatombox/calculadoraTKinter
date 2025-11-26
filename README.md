# 💻 Calculadora Modular con Tkinter

## ✨ Autor
**Jacobo Morales Londoño**

---

## 🎯 Objetivo del Proyecto

Este proyecto implementa una **calculadora simple** con Interfaz Gráfica de Usuario (GUI) utilizando **Python** y la librería **Tkinter**. El diseño sigue una estricta **estructura modular** para garantizar la separación de la lógica de negocio y la presentación, tal como se solicitó.

## 📁 Estructura del Proyecto

La organización de los archivos se basa en un patrón modular, facilitando la escalabilidad y el mantenimiento:

CALCULATOR_PROJECT/
├── core/
│   ├── init.py
│   ├── operations.py  <-- 🧠 Lógica de la Calculadora
│   └── models/
│       └── init.py
├── main.py            <-- 🖥️ Interfaz Gráfica (GUI) y Punto de Entrada
└── README.md

### 🧱 Modularidad y Responsabilidades

| Archivo/Módulo | Responsabilidad Principal | Detalle de Implementación |
| :--- | :--- | :--- |
| **`core/operations.py`** | **Lógica de Negocio (Backend)** | Contiene la clase `CalculatorLogic` con métodos puros (`add`, `subtract`, `multiply`, `divide`) y un método `calculate` para evaluar expresiones. **Es independiente de la GUI.** |
| **`main.py`** | **Interfaz Gráfica (Frontend)** | Contiene la clase `CalculatorGUI` que construye la interfaz de Tkinter. **Importa** y utiliza la `CalculatorLogic` para realizar los cálculos, actuando como el **punto de entrada** de la aplicación. |
| **`core/models/`** | **Estructuras de Datos** | Se incluye para mantener la estructura modular solicitada. En proyectos más complejos (como un CRUD), contendría las clases de modelos de datos. |

---

## ▶️ Ejecución del Proyecto

El programa está diseñado para iniciarse automáticamente al ejecutar el archivo principal.

### Requisitos

Asegúrate de tener **Python 3** instalado. La librería **Tkinter** suele venir incluida con la instalación estándar de Python, pero en algunos sistemas Linux podría requerir una instalación adicional (ej: `sudo apt-get install python3-tk`).

### Pasos para Ejecutar

1.  Navega al directorio raíz del proyecto (`CALCULATOR_PROJECT`).
2.  Ejecuta el archivo principal `main.py` desde tu terminal:

```bash
python3 main.py

