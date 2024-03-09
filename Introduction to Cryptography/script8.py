# from Crypto.Util.number import *
# from pwn import *
#
# x = long_to_bytes(
#     0x0E0B213F26041E480B26217F27342E175D0E070A3C5B103E2526217F27342E175D0E077E263451150104
# )
#
# output = b""
# y = 1
# while y < 1000:
#     z = xor(x, y)
#     y += 1
#     output = output + z
#
# print(output)
#
from pwn import *
from Crypto.Util.number import *

# if message ^ secret_key = "crypto{"
# therefore message ^ “crypto{“ = partial secret key

x = long_to_bytes(
    0x0E0B213F26041E480B26217F27342E175D0E070A3C5B103E2526217F27342E175D0E077E263451150104
)
# print(x)
y = xor(x[:7], "crypto{")

print(y)
# This prints b'myXORke' which can be translated to "myXORkey"

z = ("myXORkey" * 99)[: len(x)]
print(z)  # z is the full key

a = xor(x, z)
print(a)
