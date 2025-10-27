# main.py

from qiskit import QuantumRegister , ClassicalRegister , QuantumCircuit
from qiskit_aer import StatevectorSimulator, QasmSimulator, AerSimulator
import matplotlib.pyplot as plt

def main():
    print("Hello from quantum-computing-lab!")
    print("Setting up a simple Qiskit quantum circuit...")

    qreg_q = QuantumRegister(1,'q')
    creg_c = ClassicalRegister(1,'c')

    qc = QuantumCircuit(qreg_q,creg_c)

    qc.h(qreg_q[0])
    qc.measure(qreg_q,creg_c)
    print(qc.draw("mpl"))

    # M_simulator = QasmSimulator()

    # M_simulator = StatevectorSimulator()
    M_simulator = AerSimulator()

    job = M_simulator.run(qc,shots=1024)
    result = job.result()
    print(result.get_counts(qc))

if __name__ == "__main__":
    main()
