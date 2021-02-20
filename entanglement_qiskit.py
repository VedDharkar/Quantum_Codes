# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:42:29 2021

@author: VED DHARKAR
"""

import qiskit as qk

# Input from user about number of qubits and bits




q = qk.QuantumRegister(2)
c = qk.ClassicalRegister(2)

 
# Circuit
circuit = qk.QuantumCircuit(q, c)

# Hadamard Gate on the first Qubit
circuit.h(0)
# CNOT Gate on the first and second Qubits
circuit.cx(0, 1)
# Measuring the Qubits
circuit.measure(q, c)

print(circuit)

# Shots
simulator = qk.BasicAer.get_backend('qasm_simulator')
shot_input = int(input("Enter the number of shots:- "))
# Simulating the circuit using the simulator to get the result
job = qk.execute(circuit, simulator, shots = shot_input)
result = job.result()

# Output.
counts = result.get_counts(circuit)
print (counts)


