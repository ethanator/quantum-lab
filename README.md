# quantum-lab
A lab where I tinker with quantum computing and quantum machine learning.

## Roadmap (TBD)

- April 9, 2023 - April 15, 2023
    - [HHL Algorithm](https://youtu.be/hQpdPM-6wtU)
        - [Quantum Matrix Inversion](https://youtu.be/24gxm-DhH2E)
        - Hermitian simulation
        - Rejection sampling
    - [Classical vs. Quantum ML](https://youtu.be/OstyW7c0v48)
        - QRAM
        - [Quantum Kernel Machine Learning](https://qiskit.org/ecosystem/machine-learning/tutorials/03_quantum_kernel.html)
            - Kernel trick
            - [Quantum SVM](https://youtu.be/OKbcJCUx6xA)
            - Spectral clustering
        - Quantum PCA
    - [Grover's Algorithm](https://youtu.be/0RPFWZj7Jm0)

- April 1, 2023 - April 8, 2023
    - [Single qubit gates](https://qiskit.org/textbook/ch-states/single-qubit-gates.html)
        - Bloch sphere
        - Pauli gates: X-gate (NOT gate), Y-, Z-gates
        - get_statevector, plot_bloch_multivector
    - [Shor's Algorithm](https://qiskit.org/textbook/ch-algorithms/shor.html)
    - [Quantum phase estimation](https://qiskit.org/textbook/ch-algorithms/quantum-phase-estimation.html)
        - [Phase kickback](https://qiskit.org/textbook/ch-gates/phase-kickback.html)
            - CNOT
        - Counting register vs. Auxiliary register
        - n-bit Hadamard gate
        - T-gate
    - [Quantum Fourier Transform](https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html)
        - Fourier basis (X-basis) vs. Computational basis (Z-basis)
        - Controlled rotation CROT
    - [OpenQASM](https://github.com/openqasm/openqasm)
    - Unitary operator
    - Eigenstate
    - Bra-ket notation
    - Continued fractions algorithm
    - Circuit diagram

## Notes

- Qiskit Runtime includes two primitives: Estimator and Sampler. [[3]](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/)
- Interference effects can be used to design quantum algorithms. [[4]](https://www.youtube.com/playlist?list=PLOFEBzvs-VvqJwybFxkTiDzhf5E11p8BI)

### Notations

- States in Fourier basis are often denoted with ~

## References

1. [YouTube | Quantum Machine Learning Explained by IBM Technology](https://www.youtube.com/watch?v=NqHKr9CGWJ0)
2. [Qiskit Docs | Get started with the Sampler primitive](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/tutorials/how-to-getting-started-with-sampler.html)
3. [Qiskit Docs | Qiskit Runtime overview](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/)
4. [YouTube | 2021 Qiskit Global Summer School Quantum Machine Learning](https://www.youtube.com/playlist?list=PLOFEBzvs-VvqJwybFxkTiDzhf5E11p8BI)
5. [Wikipedia | Bra-ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation)
6. [Wikipedia | Conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose)
7. [StackExchange | Who introduced the "dagger" symbol as conjugate transpose in quantum mechanics?](https://hsm.stackexchange.com/a/11432/18069)
8. [Learn Quantum Computation using Qiskit](https://qiskit.org/textbook/preface.html)
9. [Qiskit Textbook (new version of the above)](https://qiskit.org/learn/)
