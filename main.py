from AlgoritmosClasicos import buscar_primo_fuerzaBruta
from AlgoritmosClasicos import shors_algorithm
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
##################Main#######################
if __name__=="__main__":
    with open('resultados.csv', mode='w', newline='') as csvfile:
        fieldnames = ['N', 'Tiempo (segundos)', 'Primo1', 'Primo2','algoritmo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        primos=generar_lista_primos(1000,50)
        print(primos)
        time.sleep(10)
        for i in (primos):
            primo1=i[0]
            primo2=i[1]
            n = primo1*primo2
            print(str(primo1)+" x "+str(primo2))
            for x in range(0, 2):
                #time.sleep(1)
                start_time = time.time()
                if (x==0):
                    algoritmo="Fuerza Bruta"
                    factors = buscar_primo_fuerzaBruta(n)
                if (x==1):
                    algoritmo="Shor Clasico"
                    factors = shors_algorithm(n)
                else:
                    algoritmo="GNFS"
                    factors = factorizar(n)
                #factors=buscar_primo_fuerzaBruta(n)
                q_found=factors[0]
                p_found=factors[1]
                end_time = time.time()
                elapsed_time = end_time - start_time
                writer.writerow({'N': n, 'Tiempo (segundos)': elapsed_time, 'Primo1': p_found, 'Primo2': q_found,'algoritmo':algoritmo})
                print(f"Primos encontrados para N={n}: {p_found} y {q_found}. Tiempo: {elapsed_time} segundos con {algoritmo}")

