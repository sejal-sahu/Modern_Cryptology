#frequency analysis of given plaintext

import operator

ciphertext = "Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa \"mxSrN03uwdd\" vwmegnm mey dngmya."
temp={}
for char in ciphertext:
    if char.isalpha():
        temp[char.lower()]=temp.get(char.lower(),0)+1
res=dict(sorted(temp.items(), key=operator.itemgetter(1),reverse=True))
for key,value in res.items():
    print("{} -> {:.1f}%".format(key, value/len(ciphertext)*100))

