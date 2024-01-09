kod = 'OPYIRYUN'
kod1 = 'ABNUSWBN'
import string
import random
set = set()
with open('slowa.txt','r') as ff:
    for i in ff:
        if len(i) == len(kod):
            set.add(i)

alphabet = string.ascii_uppercase
list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25]
archive,all = [],[]
file = open('newKod.txt','w')

#kod = 'f''JFRENUPAN ABNUSWBN SW SFWCPN OPYIRYUN, ASWCN WMPQVGF YNREWBNUPF QPF JNZIRE WLPFASWB, SNAPRE GNA QVLNSWJI, RYNQSAP P OWSWUI, UN QANZP JPACWQAWMWBFG. YWQSNZN WUN WMCNRWBNUN B ZNSNRE 20. HH BPFAV P GFQS WLFRUPF MWXQSNBN BPFZV XYPFXYPU OPYIAP, B SIJ OPYIAP GNXCWBFG, OPYIAP RPNZN QSNZFDW, OPYIAP NSWJWBFG P OPYIAP WMSIRYUFG.
#JFRENUPAN ABNUSWBN WMPFCN QPF UN APZAV MWXQSNBWBIRE YNZWYFUPNRE, SNAPRE GNA UPFWYUNRYWUWQR EFPQFULFCDN, ASWCN JWBP, YF UPF JWYUN XWAZNXUPF YJPFCYIR GFXUWRYFQUPF WLV BPFZAWQRP OPYIRYUIRE, SNAPRE GNA MWZWYFUPF P MFX, WCNY YGNBPQAW PUSFCOFCFURGP ABNUSWBFG, ASWCF WMPQVGF QMWQWL, B GNAP ONZWBI RENCNASFC RYNQSFA JWYF MCWBNXYPR XW YGNBPQAN PUSFCOFCFURGP B OPYIRF AZNQIRYUFG.
#JFRENUPAN ABNUSWBN XNGF UNJ SNAYF JWYZPBWQR WMPQNUPN UPFASWCIRE XYPBUIRE YGNBPQA, SNAPRE GNA SVUFZWBNUPF ABNUSWBF, DXYPF RYNQSAN JWYF "MCYFUPAUNR" MCYFY LNCPFCF, ASWCN BFXZVD JFRENUPAP AZNQIRYUFG LIZNLI UPFJWYZPBN XW MCYFACWRYFUPN. GFQS SW GFXUN Y UNGBNYUPFGQYIRE SFWCPP OPYIRYUIRE BQMWZRYFQUFG UNVAP P JN AZVRYWBF YUNRYFUPF XZN YCWYVJPFUPN BPFZV YGNBPQA YNREWXYNRIRE B UNQYIJ QBPFRPF.'''


print(kod)
newKod = ''
x = 0
for i in range(26**26 + x):
    dict = {' ' : ' '}
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25]
    newKod = ''
    #creating new cipher key
    for i in range(26):
       randomIndex = random.choice(list)
       newLetter = alphabet[randomIndex]
       list.pop()
       dict[alphabet[i]] = newLetter


    for j in range(len(kod)):
       for i in dict:
           if i == kod[j]:
               newKod += dict[i]
               break
    if dict not in all:
        all.append(dict)
        if kod in set and kod1 in set:
            print(dict)
            print(newKod)
            file.write(newKod)
            file.write(str(dict))
            file.write('\n')

    else:
        x +=1
