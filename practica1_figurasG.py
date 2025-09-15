""" PRACTICA 1 APRENDIENDO A USAR TURTLE """

# El objetivo de esta practica es hacer figuras basicas con la libreria turtle para ir conociendo como funciona

from turtle import *

penup() # Este es para levantar la tortuga y no dibuje una linea atravesada hasta el punto de inicio
forward(-300) # Estos son los pasos que dara sin dibujar para llegar a la posicion que yo quiera
left(90)
forward(200)
pendown() # Este es para bajar la tortuga y que ahora si empiece a dibujar

color('blue') # Este es para darle color a la tortuga
forward(100) #Estos son los pasos que da para cada lado, define el tamaño de los lados, se haran 4
right(90) # Como quiero formar un cuadrado ocupo que sean giros de 90 grados, se haran 3
forward(100)
right(90)
forward(100)
right(90)
forward(100)

penup() # Volvemos a levantar a la tortuga para pasarnos a otro lado de la hoja sin hacer lineas
right(180) # Lo mevemos 180 grados para que no se salga de la pantalla por la posicion en la que termino el cuadrado
forward(600) # Caminamos unos 600m pasos para inros a otro lado de la hoja para hacer la siguiente figura
pendown() # Bajamos a la tortuga para que dibuje

color('red') # Le ponemos otro color
forward(100) # Este es para el primer lado del triangulo
left(120) # Para el triangulo equilatero ocupamos hacer que gire 120 grados cada que dibuje un lado
forward(100)
left(120)
forward(100)
left(30) # Para dejarlo en 270 grados y mandarlo para abajo a la siguiente figura

penup() # Lo volvemos a levantar para que no dibuje lineas entre las figuras
forward(300) # Lo mandamos a la esquina de abajo a la derecha
pendown() # Lo bajamos para que siga dibujando

color('green') # Le damos otro color para dibujar
i=0 # Definimos una variable para no usar la funcion circle porque no le gusta al profe
while i<361: # Como el circulo tiene 360 grados tiene que ser menor de 361 para que termine el ciclo
    forward(1) # Aqui solo dara un paso
    left(1) # Y cada que de un paso girara un grado a la izquierda
    i = i + 1 # Y asi hasta que se termine el ciclo, osea cuando esten 360 pixeles lo que termina formando un circulo mas bonito que el circle pero mucho mas lento lol

penup() # Levantamos nuevamente la tortuga
right(91) # La giramos 91 grados para mandarla a la esquina inferior izquierda, con 90 no terminaba quedando derecho
forward(300) # Que camine para llegar
pendown() # Que baje para seguir dibujando

color('black') # Le damos un ultimo color
forward(200) # Dibujamos solo una linea recta