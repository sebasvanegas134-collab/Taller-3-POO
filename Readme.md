<img width="736" height="310" alt="LogoUNAL" src="https://github.com/user-attachments/assets/73744e6f-1a2d-4a8e-88e1-b6811630c9cc" />

Actividad: Exercises Activity 3 - Interfaces Gráficas y UML

Estudiante: Sebastian Vanegas Sanchez

Docente: Walter Hugo Arboleda Mazo 

# Taller Práctico: Interfaces Gráficas (GUI) y Arquitectura Orientada a Objetos en Python 

Este repositorio contiene la resolución de una serie de ejercicios prácticos enfocados en la integración de la Programación Orientada a Objetos (POO) con la creación de Interfaces Gráficas de Usuario (GUI) modernas. Cada aplicación está rigurosamente acompañada de su respectivo diseño arquitectónico modelado mediante diagramas UML (Clases, Casos de Uso y Objetos).

## Conceptos Aplicados
Durante el desarrollo de este taller se implementaron los siguientes conceptos técnicos y de diseño:
- **Desarrollo de GUI Backend/Frontend** utilizando las librerías `tkinter` y `ttk`.
- **Manejo de Excepciones Personalizadas** (`raise Exception`) para una validación estricta de la entrada de datos del usuario.
- **Herencia, Clases Abstractas y Polimorfismo** utilizando el módulo `abc` para definir contratos estructurales.
- **Diseño de Experiencia de Usuario (UX/UI)** interactivo, incorporando paletas de colores modernas, feedback visual (MessageBox) y animaciones de ventana responsivas.
- **Modelado Arquitectónico Completo** mapeando la lógica de código a diagramas de UML interactivos.

## Estructura de los Ejercicios

### Ejercicio 8.2 - Sistema de Análisis Estadístico de Notas
Desarrollo de una aplicación de escritorio con separación estricta entre la lógica de negocio (Backend) y la interfaz (Frontend). El sistema procesa un conjunto de 5 calificaciones para calcular dinámicamente el promedio, la desviación estándar, y los valores mayor y menor. 
Destaca por su sistema de validación robusto a través de excepciones personalizadas (`CamposVaciosError` y `NotaFueraDeRangoError`) y una interfaz fluida que incluye animaciones de redimensionamiento automático al arrojar resultados.

### Ejercicio 8.3 - Calculadora Geométrica 3D Polimórfica
Aplicación avanzada multi-ventana basada en el diseño de una jerarquía de clases abstractas. A partir de la clase base `Figura3D`, se derivan familias de figuras (Esferas, Cilindros, Pirámides, Cubos y Prismas).
El sistema aprovecha el **polimorfismo** para delegar los cálculos matemáticos (Volumen y Superficie) a las instancias correspondientes. Su interfaz gráfica implementa un menú principal que despliega ventanas secundarias (`Toplevel`) de forma modular, cada una equipada con representaciones visuales generadas a través del widget `Canvas`.

## 🛠️ Tecnologías y Herramientas
- **Lenguaje:** Python 3.x
- **Librerías Nativas:** `tkinter`, `math`, `abc`
- **Arquitectura de Software:** Modelado UML de Casos de Uso, Objetos y Clases (Diseñado con StarUML)