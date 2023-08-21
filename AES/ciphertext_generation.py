with open('output.txt', 'r') as input_file:
    input_lines = input_file.read().splitlines()

words = [line.split('\t')[-1] for line in input_lines if '\t\t' in line][4:]
words_to_print = words[:1024]

with open('ciphertext3.txt', 'w') as output_file:
    for i in range(8):
        for j in range(128):
            output_file.write(words_to_print[i*128+j] + " ")
        output_file.write("\n")

