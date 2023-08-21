#replacing some alphabet/number of the whole text

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
alphabet1=alphabet.upper()
alphabet = alphabet+alphabet1
key = 'svjqhponcmlktubaxgrfdwiyez6789012345'
key1=key.upper()
key=key+key1
ciphertext = "Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa \"mxSrN03uwdd\" vwmegnm mey dngmya."

def decrypt(ciphertext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c, c) for c in ciphertext)

plaintext = decrypt(ciphertext, key, alphabet)

print(plaintext)