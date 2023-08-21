# Define the file paths
plaintext_file = 'plaintexts.txt'
script_file = 'script.sh'

# Define the password and other constants
password = 'c'
prompt = 'ela\\ncryptology\\n4\\nread\\npassword\\n'
footer = 'back\\nexit'

# Read the plaintexts and create the string
with open(plaintext_file) as f:
    plaintexts = [line.strip() for line in f]

plaintext_string = '\\n'.join(plaintexts)
input_string = f'{prompt}{password}\\n{plaintext_string}\\n{footer}'

# Write the string to the script file
with open(script_file, 'w') as f:
    f.write(f'echo -e "{input_string}"')
