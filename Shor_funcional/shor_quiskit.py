from Shor import Shor
import math
from qiskit import IBMQ
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_ibm_runtime import QiskitRuntimeService
import qiskit_ibm_provider
#IBMQ.save_account('token')
# Crear una instancia de la clase Shor
# Cargar tu cuenta de IBMQ
#IBMQ.load_account()
#IBMQ.save_account('0818642c014d305e9ed09b128e956f8664588a5c0e5cf8e7551a27ce6227f4abfba5bad00b11c5906020bd092cc14cee499068fbc68bfab33475bfc09f3cf4fa', overwrite=True)

#service = QiskitRuntimeService()
#service.backends(simulator=False, operational=True, min_num_qubits=30)
# Seleccionar el proveedor y el backend
#provider = IBMQ.get_provider(hub='ibm-q')
tok='0818642c014d305e9ed09b128e956f8664588a5c0e5cf8e7551a27ce6227f4abfba5bad00b11c5906020bd092cc14cee499068fbc68bfab33475bfc09f3cf4fa'
backend = QuantumInstance(qiskit_ibm_provider.IBMProvider(token=tok).get_backend('ibm_cairo'))
#backend = QuantumInstance(Aer.get_backend('qasm_simulator'))
#backend = QuantumInstance(provider.get_backend('ibm_cairo'))
#backend = QuantumInstance(provider.get_backend('simulator_mps'))
shor_instance = Shor(quantum_instance=backend)

# Valores para factorizar
N1 = 15
A1 = 2
N2 =57
A2 = 5

circuit = shor_instance.construct_circuit(N2, A2)
#circuit.draw(output='mpl', filename='circuit.png')  #Descomentar si se quiere guardar la imagen del circuito
decomposed_circuit = circuit.decompose()  # Descomponer el circuito una vez
decomposed_circuit = decomposed_circuit.decompose()  # Descomponer nuevamente si es necesario
#decomposed_circuit.draw(output='mpl',filename="decompose_expmod") #Descomentar si se quiere guardar la imagen del circuito con la exp mod descompuesta en sumas


#Llamar al método factor

#factors_N1 = shor_instance.factor(15, 2)
factors_N2 = shor_instance.factor(N2, A2)

#print(f"Factores de {N1} con base {A1}: {factors_N1}")
print(f"Factores de {N2} con base {A2}: {factors_N2}")