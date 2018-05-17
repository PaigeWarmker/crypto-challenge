import sys

args = sys.argv[1:]

if len(args) != 2:
    print("Provide two equal-length buffers to be XOR'd")
    sys.exit (1)

b0 = bytes.fromhex(args[0])
b1 = bytes.fromhex(args[1])
if len(b0) != len(b1):
    print("Provide two equal-length buffers to be XOR'd")
    sys.exit (1)

xor = bytes(x ^ y for x, y in zip(b0, b1))
print(xor.hex())
