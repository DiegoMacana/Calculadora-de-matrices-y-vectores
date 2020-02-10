#DIEGO FERNANDO MACANA NARANJO COMPUTO CNYT MATRICES CON COMPLEJOS
"""
Complete su librería con operaciones para vectores, matrices

La librería debe incluir las siguientes operaciones:

Adición de vectores complejos.
Inverso (aditivo) de un vector complejo.
Multiplicación de un escalar por un vector complejo.
Adición de matrices complejas.
Inversa (aditiva) de una matriz compleja.
Multiplicación de un escalar por una matriz compleja.
Transpuesta de una matriz/vector
Conjugada de una matriz/vector
Adjunta (daga) de una matriz/vector
Producto de dos matrices (de tamaños compatibles)
Función para calcular la "acción" de una matriz sobre un vector.
Producto interno de dos vectores
Norma de un vector
Distancia entre dos vectores
Revisar si una matriz es unitaria
Revisar si una matriz es Hermitiana
Producto tensor de dos matrices/vectores
"""
import math
from sys import stdin
from Calculadora_de_Complejos import*

def crear_matriz(lista):
    matriz=[]
    #f=int(input("digite el tamaño de las filas: "))
    f=int(stdin.readline())
    #c=int(input("digite el tamaño de las columnas: "))
    c=int(stdin.readline())
    r=0
    for i in range(c):
        matriz.append([])
        for j in range(f):
            matriz[i].append(lista[r])
            r=r+1      
    return (matriz)
def crear_lista_tuplas():
    d=list(map(float,stdin.readline().split()))
    g=0
    y=1
    lista=[]
    #print(d)
    for i in range (int(len(d)/2)):
        k=(d[g],d[y])
        g=g+2
        y=y+2
        lista.append(k)
    return lista

def suma_de_vectores_complejos(A,B):
    h=list()
    for j in range (len(A)):
        for i in range (len(A[0])):
            h.append(suma(A[i][j],B[i][j]))
    print(h)
    return h
def inversa_de_vectores_complejos(A):
    h=list()
    for j in range (len(A)):
        for i in range (len(A[0])):
            h.append(inversa(A[i][j]))
    print(h)
    return h

"""def main():
    lista=crear_lista_tuplas()
    z=crear_matriz(lista)
    lista2=crear_lista_tuplas()
    x=crear_matriz(lista2)
    #print(z)
    print("1ra matriz")
    for i in (z):
        print (i)
    print("2da matriz: ")
    for i in (x):
        print (i)
    print()
    #print(len(z[0])*len(z))
    print ((z[1][0]))
    rta=crear_matriz(suma_de_vectores_complejos(z,x))
    print("esta es una solucion:")
    for i in (rta):
        print (i)
    rta2=crear_matriz(inversa_de_vectores_complejos(z))
    print("esta es una solucion de inverso:")
    for i in (rta2):
        print (i)
    #print(z[1])
    #prettyPrinting(z[1])
    #print("esto es una suma",suma(z[0],z[1]))
    #for i in range (1,c):
    #d=crear_lista_tuplas()
    #print(d)
    """
""" casos de prueba:
1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
2
2
1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
2
2



6 -4 7 3 4.2 -8.1 0 -3
1
4
16 2.3 0 -7 6 0 0 -4
1
4
"""
    
#main()
