from Crypto.Util.number import *
from pwn import *

x = long_to_bytes(
    0x73626960647F6B206821204F21254F7D694F7624662065622127234F726927756D
)  # bytes.fromhex() does the same thing
print(x)

y = 0
while y < 100:
    z = xor(x, y)
    y += 1
    print(z)
