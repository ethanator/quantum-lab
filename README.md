# quantum-lab
A lab where I tinker with quantum computing and quantum machine learning.

## Roadmap

- May 2, 2023 - May 6, 2023
    - Chapters 1 and 2
    - Plan
        - Chapter 11 Part III > Chapter 3 > Part II
        - [Khan Academy | Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
        - [Interactive Linear Algebra](https://textbooks.math.gatech.edu/ila/)

- April 16, 2023 - April 22, 2023
    - Function fitting

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

- 3 branches of Quantum Information Science (QIS) [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
    - Computation
    - Communication: No eavesdropping
    - Sensing: Micro-PNT (positioning, navigation, timing) devices
- Current era: NISQ (noisy intermediate-scale quantum) computers, coined by John Preskill of CalTech [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
    - No full error-correction
    - < 10^6 qubits
    - vs. scaled fault-tolerant computers
- Definition of a Quantum Computer: A device that leverages specific properties described by quantum mechanics (QM) to perform computation [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
- Superposition Principle: The linear combination of 2+ state vectors is another state vector in the same Hilbert space and describes another state of the system [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
- Born rule: The modulus squared of the amplitude of a state is the probability of that state resulting after measurement [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
- Qiskit Runtime includes two primitives: Estimator and Sampler. [[3]](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/)
- Interference effects can be used to design quantum algorithms. [[4]](https://www.youtube.com/playlist?list=PLOFEBzvs-VvqJwybFxkTiDzhf5E11p8BI)
- Theorem of Quantum Signal Processing (QSP)[[19]](https://pennylane.ai/qml/demos/function_fitting_qsp.html)
    - Measuring in the Hadamard basis to relax the third condition of the theorem
    - Signal Rotation Operator (SRO)
    - Signal Processing Operator (SPO)
    - f(x) is even iff f(x) = f(-x), is odd iff f(x) = -f(-x) [[18]](https://www.nagwa.com/en/videos/432178657986/)
- [lambeq](https://cqcl.github.io/lambeq/)
    - QNLP model: sentence --parsing-> syntax tree --encoding-> string diagram --rewriting-> rewritten string diagram --parameterization-> quantum circuit / tensor net --optimization-> task-specific output
- Landauer's Bound (LB)
    - Minimum amount of energy dissipated for an irreversible computation
    - Energy cost of erasure of n bits is nkTln 2 where k is the Boltzmann constant, and T the temperature in Kelvin of the heat sink surrounding the computing device
- In classical computing we make use of irreversible computations, whereas in quantum computing we limit ourselves to reversible logical operations
    - If we perform an irreversible operation, we have lost information and therefore a measurement
- History of Quantum Computing [[16]](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
    - Paul Benioff, Yuri Manin, Richard Feynman
    - David Deutsch and Richard Josza showed deterministic quantum advantage
    - Ethan Bernstein and Umesh Vazirani (BV) showed in a 1993 paper that non-deterministic quantum advantage (even when small errors are allowed). QFT was also described in the same paper, which would serve as a critical component of Shor's algorithm
    - Daniel Simon, a postdoc at the University of Montreal in 1994
    - Seth Lloyd proposed the first practical appraoch to a working QC
    - In 1994, Peter Shor was a researcher in the mathematical division of Bell Labs in New Jersey. Shor's algorithm achieved exponential speedup
    - In 2001, Isaac Chuang et al implemented Shor's algorithm on a nuclear magnetic resonance (NMR) system to factor the number 15 as a demonstration
    - Lov Grover demonstrated that one can achieve quadratic speedup in a search algorithm on a QC
    - Farhi and Gutmann introduced Hamiltonian oracles and the idea of implementing continuous time models of quantum computation which are different than gate-based approaches
    - In 1999- 2001, Yasunobu Nakamura built and demonstrated a functioning, controllable superconducting qubit
    - Ion trap quantum computers
    - In 1996, David DiVincenzo outlined the key criteria of a quantum computer
- Mathematics
    - John von Neumann observed in his "Mathematical Foundations of Quantum Mechanics" that all of quantum mechanics can be described by linear algebra
- qubit, qutrit, qudit
    - Each of these systems can run any algorithm that the others can, i.e., they can simulate each other

### Notations 

- States in Fourier basis are often denoted with ~

## References

### Papers

1. [Martyn et al, "A Grand Unification of Quantum Algorithms"](https://arxiv.org/pdf/2105.02859.pdf)

### Communities

1. [Discord | QNLP](https://discord.com/channels/905463572497321995/)

### Other Resources

1. [YouTube | Quantum Machine Learning Explained by IBM Technology](https://www.youtube.com/watch?v=NqHKr9CGWJ0)
2. [Qiskit Docs | Get started with the Sampler primitive](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/tutorials/how-to-getting-started-with-sampler.html)
3. [Qiskit Docs | Qiskit Runtime overview](https://qiskit.org/documentation/partners/qiskit_ibm_runtime/)
4. [YouTube | 2021 Qiskit Global Summer School Quantum Machine Learning](https://www.youtube.com/playlist?list=PLOFEBzvs-VvqJwybFxkTiDzhf5E11p8BI)
5. [Wikipedia | Bra-ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation)
6. [Wikipedia | Conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose)
7. [StackExchange | Who introduced the "dagger" symbol as conjugate transpose in quantum mechanics?](https://hsm.stackexchange.com/a/11432/18069)
8. [Learn Quantum Computation using Qiskit](https://qiskit.org/textbook/preface.html)
9. [Qiskit Textbook (new version of the above)](https://qiskit.org/learn/)
10. [Qiskit Docs | Quantum Machine Learning Course](https://learn.qiskit.org/course/machine-learning/)
11. [PennyLane | Learn Quantum Computing](https://pennylane.ai/qml/)
12. [Amazon Braket](https://aws.amazon.com/braket/)
13. [TensorFlow Quantum](https://www.tensorflow.org/quantum)
14. [Cirq](https://quantumai.google/cirq)
15. [pyQuil](https://pyquil-docs.rigetti.com/en/stable/)
16. [Quantum Computing: An Applied Approach (2nd Edition)](https://www.amazon.ca/-/fr/Jack-D-Hidary-dp-3030832732/dp/3030832732/)
17. [GitHub | JackHidary/quantumcomputingbook](https://github.com/JackHidary/quantumcomputingbook)
18. [Parity of a Polynomial Function](https://www.nagwa.com/en/videos/432178657986/)
19. [PennyLane Tutorial | Function fitting using Quantum Signal Processing](https://pennylane.ai/qml/demos/function_fitting_qsp.html)
20. [PennyLane Blog | How to start learning quantum machine learning](https://pennylane.ai/blog/2021/10/how-to-start-learning-quantum-machine-learning/)
21. [PennyLane Blog | Quantum NLP with the lambeq–PennyLane integration](https://pennylane.ai/blog/2023/04/quantum-nlp-with-the-lambeq-pennylane-integration/)