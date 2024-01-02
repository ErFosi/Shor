from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.circuit.library import QFT
from qiskit.visualization import circuit_drawer
import numpy as np
from time import sleep
def shor(N):
    n = N.bit_length()
    M = 2 ** n
    t = 0
    while M ** (t / 2) < 2 * n ** 2:
        t += 1
    a = encontrar_a_coprimo(N)
    a=7
    print(f"A es el siguiente valor:{a}")
    print(f"T es el siguiente valor:{t}")
    period = None
    while period is None:
        circuit = modular_exponentiation(a, 2 ** t, N)
        #circuit_drawer(circuit, output='mpl',filename="circuito.png").savefig("circuito.png")
        backend = Aer.get_backend('aer_simulator')
        result = execute(circuit, backend, shots=100).result()
        for key, value in result.get_counts().items():
            if value > 0:
                x = int(key, 2)
                period = x // 2 ** (n - t)
                break
    print(f'Period is: {period}')
    factor1 = pow(a, period // 2,N) - 1
    factor2 = pow(a, period // 2,N) + 1
    return (factor1, factor2)

def modular_exponentiation(a, x, N):
    n = N.bit_length()
    qr = QuantumRegister(2*(n))
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr, cr)

    # Initialization
    for i in range(n-1):
        circuit.h(qr[i])
    circuit.x(qr[n-1])
    circuit.h(qr[n-1])

    # Modular exponentiation
    for i in range(n):
        if (x >> i) & 1:
            controlled_modular_multiply(a,  i, N, qr, circuit)

    # Inverse Quantum Fourier Transform
    iqft(n, qr, circuit)

    # Measure
    for i in range(n):
        circuit.measure(qr[i], cr[i])
    #circuit.measure(qr, cr)

    backend = Aer.get_backend('aer_simulator')
    result = execute(circuit, backend, shots=1000).result()
    counts = result.get_counts()

    # Find the most common result
    measured_str = max(counts, key=counts.get)
    measured_int = int(measured_str, 2)

    # Check if measured_int is a non-trivial square root of 1
    if measured_int % 2 != 0:
        return circuit

    # If the result is trivial, repeat the measurement
    return modular_exponentiation(a, x - 1, N) if x > 0 else circuit

def controlled_modular_multiply(a, exponent, N, qr, circuit):
    for _ in range(exponent):
        circuit = modular_multiply(a, N, qr, circuit)
    return circuit
def encontrar_a_coprimo(N):
    # Encontrar un entero aleatorio coprimo con N (puede ser mejor implementado)
    a = 2
    while np.gcd(a, N) != 1:
        a += 1
    return a
def modular_multiply(a, N, qr, circuit):
    n = N.bit_length()
    """
    for i in range(n):
        a_exp_i_mod_N = pow(a, 2 ** i, N)
        for j in range(n):
            if (a_exp_i_mod_N >> j) & 1:
                circuit.cx(qr[j], qr[n])"""

    # Realizar la multiplicación modular controlada
    for i in range(n):
        a_exp_i_mod_N = pow(a, 2 ** i,N)
        for j in range(n):
            if (a_exp_i_mod_N >> j) & 1:
                for target_index in range(n, 2*n):
                    circuit.cx(qr[j], qr[target_index])
    return circuit

def iqft(n, qr, circuit):
    qft_dagger = QFT(n,do_swaps=True, inverse=True)
    circuit.append(qft_dagger, qr[:n][::-1])
    return circuit

# Example usage
N = 15
factors = shor(N)
print("Factores de", N, " : ", factors)
