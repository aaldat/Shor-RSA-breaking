import RSA
import math
from math import gcd,log
from random import randint
import numpy as np
import gmpy2
from gmpy2 import powmod,mpz,isqrt,invert
from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
from qiskit import Aer,execute,QuantumCircuit
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
from qiskit import IBMQ, execute


def shors_breaker(N):
    backend = Aer.get_backend('qasm_simulator')
    quantum_instance = QuantumInstance(backend,shots=1024)
    find_factors = Shor(N,a=2,quantum_instance=quantum_instance)
    factors = Shor.run(find_factors)
    p = ((factors['factors'])[0])[0]
    q = ((factors['factors'])[0])[1]
    print('Factors of',N,'are :',p,q)
    return p, q
            
def modular_inverse(a,m): 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

if __name__ == '__main__':
    public, private = RSA.keyPairGenerator()

    PT = input("\nPlaintext: ")

    block_size = 1
    PT = RSA.get_blocks(PT,block_size)
    plaintextBlocks = RSA.plaintextConst(PT)
    ciphertextBlocks = RSA.encrypt(plaintextBlocks,public)
    decPTBlocks = RSA.decrypt(ciphertextBlocks,private)
    plain_text_after_decryption = RSA.decryptedPTConst(decPTBlocks)
    print("\nPlaintext decryption using RSA :",plain_text_after_decryption)

    N_shor = public[1]
    assert N_shor>0,"Input must be positive"
    p,q = shors_breaker(N_shor)
    
    phi = (p-1) * (q-1)  
    d_shor = modular_inverse(public[0], phi) 
    decrypted_msg = RSA.decrypt(ciphertextBlocks,(d_shor,N_shor))
    plain_text_Shor = RSA.decryptedPTConst(decrypted_msg)
    print("\nPlaintext decryption using Shor :",plain_text_Shor)