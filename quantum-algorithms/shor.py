#!/usr/bin/env python
"""
This script attempts to implement the Shor's algorithm.

Usage: ./shor.py

References:

1. https://www.youtube.com/shorts/LFOpN5C80g4
2. https://qiskit.org/documentation/getting_started.html
3. https://github.com/Qiskit/qiskit-aqua
4. https://qiskit.org/textbook/ch-algorithms/shor.html
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fractions import Fraction
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
from math import gcd
from numpy.random import randint


def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    if a not in [2, 4, 7, 8, 11, 13]:
        raise ValueError("'a' must be 2, 4, 7, 8, 11, of 13")

    U = QuantumCircuit(4)
    for _ in range(power):
        if a in [2, 13]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)

        if a in [7, 8]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)

        if a in [4, 11]:
            U.swap(1, 3)
            U.swap(0, 2)

        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)

    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"
    c_U = U.control()

    return c_U

def qft_dagger(n):
    """n-qubit QFTdagger the first n qubits in circ"""
    qc = QuantumCircuit(n)
    for qubit in range(n // 2):
        qc.swap(qubit, n - qubit - 1)

    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi / float(2 ** (j - m)), m, j)

        qc.h(j)

    qc.name = "QFT†"

    return qc

def main() -> None:
    n_count = 8
    a = 7

    # Create QuantumCircuit with n_count counting qubits
    # plus 4 qubits for U to act on
    qc = QuantumCircuit(n_count + 4, n_count)

    # Initialize counting qubits
    # in state |+>
    for q in range(n_count):
        qc.h(q)
        
    # And auxiliary register in state |1>
    qc.x(n_count)

    # Do controlled-U operations
    for q in range(n_count):
        qc.append(
            c_amod15(a, 2 ** q),
            [q] + [i + n_count for i in range(4)],
        )

    # Do inverse-QFT
    qc.append(qft_dagger(n_count), range(n_count))

    # Measure circuit
    qc.measure(range(n_count), range(n_count))
    qc.draw(fold=-1) # -1 means 'do not fold' # TODO: Figure out what this means

    # TODO: Figure out how to display the histogram
    # TODO: Address this deprecation warning
    # ```
    # DeprecationWarning: Using a qobj for run() is deprecated as of qiskit-aer 0.9.0
    # and will be removed no sooner than 3 months from that release date. Transpiled
    # circuits should now be passed directly using `backend.run(circuits, **run_options).
    #
    # ```
    # TODO: Address the following error
    # ```
    # TypeError: _run_qobj() got multiple values for argument 'parameter_binds'
    # ```

    # aer_sim = Aer.get_backend("aer_simulator")
    # t_qc = transpile(qc, aer_sim)
    # qobj = assemble(t_qc)
    # results = aer_sim.run(qobj).result()
    # counts = results.get_counts()
    # plot_histogram(counts)

if __name__ == "__main__":
    main()