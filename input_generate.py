import numpy as np

hex_to_char = {f"{i:04b}": chr(102 + i) for i in range(16)}
bin_XOR_value = list(f"{0x0000901010005000:064b}")

def binary_string_to_plaintext(bin_str):
    return ''.join([hex_to_char[bin_str[i:i+4]] for i in range(0, 64, 4)])

plaintexts = []
for i in range(100000):
    bin_input = np.random.choice(list(hex_to_char.keys()), size=(2, 16))
    bin_plaintext = [list(np.bitwise_xor(bin_input[j], bin_XOR_value)) for j in range(2)]
    plaintexts.extend([binary_string_to_plaintext(bin_str) for bin_str in bin_plaintext])

with open("plaintexts.txt", "w") as f:
    f.write('\n'.join(plaintexts))
