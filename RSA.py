from math import sqrt
import random
from random import randint
import gmpy2
from gmpy2 import powmod,mpz,isqrt,invert
import numpy as np

ALPHANUM = "0123456789abcdefghijklmnopqrstuvwxyz "
char_to_val = {c: i for i, c in enumerate(ALPHANUM)}
val_to_char = {i: c for i, c in enumerate(ALPHANUM)}

def plaintextConst(pt):
    plaintextBlocks = []
    for block in pt:
        plaintext = 0
        for ch in block:
            val = char_to_val[ch]
            plaintext = plaintext * 38 + val
        plaintextBlocks.append(plaintext)
    return plaintextBlocks

def decryptedPTConst(decPTBlocks):
    plaintextBlocks = []
    for num in decPTBlocks:
        block_chars = []
        if num == 0:
            block_chars.append(val_to_char[0])
        else:
            while num > 0:
                val = num % 38
                block_chars.append(val_to_char[val])
                num //= 38
        block_chars.reverse()
        plaintextBlocks.append(''.join(block_chars))
    return ''.join(plaintextBlocks)

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def isPrime(n):
    if (n == 2):
        return True
    elif (n < 2):
        return False
    else:
        for i in range(1, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False
    return True

def inverseModulus(a, m):
    inv = gmpy2.invert(a, m)
    if inv == 0:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return int(inv)

def keyPairGenerator(maxn=51):
    while True:
        rand1 = random.randint(2, 47)
        rand2 = random.randint(2, 47)
        p = int(gmpy2.next_prime(rand1))
        q = int(gmpy2.next_prime(rand2))
        
        if p == q:
            continue
        
        n = p * q
        if n < 38 or n > maxn:
            continue
        
        phi = (p - 1) * (q - 1)
        
        while True:
            e = random.randrange(2, phi)
            if gcd(e, phi) == 1:
                d = inverseModulus(e, phi)
                if e != d:
                    break
        break

    print("e =", e, "d =", d, "n =", n)
    return ((e, n), (d, n)) #Kpub and Kpr

def get_blocks(PT,block_size):
    blocks = []
    i = 0
    while i<len(PT):
        temp_str=''
        if i+block_size-1 < len(PT):
            temp_str=temp_str+PT[i:i+block_size]
        else :
            temp_str=temp_str+PT[i::]
        blocks.append(temp_str)
        i=i+block_size
    return blocks

def encrypt(plain_text_blocks,public_keys):
    cipher_text_blocks = []
    e,n = public_keys
    for plain_text in plain_text_blocks:
        cipher_text = (gmpy2.powmod(plain_text,e,n))
        cipher_text_blocks.append(cipher_text)
    return cipher_text_blocks

def decrypt(cipher_text_blocks,secret_key):
    d,n = secret_key
    decypted_plain_text_blocks = []
    for cipher_text in cipher_text_blocks:
        plain_text = (gmpy2.powmod(cipher_text,d,n))
        decypted_plain_text_blocks.append(plain_text)
    return decypted_plain_text_blocks