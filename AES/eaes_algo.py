print("Start Decrypting Password")

#importing required libraries
import numpy as np
import random
from pyfinite import ffield

F = ffield.FField(7)
def Expo(b,e):
    ans = 1
    for i in range(e):
        ans = F.Multiply(ans,b)
    return ans

def access_file():
    inp_file = open("plaintext.txt", 'r')
    out_file = open("ciphertext.txt", 'r')
    return inp_file,out_file

# map block to hex values
def convert_block_to_byte(c):
    tem_plain = ""
    for i in range(0, len(c), 2):
        #mappig two char set(byte) into he value
        st=c[i:i+2]
        char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
        tem_plain += char
    return tem_plain

def cryptanalysis(plaintext, lin_mat, exp_mat):
    plaintext = [ord(c) for c in plaintext]
    Output = [[0 for j in range (8)] for i in range(8)]
    for ind, elem in enumerate(plaintext):
        Output[0][ind] = Expo(elem, exp_mat[ind])
        
    #taking LinearTransformation on lin_mat and Output[0]
    mat=lin_mat
    elist=Output[0]
    result = [0,0,0,0,0,0,0,0]
    for row, elem in zip(mat, elist):
        temp_res = [0,0,0,0,0,0,0,0]
        for i, e in enumerate(row):
            temp_res[i] = F.Multiply(e, elem)
        temp_result = [0,0,0,0,0,0,0,0]
        for i, (e1, e2) in enumerate(zip(temp_res, result)):
            temp_result[i] = int(e1) ^ int(e2)
        result = temp_result
    Output[1] = result
    
    for ind, elem in enumerate(Output[1]):
        Output[2][ind] = Expo(elem, exp_mat[ind])
        
    #taking LinearTransformation on lin_mat and Output[2]    
    mat=lin_mat
    elist=Output[2]
    result = [0,0,0,0,0,0,0,0]
    for row, elem in zip(mat, elist):
        temp_res = [0,0,0,0,0,0,0,0]
        for i, e in enumerate(row):
            temp_res[i] = F.Multiply(e, elem)
        temp_result = [0,0,0,0,0,0,0,0]
        for i, (e1, e2) in enumerate(zip(temp_res, result)):
            temp_result[i] = int(e1) ^ int(e2)
        result = temp_result
    Output[3] = result

    for ind, elem in enumerate(Output[3]):
        Output[4][ind] = Expo(elem, exp_mat[ind])
        
    return Output[4]


def processing_hex_value(iline,ind,flag):
    ips=[]
    for hex_value in iline.strip().split(" "):
        c=hex_value
        tem_plain = ""
        for i in range(0, len(c), 2):
            st=c[i:i+2]
            a11=16*(ord(st[0]) - ord('f'))
            a12=ord(st[1]) - ord('f')
            char = chr( a11+a12 )
            tem_plain += char
        if flag:
            ips.append(tem_plain[ind+1])
        else:
            ips.append(tem_plain[ind])
    return ips

def finding_block_value():
    input_file,output_file = access_file()
    #use to store possible exponents
    e_vector = [[] for i in range(8)]
    #use to store all possible diagonal values
    a_vector = [[[] for i in range(8)] for j in range(8)]
    for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
        #Converting each input to corresponding hex values in input file
        ips = processing_hex_value(iline,ind,False)
        #Converting each input to corresponding hex values in output file
        ous = processing_hex_value(oline,ind,False)
        for i in range(1, 127):
            for j in range(1, 128):
                flag = True
                for inps, outs in zip(ips, ous):
                    a11=Expo(ord(inps), i)
                    a12=Expo(F.Multiply(a11, j), i)
                    a13=Expo(F.Multiply(a12, j), i)
                    if ord(outs) != a13:
                        flag = False
                        break
                if flag:
                    e_vector[ind].append(i)
                    a_vector[ind][ind].append(j)
    return a_vector,e_vector


a_vector,e_vector=finding_block_value()

