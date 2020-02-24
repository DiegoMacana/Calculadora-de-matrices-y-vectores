#DIEGO FERNANDO MACANA NARANJO - CNYT - MATRICES CON COMPLEJOS
import math
from sys import stdin
from Calculadora_de_Complejos import*
def crear_matriz(lista):
    matriz=[]
    f=int(stdin.readline())
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
    for i in range (int(len(d)/2)):
        k=(d[g],d[y])
        g=g+2
        y=y+2
        lista.append(k)
    return lista
def suma_de_vectores_complejos(A,B):
    h=list()
    for j in range (len(A[0])):   
        for i in range (len(A)):
            h.append(suma(A[i][j],B[i][j]))
    return h
def inversa_de_vectores_complejos(A):
    print (A)
    h=list()
    for j in range (len(A[0])):
        for i in range (len(A)):
            r=-(A[i][0][0])
            f=-(A[i][0][1])
            h.append((r,f))
            print (h)
    return h
def escalar_x_complejo(E,C):
    rr=E*(C[0])
    pp=E*(C[1])
    rta=(rr,pp)
    return rta
def suma_matrices(A,B):
    if len(A)!= len(B) and len(A[0]!=len(B[0])): # tienen que ser del mismo tamaño
        return print("matrices de diferente tamaño")
    else:
        d=[]

        for i in range (len(A)):
            d.append([])
            for j in range (len(A[0])):
                d[i].append(suma(A[i][j],B[i][j]))
    return d
def inversa_matriz(A):
    l=[]
    for i in range (len(A)):
        l.append([])
        for j in range (len(A[0])):
            f=-(A[i][j][0])
            j=-(A[i][j][1])
            l[i].append((f,j))
    return l
def esacalar_X_Mcompleja(E,M):
    h=[]
    for i in range (len (M)):
        h.append([])
        for j in range (len(M[0])):
            
            aux=E*(M[i][j][0])
            aux2=E*(M[i][j][1])
            h[i].append((aux,aux2))
    return (h)
        
def traspuesta_matriz_o_Vector(A):
    p=[]
    for i in range (len(A[0])):
        p.append([])
        for j in range (len(A)):
            p[i].append (A[j][i])
    return p
        
    
    
def conjugada (A):
    h=[]
    for i in range (len(A)):
        h.append([])
        for j in range(len (A[0])):
            h[i].append(conjugado(A[i][j]))
    return h
def adjunta_daga(A):
    A=conjugada(traspuesta_matriz_o_Vector(A))
    return S

def producto_AB(A,B):
    B=traspuesta_matriz_o_Vector(B)
    if (len(A)!= len(B)) and (len(A[0])!=len(B[0])): # tienen que ser del mismo tamaño
        return print("ERROR: matrices de diferente tamaño")
    else:
        d=[]
        for i in range (len(A)):
            d.append([])
            for j in range (len(A[0])):
                aux=(0,0)
                for y in range (len(A)):
                    aux=suma(multiplicar(A[i][y],B[j][y]),aux)
                    #print(A[i][y],"y",B[i][y])
                    #print ("resultado:",aux)
                    
                #print ("agrego")
                d[i].append(aux)
        
                """prueba:
1 0 -2 0 -3 0 0 0 2 0 -3 0 0 0 0 0 3 0
3
3
5 0 0 0 0 0 4 0 -3 0 0 0 -2 0 1 0 5 0
3
3
"""
    return d
def distancia(A,B):
    t=(B[0]-A[0])*(B[0]-A[0])
    s=((B[1]-A[1])*(B[1]-A[1]))
    rta=math.sqrt((t+s))
    return rta
def prod_interno(A,B):
    t=producto_AB(A,B)
    li=[]
    for i in range (len(t)):
        for j in range (len(t)):
            if i==j:
                li.append(t[i][i])
    return (li)
def norma(A):
    aux=0
    for i in range (len(A)):
        aux=modulo(multiplicar(A[i][0],A[i][0]))
    return(aux)
def es_hermitaria(A):
    aux=0
    ref=A[0][0][0]
    for i in range (len(A)):
        for j in range (len(A)):
            if i==j and A[i][j][0]==ref:
                aux=aux+1            
    if aux==len(A):
        return 0#"es hermitaria"
    else:
        return 1#" no es hermitaria"
def es_unitaria(A):
    t=traspuesta_matriz_o_Vector(A)
    h=inversa_matriz(A)
    if t==h:
        return 0#"es unitaria"
    else:
        return 1#"no es unitaria"
def producto_tensor(A,B):
    filas=len(A)*len(B)
    columnas=len(A[0])*len(B[0])
    print (len(A)*len(B))
    print(len(A[0])*len(B[0]))
    print (A[0][0][0])
    r=[]
    for i in range (len(A)):
        for j in range (len(A[0])):
            for k in range (len(B)):
                for s in range (len(B[0])):
                    r.append(A[i][j][0]*B[k][s][0])
    rta=[]
    conta=0
    for i in range (filas):
        rta.append([])
        for j in range (columnas):
            rta[i].append (r[conta])
            conta=conta+1
    for i in (rta):
        print (i)
    
            
"""            
def main():
    global S
    S=[[(1.0, 2.0), (1.0, 2.0)], [(1.0, 2.0), (1.0, 2.0)]]
    lista=crear_lista_tuplas()
    z=crear_matriz(lista)
    lista2=crear_lista_tuplas()
    x=crear_matriz(lista2)
    print("1ra matriz")
    for i in (z):
        print (i)
    print("2da matriz: ")
    for i in (x):
        print (i)
    print("z:",z)
    print("x:",x)
    print("rta: ",es_unitaria(z))
    print(adjunta_daga(z))
    print(es_hermitaria(z))
    print ("inversa")
    g=inversa_matriz(z)
    for i in (g):
        print (i)
    print("suma:")
    j=(suma_matrices(z,g))
    for i in (j):
        print (i)
    print ("escalar por Matriz compleja:")
    yy=esacalar_X_Mcompleja(3,z)
    for i in (yy):
        print (i)
    print ("conjugado:")
    kk=conjugada(z)
    print (kk)
    for i in (kk):
        print (i)
    print ("producto A B :")
    prod=producto_AB(z,x)
    for i in (prod):
        print (i)
    yyyy=distancia((1,-2),(3,4))
    print(yyyy)
    prod_interno(z,x)
    print ("norma :")
    norma (z)
main()
  
 casos de prueba:
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
