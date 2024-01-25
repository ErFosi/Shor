from qiskit import QuantumCircuit, Aer, execute
from gates import Exp_mod
import qiskit as q
import numpy as np
from gates import *
from handler import nb_to_reg, keys_to_nb, size
import pytest
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Define the number of qubits needed for 'N' and the base 'a'
n = 4  # Number of qubits for the binary representation of 15
N = 15
a = 7  # This is an example; 'a' must be coprime with N (15 in this case)

# Create quantum registers for the algorithm
regN = QuantumRegister(n, name='regN')       # Register to store N (15 in this case)
regN_ctrl = QuantumRegister(n, name='regN_ctrl')  # Ancillary register to store N
regx = QuantumRegister(n, name='regx')       # Register to store the exponent x
reg1 = QuantumRegister(n, name='reg1')       # Register to store the base a
reg2 = QuantumRegister(n, name='reg2')       # Register to store the multiplication results
ancil_ctrl = QuantumRegister(n+2, name='ancil_ctrl')  # Ancillary qubits including one for control
regX = QuantumRegister(1, name='regX')       # Control qubit for controlled operations
c = QuantumCircuit(regN, regN_ctrl, regx, reg1, reg2, ancil_ctrl, regX)

# Initialize regN with the value N
c.initialize([0]*15 + [1], regN)  # This is a simplified way to set the qubit state to represent 15

# Initialize reg1 with the value a
c.initialize([0]*7 + [1], reg1)  # This initializes the register to the binary representation of 7

# Put the exponent qubits in superposition
c.h(regx)

# Now you can call the Exp_mod function
qc = Exp_mod(c, regx, reg1, regX, reg2, regN, regN_ctrl, ancil_ctrl)
# Execute the circuit on a simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=10)
result = job.result()

# Plot the results
counts = result.get_counts(qc)
plot_histogram(counts)