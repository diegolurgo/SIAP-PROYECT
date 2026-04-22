from ultralytics import YOLO #esta es nuestra base de todo
import cv2 #vision por computadora
import pyttsx3
import time
import threading
import queue

escanear = False #esto escanea el entorno

ultimo_habla = 0 #esto es para cuando dice la ultima palabra

cola_voz = queue.Queue()

ultimo_scan = 0 #esto es para el ultimo scan

ultimo_peligro = False #esto es para detectar peligro
peligro_detectado = False #esto es para el peligro que detecta

frame_count = 0 #esto cuenta frame x frame
results = None #estos son los resultados

#importacion de las primeras bases del codigo

model = YOLO("yolov8n.pt").to("cuda") #carga del modelo de yolo
cap = cv2.VideoCapture(0) #esto es el capture video 


#este es el hio de voz
def hablar(texto): #defino funcion que simplifica codigo en la carga de tts el cual genera problemas
    def _hablar():
        engine = pyttsx3.init() 
        engine.say(texto) #esto llama a tts dirigido al texto
        engine.runAndWait()
    threading.Thread(target=_hablar).start()

#ahora va el mensaje inicial
hablar("Hola, bienvenido a SIAP, Presiona la tecla E para escanear el entorno")

ultimo_objeto = []

cap.set(3, 640) #esto es resolucion de pantalla
cap.set(4, 480)

#aqui empieza el programita
while True:
    ret, frame = cap.read() #esto lee la captura de imagen
    if not ret:
        break
    
    frame_count += 1 #esto cuenta frame x frame, lo suma y lo guarda
    
    #esto va a hacer que muestre siempre
    if escanear and results is not None:
        annotated_frame = results[0].plot()
        cv2.imshow("SIAP - Detecta", annotated_frame)
    else:
        cv2.imshow("SIAP", frame)
    
    
    #esto es el escaneo
    if escanear and frame_count % 2 == 0:
        results = model(frame, conf = 0.3) #esto es para que escanee y cuente los frames, conf es para optimizar
        
        objetos_detectados = []
        
        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0]) #esto es lo que detecta y lo manda a resultados
                label = model.names[cls]
                #esto es para direccion 
                if label in ["person", "chair", "dining table", "bottle", "cell phone", "dog", "cat"]: #estos son los objetos que puede detectar
                    x1, y1, x2, y2 = box.xyxy[0].tolist() #estas son las direcciones que detecta
                    centro_x = (x1 + x2) / 2
                    area = (x2 - x1) * (y2 - y1)
                    ancho = frame.shape[1]
                    #estas son las direcciones
                    if centro_x < ancho / 3:
                        posicion = "izquierda"
                    elif centro_x < 2 * ancho / 3:
                        posicion = "centro"
                    else:
                        posicion = "derecha"
                    
                    if area > 50000:
                        distancia = "cerca"
                    elif area > 20000:
                        distancia = "a media distancia"
                    else:
                        distancia = "lejos"
                        
                    #esto es la deteccion de peligro
                    if posicion == "centro" and distancia == "cerca":
                        peligro_detectado = True
                    #traduccion
                    traducciones = { #esto es mera traduccion, no mucho mas
                        "person" : "persona",
                        "chair" : "silla",
                        "dining table" : "mesa",
                        "bottle" : "botella",
                        "cell phone" : "telefono",
                        "dog" : "perro",
                        "cat" : "gato"
                    }
                    
                    label_es = traducciones.get(label, label) #esto toma la variable label y la traduce
                    descripcion = f"hay una {label_es} en el {posicion} {distancia}" #esto es la descripcion
                    objetos_detectados.append(descripcion)
                    
                    print("Detectando crudo:", label) #esto es solo de prueba
                    
        objetos_detectados = list(set(objetos_detectados))

        #esta es la prioridad
        
        objetos_detectados.sort(key = lambda x: 0 if "persona" in x else 1) 
        objetos_detectados = objetos_detectados[:2]
        
        #aqui habla
        print("OBJETOS: ", objetos_detectados)
        if objetos_detectados and time.time() - ultimo_habla > 3:
            print("detectado: ", objetos_detectados)
            for item in objetos_detectados:
                hablar(item)
            ultimo_habla = time.time()
            
            ultimo_objeto = objetos_detectados.copy()
        
        #esto es la alerta
        if peligro_detectado and not ultimo_peligro:
            hablar("cuidado, tenes algo muy cerca enfrente")
        ultimo_peligro = peligro_detectado
        peligro_detectado = False
        

    #esto es para las teclas

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord("e") and time.time() - ultimo_scan > 2:
        escanear = True
        ultimo_scan = time.time()
        hablar("Escaneando entorno")
    if tecla == ord("s"):
        escanear = False
        hablar("deteniendo")
    if tecla == ord("q"):
        break
    
    time.sleep(0.01)
    
cap.release()
cv2.destroyAllWindows() #esto cierra todos los procesos de cv2 que esten usandose en windows para no dejar procesos activos