"""Practica 2 Mover una figura con el teclado"""

#El objetivo es hacer un cuadrado o circulo y conseguir que este se mueva con las flechas del teclado

from turtle import * # Usamos turtle para los graficos

color("red") # Le damos un color a la tortuga
shape("square") # Intente con el circle o hacer el cuadrado como lo hicimos en clase pero no funciono con ninguno, internet y chat me dieron este y con este si funciono, a es la figura
penup() # Levantamos a la tortuga para que no deje rastro por donde va pasando

def izquierda(): # Definimos la variable con la que lo moveremos a la izquiera
    x = xcor() # Se movera en las cordenadas del eje X
    setx(x - 1) # Y este valor le quita 1 a X, pero se puede poner el valor que sea para que se mueva mas o menos lento

def derecha(): # Definimos la variable con la que lo moveremos a la derecha
    x = xcor()# Tambien se movera en las cordenadas del eje X
    setx(x + 1) # Ahora en vez de restarle 1 a X, se lo sumaremos

def arriba(): # Definimos la variable con la que lo moveremos a arriba
    y = ycor() # Ahora este se movera en las cordenadas del eje Y
    sety(y + 1) #   Como es para arriba le sumamos 1 a Y

def abajo(): # Definimos la variable con la que lo moveremos a abajo
    y = ycor() # Tambien lo meveremos en el eje Y
    sety(y - 1) # Pero ahora le restamos 

listen()
onkeypress(izquierda, "Left") # Este es para mover la tortuga a la izquierda
onkeypress(derecha, "Right") # Este es para mover la tortuga a la derecha
onkeypress(arriba, "Up") # Este es para mover la tortuga a la arriba
onkeypress(abajo, "Down") # Este es para mover la tortuga a la abajo

mainloop() # Y este es para que no se cierre el programa

# Busque en internet y en el documento de turtle lo de la figura,ero chat me dio un ejemplo con el shape, y con ese si funciono, grande chat