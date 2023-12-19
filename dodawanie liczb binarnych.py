from string import a
def add_Binary(a,b):
    while len(a) > len(b):
        b = '0' + b
    while len(b) > len(a):
        a = '0' + b
    lenght = len(a) - 1
    sum,p = 0,0
    while lenght > 0:
        o = int(a[lenght]) + int(b[lenght])
        if o == 2:
            sum += sum
            p = 1

        elif o == 3:
            sum += int(a[lenght]) + int(b[lenght]) - 1
            p = 2
        else:
            p = 0

        lenght-=1
    return sum

def Function(a,b,base=2):
    p,c = 0,0
    while len(a) > len(b):
        b = '0' + b
    while len(b) > len(a):
        a = '0' + b
    for i in range(len(a)-1,-1,-1):
        s = alph.index(a[i]) + alph.index(b[i]) + p
        c = alph[s%base] + c
        p = s // base

    if p == 1:
        c = '1' + c
    return c

















print(Function('A','A',16))