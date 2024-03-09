from pwn import *

x = xor("label", 13)

print(x)
