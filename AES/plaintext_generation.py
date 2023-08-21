import numpy as np

def generate_plaintext(mapping_dict):
    plaintext_list = []
    for i in range(8):
        plaintext_row = ""
        for j in range(128):
            binary = bin(j)[2:].zfill(8)
            plaintext = 'ff' * i + mapping_dict[binary[:4]] + mapping_dict[binary[4:]] + 'ff' * (8 - i - 1)
            plaintext_row += plaintext + " "
        plaintext_list.append(plaintext_row)
    return plaintext_list

def write_plaintext_to_file(plaintext_list, filename):
    with open(filename, "w+") as file:
        for row in plaintext_list:
            file.write(row)
            file.write("\n")

if __name__ == "__main__":
    mapping = {'0000': 'f', '0001': 'g', '0010': 'h', '0011': 'i', '0100': 'j', '0101': 'k', '0110': 'l', '0111': 'm', '1000': 'n', '1001': 'o', '1010': 'p', '1011': 'q', '1100': 'r', '1101': 's', '1110': 't', '1111': 'u'}
    plaintext_list = generate_plaintext(mapping)
    write_plaintext_to_file(plaintext_list, "plaintext.txt")
    print("Generating plaintext Done....")
