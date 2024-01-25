from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import numpy as np
from qiskit.visualization import circuit_drawer

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import numpy as np

def shors_algorithm(N):
    if N <= 0 or N % 2 == 0:
        raise ValueError("N debe ser un número impar y mayor que 0")

    # Encontrar a, un entero aleatorio coprimo con N
    a = encontrar_a_coprimo(N)

    # Encontrar el período r usando el algoritmo cuántico
    r = encontrar_periodo(a, N)

    # Verificar si r es par y si a^(r/2) es diferente de -1 (mod N)
    if r % 2 == 0 and (a**(r//2)) % N != N - 1:
        factor1 = np.gcd(a**(r//2) + 1, N)
        factor2 = np.gcd(a**(r//2) - 1, N)
        return [factor1, factor2]

    raise ValueError("No se pudo encontrar un factor no trivial")

def encontrar_a_coprimo(N):
    # Encontrar un entero aleatorio coprimo con N (puede ser mejor implementado)
    a = 2
    while np.gcd(a, N) != 1:
        a += 1
    return a

def encontrar_periodo(a, N):
    # Implementación de la parte cuántica de Shor para encontrar el período
    # (Esta es una versión simplificada y puede no ser eficiente para números grandes)

    # Crear un circuito cuántico
    n_count = int(np.ceil(np.log2(N)))
    n_ancilla = 3
    qc = QuantumCircuit(n_count + n_ancilla, n_count)

    # Inicializar qubits
    qc.h(range(n_count + n_ancilla))

    # Aplicar puertas controladas de a^x mod N
    for q in range(n_count):
        qc.append(modular_exponentiation(a, 2**q, N, n_ancilla), 
                 [i for i in range(n_count, n_count + n_ancilla)])

    # Aplicar la transformada de Fourier cuántica (QFT)
    qc.append(QFT(n_ancilla).to_instruction(), 
             [i for i in range(n_count, n_count + n_ancilla)])

    # Medir los qubits de resultado
    qc.measure([i for i in range(n_count, n_count + n_ancilla)], 
               [i for i in range(n_count)])

    # Ejecutar el circuito cuántico
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result()

    # Analizar los resultados (puede necesitar mejoras)
    counts = result.get_counts(qc)
    measured_freqs = [int(k, 2) / (2**n_ancilla) for k in counts.keys()]
    r_estimate = int(1 / np.mean(measured_freqs))

    return r_estimate

def modular_exponentiation(a, x, N, n_ancilla):
    # Implementación simplificada de modular exponentiation (puede necesitar mejoras)
    qc = QuantumCircuit(n_ancilla + 1, n_ancilla)

    for q in range(n_ancilla):
        qc.x(q) if (x & (1 << q)) else None

    for q in range(n_ancilla + 1):
        qc.append(QuantumCircuit(n_ancilla + 1, 1, name='U_a^%d' % (2**q)).to_instruction(), 
                  [i for i in range(n_ancilla + 1)])

    return qc

def QFT(n):
    # Implementación simplificada de la transformada de Fourier cuántica (puede necesitar mejoras)
    qc = QuantumCircuit(n, n)
    for q in range(n):
        qc.h(q)
        for i in range(q + 1, n):
            qc.cp(np.pi / 2**(i - q), i, q)
    for q in range(n // 2):
        qc.swap(q, n - q - 1)
    return qc

# Ejemplo de uso
N = 15
factors = shors_algorithm(N)
print(f"Factores encontrados para N={N}: {factors}")