# Calculadora-de-matrices-y-vectores
Este proyecto fue diseñado por DIEGO FERNANDO MACANA NARANJO en el lenguaje Python. Para la materia CNYT (Ciencias Naturales Y Tecnología). Es una libreria que opera matrices y vectores complejos.

![Captura1](https://user-images.githubusercontent.com/59974540/75197864-36a2b880-572d-11ea-9d32-c406db6710bd.PNG)
![Captura2](https://user-images.githubusercontent.com/59974540/75197865-36a2b880-572d-11ea-90e4-b44989ef10f5.PNG)
![Captura3](https://user-images.githubusercontent.com/59974540/75197858-35718b80-572d-11ea-9f58-1aa76603f8c2.PNG)
![Captura4](https://user-images.githubusercontent.com/59974540/75197861-360a2200-572d-11ea-9767-3a1028831b0b.PNG)
![Captura5](https://user-images.githubusercontent.com/59974540/75197863-360a2200-572d-11ea-8933-0034af3554f5.PNG)

ESTE PROYECTO CONSTA DE 17 FUNCIONES
1. crear_matriz(lista): esta funcion me ayudo bastante a la hora de crear las matrices o los vectores de numeros complejos, reciviendo como parametro una lista de numeros, lo cual posteriormente las cambia a duplas de complejos y las organiza segun como se lo pida.
2.crear_lista_tuplas(): es un complemento de la matriz que acabe de nombrar atras. 
AHORA SI ENTRANDO EN TEMA :
1. suma_de_vectores_complejos(A,B): es una funcion que me ayuda a sumar dos vectores complejos, reciclando la funcion suma_de_complejos de la anterior libreria. 
2. inversa_de_vectores_complejos(): recive un vector e intercambia sus valores por negativo, dando solucion a la inversa del vector.
3. escalar_x_complejo(): multiplica un numero entero dado por una expresion imaginaria. 
4.  suma_matrices(): suma dos matrices de igual tamaño con datos complejos, usando de nuevo la libreria anteriormente usada. 
5. inversa_matriz(): Cambia los valores de una matriz por su correspondiente negativo.
6.esacalar_X_Mcompleja():en esta funcion el escalar esta vez multiplicara a cada elemento de una matriz.
7.  traspuesta_matriz_o_Vector(): Transpone a una matriz o vector,  muy util a la hora de multiplicar o hacer otras funciones. 
8. conjugada: cambia los elementos imaginarios por su inverso aditivo. 
9. adjunta_daga(): una funcion que usa la funcion de conjugada y la de transpuesta para crear esta nueva matriz. 
10. Producto_AB(): nos retorna los valores propios de una matriz, usando un condicional que informa error al entrar una matriz no cuadrada.
11. distancia(A,B): usando el algebra basica, hayamos la distancia entre dos puntos, usando el teorema de pitagoras, pero al ser ezpresiones imaginarias, usamos la anterior libreria para ayudarnos. 
12. prod_interno: Nos retorna los valores que se multiplican o se suman en su diagonal, usando la funcion producto(A,B) definida en la enterir libreria. 
13. norma(A) : la norma de una matriz o vector sera el modulo de la multipliacion de los cuadrados de la expresion. 
14. es_hermitaria(A):Siguiendo las reglas de la definicion de Hermitario, adapto los condicionales necesarios para saber si una matriz es hermitaria o no lo es, como es una pregunta de si/No entonces retorna un 0  si es hermitaria o un 1 si no lo es. 
15. es_unitaria(): Es una funcion que sigue las normas para que una expresion sea unitaria e identifica si una matriz lo es, o no. 
16. producto_tensor(): Es una funcion muy complicada de hacer, aun sigue en proceso, por ahora supongo que me ayudare con la funcion de tensor de Numpy. 

Adjunto los test que se realizaron en el proyecto :


![Captura22](https://user-images.githubusercontent.com/59974540/75199533-5fc54800-5731-11ea-855e-56e0149f1b44.PNG)
![Captura33](https://user-images.githubusercontent.com/59974540/75199536-605dde80-5731-11ea-8e49-cb9e3c0db700.PNG)

