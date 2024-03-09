from pwn import *
from Crypto.Util.number import *

key1 = long_to_bytes(0xA6C8B6733C9B22DE7BC0253266A3867DF55ACDE8635E19C73313)
# print(key1)

key12 = long_to_bytes(0x37DCB292030FAA90D07EEC17E3B1C6D8DAF94C35D4C9191A5E1E)
# print(key12)

key2 = xor(key1, key12)
# print(key2)

key23 = long_to_bytes(0xC1545756687E7573DB23AA1C3452A098B71A7FBF0FDDDDDE5FC1)
# print(key23)

key3 = xor(key23, key2)
# print(key3)

key123flag = long_to_bytes(0x04EE9855208A2CD59091D04767AE47963170D1660DF7F56F5FAF)
# print(key123flag)

flag = xor(key1, key2, key3, key123flag)
print(flag)
