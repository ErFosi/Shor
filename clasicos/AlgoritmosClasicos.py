import random
import sympy
from math import gcd
######################Implementación Shor con algoritmo clásico#######################
def shors_algorithm(N):
    #Implementacion de shor en ordenador clasico
    #primes = list(sympy.sieve.primerange(0, N))
    #primes.reverse()
    n = N.bit_length()
    a_values_tested = set()
    while True:
        # Selecciona un 'a' aleatorio que no se haya probado antes
        a = random.randint(2, N - 1)
        if a in a_values_tested:
            print("a ya utilizado")
        else:
            a_values_tested.add(a)

            if gcd(a, N) == 1:
                print(f"{N} y {a} son coprimos")
                d = gcd(a, N)
                if d > 1:
                    return d  # N es divisible por 'd'

                r = find_period(a, N, n)  # Se busca el período
                if r is not None and r % 2 == 0:
                    # Calcula los posibles factores
                    x = pow(a, r // 2, N)
                    p = gcd(x + 1, N)
                    q = gcd(x - 1, N)

                    if p != 1 and q != 1:
                        return (p, q)  # Factores primos encontrados
def find_period(a, N, n):
    # Calcula el límite máximo de iteraciones para encontrar el período
    max_iteraciones = int(10 * 1.69**n)

    # Función que busca cuando a^r mod N sea 1
    r = 0
    for _ in range(max_iteraciones):
        r += 1
        if r >= N:
            return None
        result = pow(a, r, N)
        if result == 1:
            return r
    return None
        
###############Implementación de Fuerza Bruta#####################################
def buscar_primo_fuerzaBruta(n):
    iteracion=0
    for x in list(sympy.sieve.primerange(0, n)):
        iteracion=iteracion+1
        #print("Iteracion:"+str(iteracion) +" resto:"+ str(n % x))
        if (n % x==0):
            #print("Primer primo encontrado")
            primo1=x
            break
    primo2=n/primo1
    #print("Primo1:"+str(primo1))
    #print("Primo2:"+str(primo2))
    return(primo1,int(primo2))
##############Implementación de GNFS de la libreria sympy###########################
def factorizar(N):
    p, q = sympy.factorint(N).keys()
    return (p, q)
##############Implementación de Shor cuántico#####################################


#############Funciones de uso común####################################
"""def gcd(a,b):#Para comprobar si se puede dividir con resto 0, divisor.
    if b==0:
        return a
    else:
        return gcd(b,a%b)"""