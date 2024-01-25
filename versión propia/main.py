
from qiskit import ClassicalRegister,QuantumCircuit, QuantumRegister, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from gates import Exp_mod
import matplotlib as plt


def main():


    # Assuming n qubits are sufficient for N=15
    n = 4
    N = 15
    a = 7

    # Crear un circuito cuántico
    regx=QuantumRegister(n, 'regx')
    regX = QuantumRegister(n, 'regX')
    # qubits para almacenar el estado cuántico de la base (reg1)
    reg1 = QuantumRegister(n, 'reg1')
    # qubits para almacenar el resultado de la exponenciación modular (reg2)
    reg2 = QuantumRegister(n, 'reg2')
    # qubits para el módulo N (regN)
    regN = QuantumRegister(n, 'regN')
    # qubits para operaciones auxiliares (regN_ctrl)
    regN_ctrl = QuantumRegister(n, 'regN_ctrl')
    # qubits auxiliares adicionales (ancil_ctrl)
    ancil_ctrl = QuantumRegister(n + 3, 'ancil_ctrl')
    # Registro clásico para la medición
    classical_reg = ClassicalRegister(2 * n, 'classical_reg')

    # Construir el circuito
    qc = QuantumCircuit(regx, reg1, regX, reg2, regN, regN_ctrl, ancil_ctrl)
    qc = Exp_mod(qc, regx, reg1, regX, reg2, regN, regN_ctrl, ancil_ctrl)


    # Inicializar los registros
    qc.x(reg1)  # Set reg1 to |1111>
    qc.x(regN)  # Set regN to |1111> (N = 15)
    
    # Aplicar la transformada de Fourier cuántica al registro 'regx'
    qc.h(regx)

    # Realizar la exponenciación modular
    qc = Exp_mod(qc, regx, reg1, reg1, reg2, regN, regN_ctrl, ancil_ctrl)

    # Aplicar la transformada de Fourier cuántica inversa
    qc.append(QFT(len(regx), do_swaps=False).inverse(), regx)

    # Medir los qubits
    qc.measure(regx, classical_reg)

    # Ejecutar el circuito en un simulador cuántico
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts(qc)
    print(counts)

    # Plot the results
    fig = plot_histogram(counts)
    fig.savefig("histogram.png")  # Saves the plot as an image file
    print(result)
 
if __name__ == "__main__":
    main()