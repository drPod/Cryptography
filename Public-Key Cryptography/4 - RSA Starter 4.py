# Given only 2 primes and an exponent, we have to find the private key.

# In RSA, the private key is the modular multiplicative inverse of exponent e modulo the totient function - φ(n).
# So, we need to find the totient of n by (p-1)*(q-1) and then find the modular multiplicative inverse of e.

# We can use the sympy library to find the modular multiplicative inverse of e modulo φ(n).

n = (857504083339712752489993810777 - 1) * (1029224947942998075080348647219 - 1)
e = 65537

from sympy import mod_inverse

d = mod_inverse(e, n)
print(d)

# We could have also used the pow function to find the modular multiplicative inverse of e modulo φ(n).
# d = pow(e, -1, n)

# We could have also used the inverse function from the Crypto.Util.number library
# from Crypto.Util.number import inverse
# d = inverse(e, n)
