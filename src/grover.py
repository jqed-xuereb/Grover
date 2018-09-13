from qiskit import register, available_backends, get_backend
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit, execute
from qiskit.tools.visualization import plot_histogram, matplotlib_circuit_drawer as drawer, qx_color_scheme
from qiskit import QuantumProgram
import Qconfig

qx_config = {
    "APItoken": Qconfig.APItoken,
    "url": Qconfig.config['url']}

#set api
register(qx_config['APItoken'], qx_config['url'])

# set up registers and program
qr = QuantumRegister(16)
cr = ClassicalRegister(16)
qc = QuantumCircuit(qr, cr)

# rightmost eight (qu)bits have ')' = 00101001 .x is like identity
qc.x(qr[0]) 
qc.x(qr[3])
qc.x(qr[5])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[9]) # Haddamard create superposition on 9
qc.cx(qr[9],qr[8]) # spread it to 8 with a CNOT
qc.x(qr[11])
qc.x(qr[12])
qc.x(qr[13])

# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

backend = "ibmq_qasm_simulator" 
shots_sim = 128

job_sim = execute(qc, backend, shots=shots_sim)
stats_sim = job_sim.result().get_counts()

drawer(qc)
plot_histogram(stats_sim)