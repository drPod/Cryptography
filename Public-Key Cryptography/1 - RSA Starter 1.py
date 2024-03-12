# Modular Exponentiation is written like: 2^10 mod 17

# There is a python function used for this written as: pow(base, exponent, modulus)

# In RSA, modular exponentiation, coupled with prime factorization, helps building the trapdoor function,
# easy to compute in one direction, but hard to do in reverse.

print(pow(101, 17, 22663))
