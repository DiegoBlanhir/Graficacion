""" Practica 3 Archivo Numerico """

# En esta practica haremos que la tortuga lea una matriz y moverla a la coordenada correspendiente y pintar del color asignado.

from turtle import * # Importamos la libreria de la tortuga

filename= "foto.txt" # Leeremos el archivo txt donde tenemos la matriz de 100x100

colores={ # Hacemos nuestra paleta de colores
    '0': "black",
    '1': "white",
    '2': "green",
    '3': "blue",
    '4': "red",
    '5': "yellow",
    '6': "purple",
    '7': "orange",
    '8': "pink",
    '9': "brown"
}

def lee_archivo(): # Hacemos una funcion para leer el archivo
    filename = "foto.txt"
    matriz = []
    for line in open(filename): # Abrimos el archivo y se recorre linea por linea
        seq = line.split() # Se separan las lineas
        fila = [c for c in seq[0]] # Esto no recuerdo para que era pero lo puso el profe y si sirvio
        matriz.append(fila)
    return matriz

matriz= lee_archivo() # Llamamos a la funcion para sacar la matriz
filas= len(matriz)
columnas= len(matriz[0]) if filas>0 else 0

penup() # Levantamos la tortuga para que no deje lineas
PIXEL=2 #tamaño del pixel porque si lo dejamos en 1 ni se alcanza a ver
inicio_x = -50 # En que eje de X queremos que inicie
inicio_y = 50 # En que eje de Y queremos que inicie

# Con esta si me ayudo chatgpt porque no tenia ni idea de como hacerle, pero me explico cada cosa
for y in range(filas): # Es para recorrer todas las filas
    for x in range(columnas): # Y este para todas las columnas
        color = colores.get(matriz[y][x], "white") # Este busca el color dependiendo el numero en la matriz
        goto(inicio_x + x * PIXEL, inicio_y - y * PIXEL) # Este mueve la tortuga a la posicion deseada
        dot(PIXEL, color) # Y este dibuja el punto del tamaño y el color que le toca

mainloop() # Lo dejamos abierto para ver nuestra obra