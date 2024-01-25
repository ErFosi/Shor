import math
import random
import sympy
import time
import csv
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def coprimo(numero):
    while True:
        candidato = random.randint(2, numero - 1)
        if math.gcd(numero, candidato) == 1:
            return candidato
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
def find_period(a, N):
    r = 0
    while True:
        print("Iteración de periodo:"+str(r))
        r += 1
        if r >= N:
            return None
        result = pow(a, r, N)
        if result == 1:
            return r
def shors_algorithm(N):
    while True:
        a = random.randint(2, N - 1)
        d = gcd(a, N)
        if d > 1:
            return d  # N es divisible por 'd'
        
        r = find_period(a, N)
        if r is None or r % 2 != 0:
            continue

        x = pow(a, r // 2, N)
        p = gcd(x + 1, N)
        q = gcd(x - 1, N)
        
        if p != 1 and q != 1:
            return (p, q)  # Factores primos encontrados


def buscar_primos(n):
    q_found=1
    p_found=1
    iteracion=0
    iteracion_periodo=0
    print("Esto es una prueba")
    while (q_found==1 or p_found==1):
        iteracion =iteracion+1
        iteracion_periodo=0
        try:
            a = coprimo(n)   # un coprimo de n
            assert gcd(a, n) == 1
            r=0
            rem = 100
            while(rem != 1 ):#"""and r<n/30"""
                iteracion_periodo=iteracion_periodo+1
                #print("Iteracion de periodo:"+str(iteracion_periodo))
                r += 1
                print((str(r))+":"+str((a**r) % n))
                rem = (a**r) % n
                
        
            assert a**r % n == 1
        
            # explicitly use as integer
            f1 = pow(a, r // 2, n) - 1
            f2 = pow(a, r // 2, n) + 1
            q_found = gcd(f1, n)
            print("Iteración:"+str(iteracion))
            print(f'One possible prime factor of n ({n}) is: {q_found}')

            # explicit int (to avoid floating point)
            p_found = int ( n/q_found )
            print(f'The second prime factor of n ({n}) is: {p_found}')
        except Exception as e:
            p_found=1
        #print(f"f1 = {f1}")
        #print(f"f2 = {f2}")
    assert n == p_found * q_found
    return(q_found,p_found)
def shor_cuantico(N):
    from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options
    from qiskit_ibm_runtime import QiskitRuntimeService
    import math
    import numpy as np
    from qiskit import Aer
    from qiskit.algorithms import Shor
    # Save an IBM Quantum account.
    #QiskitRuntimeService.save_account(channel="ibm_quantum", token="fd7358cdc877ebaf1fbec2fe1d431189c1e6d0e1ef005c8ca5cd8969e1428bf8fdf01e7ea6aa4823d81fcf8a9c1aed3285a07ab71e70494a44815b0ae7ad73d7")
    service = QiskitRuntimeService()
    
    # Run on the least-busy backend you have access to
    backend = service.least_busy(simulator=True, operational=True)
    quantum_instance = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=quantum_instance)
    result = shor.factor(N)
    print(f"La lista de factores de {N} calculada por el algoritmo de Shor es {result.factors[0]}.")
    return(result.factors)
if __name__=="__main__":
    #n_prueba1=buscar_primo_fuerzaBruta(499*331)
    #n_prueba=buscar_primos(499*331)
    
    with open('resultados.csv', mode='w', newline='') as csvfile:
        fieldnames = ['N', 'Tiempo (segundos)', 'Primo1', 'Primo2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        inicio = 100
        primos_3_4_digitos = []
       

# Iniciamos la búsqueda desde 100 hasta encontrar 10 pares de primos
        inicio = 100
        while len(primos_3_4_digitos) < 10:
            primos = list(sympy.primerange(inicio, inicio + 200))
            if len(primos) >= 2:
                primo1, primo2 = random.sample(primos, 2)
                primos_3_4_digitos.append((primo1, primo2))
                inicio = primo2 + 1
                inicio=inicio+250
            else:
                inicio += 200  # Si no hay suficientes primos en este rango, avanzamos
        print((primos_3_4_digitos))

        time.sleep(10)
        for i in (primos_3_4_digitos):
            primo1=i[0]
            primo2=i[1]
            n = primo1*primo2
            print(str(primo1)+" x "+str(primo2))
            start_time = time.time()
            factors = shor_cuantico(n)
            #factors=buscar_primo_fuerzaBruta(n)
            q_found=factors[0]
            p_found=factors[1]
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            
            writer.writerow({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found})
            
            print(f"Primos encontrados para N={n}: {p_found} y {q_found}. Tiempo: {elapsed_time} segundos")
            time.sleep(10)
            primo_actual = n  # Actualiza el valor del próximo primo
