import random
import sympy
######################Implementación Shor con algoritmo clásico#######################
def shors_algorithm(N):
    #Implementacion de shor en ordenador clasico
    while True:
        a = random.randint(2, N - 1)#Se hace un guess inicial menor que N
        d = gcd(a, N)
        if d > 1:
            return d  # N es divisible por 'd'
        
        r = find_period(a, N)#Se busca el periodo tal que a^r mod N sea 1
        if r is None or r % 2 != 0:
            continue
        #Una vez obtenido el periodo podremos obtener dos multiplos de N, los primos
        x = pow(a, r // 2, N)
        p = gcd(x + 1, N)
        q = gcd(x - 1, N)
        
        if p != 1 and q != 1:
            return (p, q)  # Factores primos encontrados
def find_period(a, N):
    #Funcion que busca cuando a^r mod N sea 1
    r = 0
    while True:
        #print("Iteración de periodo:"+str(r))
        r += 1
        if r >= N:
            return None
        result = pow(a, r, N)#result = pow(5, 3, 11) calculará 5^3 mod 11
        if result == 1:
            return r
        
###############Implementación de Fuerza Bruta#####################################
def buscar_primo_fuerzaBruta(n):
    iteracion=0
    for x in list(sympy.sieve.primerange(0, n)):
        iteracion=iteracion+1
        print("Iteracion:"+str(iteracion) +" resto:"+ str(n % x))
        if (n % x==0):
            print("Primer primo encontrado")
            primo1=x
    primo2=n/primo1
    print("Primo1:"+str(primo1))
    print("Primo2:"+str(primo2))
    return(primo1,primo2)
##############Implementación de Shor cuántico#####################################


#############Funciones de uso común####################################
def gcd(a,b):#Para comprobar si se puede dividir con resto 0, divisor.
    if b==0:
        return a
    else:
        return gcd(b,a%b)