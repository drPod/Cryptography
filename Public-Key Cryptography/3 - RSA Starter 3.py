# ChatGPT said:

# The Euler totient function, denoted by φ(n) (phi n), is a mathematical function that counts the number of positive integers less than or
# equal to n that are relatively prime to n. In other words, it calculates the number of integers between 1 and n that have no common
# factors with n other than 1.

# For example, if n = 8, the numbers less than or equal to 8 that are relatively prime to 8 are 1, 3, 5, and 7,
# as they have no common factors with 8 other than 1. So, φ(8) = 4.

# from sympy import totient

# print(totient(857504083339712752489993810777 * 1029224947942998075080348647219))

# The above code will run forever, as the number is too large for the sympy library to handle.
# However, the totient function can be calculated using the formula:
# φ(N) = (p - 1) * (q - 1)

# Given the two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

x = (p - 1) * (q - 1)
print(x)
