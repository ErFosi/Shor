import qiskit
import time
import csv
import random
import sympy
import os
from Shor import Shor
from qiskit import IBMQ
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_ibm_runtime import QiskitRuntimeService
import qiskit_ibm_provider

def generar_lista_primos(intervalo,cuantos):
    listaN=[]
    inicio = 3
    while len(listaN) < cuantos:
        primos = list(sympy.primerange(inicio, inicio + intervalo))
        if len(primos) >= 2:
            primo1, primo2 = random.sample(primos, 2)
            listaN.append((primo1, primo2))
            inicio = primo2 + 1
            inicio=inicio+intervalo
        else:
            inicio += 10  # Si no hay suficientes primos en este rango, avanzamos
    #print(listaN)

    return(listaN)


def guardar_resultados(resultados):
    with open('Shor_funcional/resultados_circuito.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Primo 1', 'Primo 2', 'Producto', 'Tiempo (segundos)'])
        writer.writerows(resultados)

def guardar_circuito(circuito, archivo):
    carpeta_circuitos = os.path.dirname(archivo)
    if not os.path.exists(carpeta_circuitos):
        os.makedirs(carpeta_circuitos)
    with open(archivo, 'w') as f:
        f.write(circuito.qasm())  # Guarda en formato QASM
        print(f"Se ha guardado el archivo {archivo}")

def circuitos():
    tok='0818642c014d305e9ed09b128e956f8664588a5c0e5cf8e7551a27ce6227f4abfba5bad00b11c5906020bd092cc14cee499068fbc68bfab33475bfc09f3cf4fa'
    backend =QuantumInstance(qiskit_ibm_provider.IBMProvider(token=tok).get_backend('ibm_cairo'))
    shor_instance = Shor(quantum_instance=backend)
    primos_pequeños=generar_lista_primos(10,8)
    primos = generar_lista_primos(200, 25)
    primos=primos_pequeños + primos
    print(primos)
    resultados=[]
    carpeta_circuitos = 'Shor_funcional/circuits'
    for primo1, primo2 in primos:
        inicio = time.time()
        producto = primo1 * primo2
        circuit = shor_instance.construct_circuit(producto, 2)
        tiempo = time.time()
        nombre_archivo_qasm = f"{carpeta_circuitos}/{producto}_{primo1}_{primo2}_circuit.qasm"
        guardar_circuito(circuit, nombre_archivo_qasm)
        resultados.append((primo1, primo2, producto, tiempo-inicio))

    return resultados


if __name__ == "__main__":
    
    resultados=circuitos()
    guardar_resultados(resultados)
