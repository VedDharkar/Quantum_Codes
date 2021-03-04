# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:00:27 2021

@author: VED DHARKAR
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
import qiskit as qk

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])

# Shots
simulator = qk.BasicAer.get_backend('qasm_simulator')
circuit_input = int(input("Enter the number of shots:- "))
# Simulating the circuit using the simulator to get the result
job = qk.execute(circuit, simulator, shots = 1000)
result = job.result()

# Output.
counts = result.get_counts(circuit)
print (counts)