import test_gates
from qiskit import QuantumCircuit, QuantumRegister, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from gates import Exp_mod



def main():


    # Assuming n qubits are sufficient for N=15
    n = 4

    # Initialize quantum registers
    regx = QuantumRegister(n, 'regx')
    reg1 = QuantumRegister(n, 'reg1')
    regX = QuantumRegister(1, 'regX')  # Assuming a single qubit for simplicity
    reg2 = QuantumRegister(n, 'reg2')
    regN = QuantumRegister(n, 'regN')
    regN_ctrl = QuantumRegister(n, 'regN_ctrl')
    ancil_ctrl = QuantumRegister(n, 'ancil_ctrl')  # Adjust size as necessary
    meas = QuantumRegister(n, 'meas')

    # Initialize the circuit
    c = QuantumCircuit(regx, reg1, regX, reg2, regN, regN_ctrl, ancil_ctrl, meas)

    # Prepare initial state
    c.h(regX)  # Create a superposition of x values
    # Initialize regN to represent the number 15
    c.x(regN[0])
    c.x(regN[1])
    c.x(regN[2])
    c.x(regN[3])

    # Call Exp_mod function (assuming implementation is provided)
    c = Exp_mod(c, regx, reg1, regX, reg2, regN, regN_ctrl, ancil_ctrl)

    # Inverse QFT for extracting the phase
    c.append(QFT(num_qubits=n, inverse=True), regx[:])

    # Measurement
    c.measure(regx, meas)

    # Execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(c, backend, shots=1024)
    result = job.result()
    counts = result.get_counts(c)

    # Plot the results
    plot_histogram(counts)

 
if __name__ == "__main__":
    main()