#Calculadora de Numeros complejos
#Estudiante: Diego Fernando Macana Naranjo

import math
     
def suma(A,B):
    #print ("(",A[0],"+",A[1],"i) + (",B[0],"+",B[1],"i)  = ","(",A[0],"+",B[0],") + (",A[1],"+",B[1],")i")    
    r=A[0]+B[0]
    c=A[1]+B[1]
    #if r==0:
    #   print("=",c,"i")
    #else:
    #   print ("=",r," + ",c,"i")
    f=(r,c)
    return (f)
def resta(A,B):
    #print ("(",A[0],"+",A[1],"i) - (",B[0],"+",B[1],"i)  = ","(",A[0],"-",B[0],") + (",A[1],"-",B[1],")i")    
    r=A[0]-B[0]
    c=A[1]-B[1]
    #if r==0:
    #    print("=",c,"i")
    #else:
    #    print ("=",r," + ",c,"i")
    f=(r,c)
    return(f)
        
def multiplicar(A,B):
    x=(A[0]*B[0])
    y=(A[1]*B[1])
    ff=x-y
    w=(A[0]*B[1])
    z=(A[1]*B[0])
    gg=w+z
    #print("=",ff,"+",gg,"i")
    f=(ff,gg)
    return (f)
    
def dividir(A,B):
    conjugado=B[1]*-1
    q=(A[0]*B[0])
    w=(A[0]*conjugado)
    e=(A[1]*B[0])
    r=-(A[1]*conjugado)
    sum2=q+r
    sumat=w+e
    #print(sum2,sumat,"i")
    a=(B[0]*B[0])
    f=-(B[1]*conjugado)
    sum1=a+f
    #print(sum2,sumat,"i / ",sum1)
    #print(sum1)
    qq=sum2/sum1
    ww=sumat/sum1
    ff=(qq,ww)
    return(ff)

def modulo(X):
    mod=math.sqrt((X[0]*X[0])+(X[1]*X[1]))
    return (mod)

def conjugado(X):
    ff=(X[0],(-X[1]))
    return(ff)
    
def prettyPrinting(X):# no probar
    print("(",X[0],"+",X[1],"i)")
    
def carteciana(X):
    return(X)
    
def polar(X):
    a=modulo(X)
    b=math.atan(X[1]/X[0])*(180/math.pi)
    print("(",a,",",b,"°)")

def inversa(A):
    suma_de_cuadrados=(A[1]*A[1])+(A[0]*A[0])
    rta=(A[0]/suma_de_cuadrados,-A[1]/suma_de_cuadrados)
    return rta

def escalar_X_complejo(n,A):
    n=int(stdin.readline())
    rta=(n*A[0],n*A[1])
    return(rta)
"""

def main():   
    A=(0,-1/math.sqrt(2))
    B=(4,0)
    print(inversa(A))
main()
"""
