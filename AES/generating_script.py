new_string = ''
file = open('plaintext.txt', 'r')
for line in file.readlines():
    words = line.split()
    for word in words:
        if word == '\n':
            continue
        new_string = new_string + word + "\\" + "n"  + 'c' + "\\n"

final_string = 'echo -e "ela\\ncryptology\\n5\\ngo\\nwave\\ndive\\ngo\\nread\\n' + new_string +'back\\nexit"'
script_file = open('script.sh', 'w+')
script_file.write(final_string)
script_file.close()
