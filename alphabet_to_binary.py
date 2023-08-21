# Define the mapping from f to u using dictionary comprehension
mapping = {chr(i+102): '{0:04b}'.format(i) for i in range(16)}

# Open the input file and read the lines
with open('ciphertexts.txt', 'r') as f:
    lines = f.readlines()

# Encode each line of text into binary using the mapping
binary_lines = []
for line in lines:
    binary = ''
    for char in line:
        if char.lower() in mapping:
            binary += mapping[char.lower()]
        else:
            # If character not in mapping, skip it
            continue
    binary_lines.append(binary)

# Write the binary representation to a file
with open('binary_cipher.txt', 'w') as f:
    for line in binary_lines:
        f.write(line + '\n')

print("Binary representation of the text written to binary_cipher.txt.")

# Close the output file
f.close()
