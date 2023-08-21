string = ''
with open('overall_input1.txt') as f:
    line = f.readline()
    while(line):
        line = line[:-1]
        string = string + line + "\\" + "n"  + 'c' + "\\n"
        
        line = f.readline()

string = 'echo -e "ela\\ncryptology\\n4\\nread\\npassword\\nc\\n' + string +'back\\nexit"'
j = open('script1.sh','w+')
j.write(string)
j.close()          