def finding__matrix():
    input_file,output_file = access_file()
    for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
        if ind > 6 :
            break
        #Converting each input to corresponding hex values in input file
        ips = processing_hex_value(iline,ind,False)
        #Converting each input to corresponding hex values in output file
        ous = processing_hex_value(oline,ind,True)
            
        for i in range(1, 128):
            #iterate over exponents and diagonal values
            for p1, e1 in zip(e_vector[ind+1], a_vector[ind+1][ind+1]):
                for p2, e2 in zip(e_vector[ind], a_vector[ind][ind]):
                    flag = True
                    for inp, outp in zip(ips, ous):
                        a11=Expo(ord(inp), p2)
                        a12=F.Multiply(a11, e2)
                        a13=Expo(a12, p2)
                        temp1=F.Multiply(a13, i) 
                        temp2=F.Multiply(Expo(F.Multiply(Expo(ord(inp), p2), i), p1), e1)
                        if ord(outp) != Expo(int(temp1) ^ int(temp2), p1):
                            flag = False
                            break
                    if flag:
                        e_vector[ind+1] = [p1]
                        a_vector[ind+1][ind+1] = [e1]
                        e_vector[ind] = [p2]
                        a_vector[ind][ind] = [e2]
                        a_vector[ind][ind+1] = [i]
    return a_vector,e_vector

def final_mv(a_vector,e_vector):
    for index in range(6):
        of = index + 2    
        exp_list = [e[0] for e in e_vector]
        lin_trans_list = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                lin_trans_list[i][j] = 0 if len(a_vector[i][j]) == 0 else a_vector[i][j][0]
        inp,out = access_file()
        for ind, (iline, oline) in enumerate(zip(inp.readlines(), out.readlines())):
            if ind > (7-of):
                continue
            ips=[]
            for msg in iline.strip().split(" "):
                ips.append(convert_block_to_byte(msg))
            ous=[]
            for msg in oline.strip().split(" "):
                ous.append(convert_block_to_byte(msg))
         
            for i in range(1, 128):
                lin_trans_list[ind][ind+of] = i
                flag = True
                for inps, outs in zip(ips, ous):
                    if cryptanalysis(inps, lin_trans_list, exp_list)[ind+of] != ord(outs[ind+of]):
                        flag = False
                        break
                if flag:
                    a_vector[ind][ind+of] = [i]
        inp.close();
        out.close();
    return a_vector,exp_list
        
        
        
a_vector,e_vector=finding__matrix()
a_vector,e_vector=final_mv(a_vector,e_vector)
lin_trans_list = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lin_trans_list[i][j] = 0 if len(a_vector[i][j]) == 0 else a_vector[i][j][0]



#Two halves of password
password_1 = "jghrlgmnhsgfffjk"
password_2 = "gkikhrmjkrgigjmu"
indt = {'0000': 'f','0001': 'g','0010': 'h','0011': 'i','0100': 'j','0101': 'k','0110': 'l','0111': 'm','1000': 'n','1001': 'o','1010': 'p','1011': 'q','1100': 'r','1101': 's','1110': 't','1111': 'u'}

def DecryptPassword(password):
    passw = convert_block_to_byte(password)
    op = ""
    for ind in range(8):
        for ans in range(128):
            temp1 = '{:0>8}'.format(format(ans,"b"))
            tempa = indt[temp1[0:4]]
            tempb=  indt[temp1[4:8]]
            inp = op + tempa+tempb +(16-len(op)-2)*'f'
            if ord(passw[ind]) == cryptanalysis(convert_block_to_byte(inp), lin_trans_list, e_vector)[ind]:
                b=ans
                temp1 = '{:0>8}'.format(format(b,"b"))
                a = indt[temp1[0:4]], indt[temp1[4:8]]
                op += a[0]+a[1]
                break
    return op
dp1=DecryptPassword(password_1)
dp2=DecryptPassword(password_2)
p1=convert_block_to_byte(dp1+dp2)




print("\n The password is : "+p1)
