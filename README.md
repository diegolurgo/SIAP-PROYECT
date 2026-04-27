# SIAP - Sistema Inteligente Asistente Perceptivo

Proyecto de visión artificial hecho para personas con discapacidad visual que detecta objetos en tiempo real y los describe mediante voz, esto permitira que muchas personas puedan solucionar muchos problemas en la vida cotidiana facilitando su movilidad y confianza al cruzar esta incertidumbre.

## Comienzo del proyecto

Para poder utilizar el codigo deberan descargar todo lo dejado en el apartado GITHUB donde podran observar actualizaciones constante del codigo, de tal manera que ustedes tambien podran actualizarlo paso por paso, para poder hacer esto deberan realizar los siguientes pasos

1 - Tendran que descargar git en la pagina oficial: https://git-scm.com/install/

2 - Ejecutar los comandos correctos para la actualizacion del codigo, este mismo lo suben a github con los siguientes comandos (deben ejecutar la git bash o consola de git desde la carpeta del proyecto):

- git add (nombre.py o nombre.md dependiendo de lo que modifiquen)

- git commit -m "(descripcion de los cambios realizados de forma detallada pero breve)"

- git push

Luego para utilizar el codigo correctamente deberan descargar las dependencias del codigo donde podran ejecutar comandos, algoritmos y funciones en base a las librerias utilizadas para el proyecto, las cuales son:

- YOLOV8 (Ultralytics)
- OpenCV python (cv2)
- torch
- pyttx3 (text - to - speech)

Podran investigar sobre las mismas en los siguientes enlaces:

- YOLOV8: https://docs.ultralytics.com/models/yolov8/
- OpenCV: https://pypi.org/project/opencv-python/
- torch: https://pypi.org/project/torch/
- pyttsx3: https://pypi.org/project/pyttsx3/

## Prerequisitos

Para poder utilizar las librerias ya habladas sera necesario que las descarguen dentro de un entorno virtual (env), las instrucciones para descargar y usar las mismas son(cabe aclarar que es fundamental utilizar la version de python 3.10):

1 - Entorno virtual (ejecutar los siguientes comandos dentro de la consola del codigo, osea en visual studio code)

- python -m venv siap-env
- siap-env\Scripts\activate.ps1

Deberia aparecerles algo asi "(siap-env) C:\Users\diego\Desktop\SIAP"

2 - Instalar las librerias utilizadas (utilizar los siguientes comandos dentro de visual studio code en la env)

- pip install ultralytics
- pip install opencv-python
- pip install pyttsx3
- pip install torch
- pip install numpy

Cabe aclarar que para que estos comandos funcionen, deberan tener instalada la version de python 3.10 que podran descargarla desde: https://www.python.org/downloads/

## Testeo del proyecto

Los testeos del proyectos se realizaran durante y al final de cada sprint, de esta manera llevaremos una dinamica constante y podremos ver errores y realizar correcciones de una manera mas flexible

## Expresiones de gratitud

- Da las gracias siempre
- Llevate bien con tus companieros de equipo
- Comunicate siempre, si no entiendes algo, alguien te ayudara
- Trabaja en equipo, no estas solo
- consulta siempre los cambios y actualiza a tu equipo

## Integrantes del proyecto

SOFTWARE DEVS:

- Diego Lurgo
- Santiago Mamani

HARDWARE DEVS:

- Exequiel Naessens
- Francisco Marazza
- Matias Vigo

SCRUM MASTER / PRODUCT OWNER:

- Rosario Ocampo

## Estado actual del proyecto

- Funcionalidades basicas como deteccion y descripcion de objetos basicos, peligro de proximidad y direccion (izquierda, centro, derecha)