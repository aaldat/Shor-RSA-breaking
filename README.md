# Breaking RSA with Quantum Computing: Shor's Algorithm

This repository contains a hybrid classical-quantum project demonstrating how **RSA public-key cryptography** can be compromised using **Shor's Algorithm** simulated on a quantum computer. 

Developed as a project for the Quantum Computing course at Politecnico di Torino, it bridges the gap between classical cryptographic concepts and quantum cryptanalysis.

The project workflow is divided into two main phases:

1. **The Classical Phase (RSA Setup):** a custom implementation of the RSA algorithm (`RSA.py`). It generates prime numbers, creates public ($e, N$) and private ($d, N$) keys, and successfully encrypts and decrypts a user-provided plaintext message.
2. **The Quantum Phase (Shor's Attack):** the main script extracts the public modulus $N$ and passes it to a simulated quantum circuit using Qiskit. Shor's algorithm runs phase estimation and modular exponentiation to find the prime factors ($p$ and $q$) of $N$, effectively breaking the encryption without knowing the private key.


## Repository Structure

* `test.py`: The core executable script that runs the RSA simulation followed by the quantum attack (formerly `test.py`).
* `RSA.py`: Custom classical library for RSA key generation, encryption, and decryption.
* `Shor.ipynb`: A Jupyter Notebook for isolated testing and visualization of the quantum circuit.
* `fastdtw/`: Locally modified version (vendored) of the FastDTW library, required for specific quantum operations.
* `requirements.txt`: Strict dependency list to ensure reproducibility.

---

## Scalability & Local Simulation

The current configuration of this project (parameters, library patches, and RSA key sizes) has been specifically tuned to allow the **quantum circuit to be simulated on a standard local machine**. 

* In Shor's algorithm, for a local simulation, we use a small $N$ (e.g., 51 or 15) to keep the number of qubits and the simulation time within reasonable limits.
* **Qiskit Aqua Patches:** the specific library versions and manual fixes were implemented to maintain a stable environment on Python 3.9, ensuring the `qasm_simulator` remains performant.
* **Scalability:** the logic implemented in `main.py` and `RSA.py` is theoretically **identical** to what would be used for larger integers. To scale this project:
    1. Increase the prime generation bit-size in `RSA.py`.
    2. Connect to a real Quantum Device (via the IBM Quantum API) instead of the local Aer simulator.
    3. Be aware that factoring a standard 2048-bit RSA key would require millions of physical qubits, far exceeding current hardware capabilities, but the **software architecture of this project remains valid**.

---

## Important Note on Reproducibility & Dependencies

Quantum computing libraries evolve rapidly. This project was built using the **legacy `qiskit.aqua` module**, which has since been deprecated in newer Qiskit releases. 

Furthermore, newer versions of `scipy` have removed certain utilities (`sputils`) that `qiskit.aqua` relies heavily upon. **To run this code successfully without `ImportError` crashes, you must strictly use the versions specified in the `requirements.txt` file.**

*(Note: The `fastdtw` library has been directly included in the root directory because internal modifications were made to ensure compatibility with this specific Qiskit setup.)*

---

## Installation

pip install -r requirements.txt
