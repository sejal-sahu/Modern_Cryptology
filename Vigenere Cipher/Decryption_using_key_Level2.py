
def Decrypted_Text(cipher_text, key):
    orig_text = []
    j=0
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            if cipher_text[i].isupper():
                x = (ord(cipher_text[i]) -
                     ord(key[j%10].upper()) + 26) % 26
                x += ord('A')
            else:
                x = (ord(cipher_text[i]) -
                     ord(key[j%10]) + 26) % 26
                x += ord('a')
            orig_text.append(chr(x))
            
            j+=1
        else:
            orig_text.append(cipher_text[i])
    return("" . join(orig_text))
string="Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg. Urfjm xwy yjg rbbufqwi \"vjg_djxn_ofs_dg_rmncbgi\" yq iq uqtxwlm. Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv, aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj."

print(string)
keyword="jcjcffcccb"
print("Decrypted Text :",
           Decrypted_Text(string, keyword))