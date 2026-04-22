# SIAP - Sistema Inteligente Asistente Perceptivo

Proyecto de visión artificial hecho para personas con discapacidad visual  que detecta objetos en tiempo real y los describe mediante voz.

## Funcionalidades
- Detección de objetos con YOLOv8
- Identificación de posición (izquierda, centro, derecha)
- Estimación de distancia
- Alertas de peligro
- Interacción por teclado

## Controles
- E - Escanear
- S - Detener
- Q - Salir

## librerias internas de python
- Time
- Threading
- queue

## Tecnologías
- Python (Version 3.10)
- OpenCV 
- pytorch
- YOLOv8 (Ultralytics)
- pyttsx3

## como crear un entorno virtual
Primero deben entrar dentro de Visual studio code y dentro del archivo .py del codigo una vez instalado python(3.10), y ejecutar esta serie de comandos.
- python -m venv siap-env
- siap-env\Scripts\Activate.ps1
deberian ver algo asi '(siap-env) C:\Users\diego\Desktop\SIAP>'

## como instalar las dependencias
Una vez instalado python (3.10), tienen que ir a Visual Studio Code y en la terminal dentro de env (entorno virtual), ejecutan cada uno de estos comandos

- pip install ultralytics
- pip install opencv-python
- pip install pyttsx3
- pip install torch
- pip install numpy

## Integrantes 

- DEVS:
    Lurgo Diego Andres, Santiago Mamani
- Hardware:
    Exequiel Naessens, Francisco Marazza, Matias Vigo
- Scrum Master:
    Rosario 

## Estado
- Funcionalidades basicas como deteccion y descripcion de objetos basicos, peligro de proximidad y direccion (izquierda, centro, derecha)

## Recomendaciones
- Usar y descargar todo en un entorno virtual (env)