from AlgoritmosClasicos import buscar_primo_fuerzaBruta
from AlgoritmosClasicos import shors_algorithm
from AlgoritmosClasicos import factorizar
import sympy
import random
import csv
import time

#from sympy import EllipticCurve, Point, Symbol
#Metodo para generar una lista de numeros resultado de una multiplicación de 2 primos
def generar_lista_primos(intervalo,cuantos):
    listaN=[]
    inicio = 100
    while len(listaN) < cuantos:
        primos = list(sympy.primerange(inicio, inicio + 200))
        if len(primos) >= 2:
            primo1, primo2 = random.sample(primos, 2)
            listaN.append((primo1, primo2))
            inicio = primo2 + 1
            inicio=inicio+intervalo
        else:
            inicio += 100  # Si no hay suficientes primos en este rango, avanzamos
    #print(listaN)

    return(listaN)
def main():
    all_results = []

    fuerza_bruta_results = []
    shor_results = []
    gnfs_results = []

    primos = generar_lista_primos(1000, 4)
    print(primos)
    time.sleep(10)

    for i in primos:
        primo1 = i[0]
        primo2 = i[1]
        n = primo1 * primo2
        print(str(primo1) + " x " + str(primo2))

        for x in range(3):
            start_time = time.time()

            if x == 0:
                algoritmo = "Fuerza Bruta"
                factors = buscar_primo_fuerzaBruta(n)
                end_time = time.time()
                elapsed_time = end_time - start_time
                fuerza_bruta_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                all_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                q_found = factors[0]
                p_found = factors[1]
                print(f"Primos encontrados para N={n}: {p_found} y {q_found}. Tiempo: {elapsed_time} segundos con {algoritmo}")
            elif x == 1:
                algoritmo = "Shor Clasico"
                factors = shors_algorithm(n)
                end_time = time.time()
                elapsed_time = end_time - start_time
                shor_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                all_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                q_found = factors[0]
                p_found = factors[1]
                print(f"Primos encontrados para N={n}: {p_found} y {q_found}. Tiempo: {elapsed_time} segundos con {algoritmo}")
            else:
                algoritmo = "GNFS"
                factors = factorizar(n)
                end_time = time.time()
                elapsed_time = end_time - start_time
                gnfs_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                all_results.append({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found, 'Algoritmo': algoritmo})
                q_found = factors[0]
                p_found = factors[1]
                print(f"Primos encontrados para N={n}: {p_found} y {q_found}. Tiempo: {elapsed_time} segundos con {algoritmo}")

            

    with open('resultados.csv', mode='w', newline='') as csvfile:
        fieldnames = ['N', 'Tiempo (segundos)', 'Primo1', 'Primo2', 'Algoritmo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    with open('fuerza_bruta_results.csv', mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fuerza_bruta_results)

    with open('shor_results.csv', mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shor_results)

    with open('gnfs_results.csv', mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(gnfs_results)

if __name__ == "__main__":
    main()