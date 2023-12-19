"""
s = {}
o = int(input('podaj liczbe wyrazow '))
x = int(input('podaj x '))
result = 0
for i in range(o):
    y = int(input('podaj wspolczynnik '))
    w = int(input('podaj wykladnik '))
    s[w] = y
print(s)
for i in s:
    result += s[i] * x ** i
print(result)
"""

s = {}
lw = int(input('podaj liczbe wyrazow '))
x = int(input('podaj x '))
for i in range(lw):
    wsp = int(input("podaj współczynnik "))
    wyk = int(input(f"podaj wykładnik dla wyrazu {wsp} "))
    s[wyk] = wsp
maxi = max(s)
range = max(int(s)) - 1
result = max(s)
for i in range(range,-1):
    result *= x
    del(s[maxi])
    maxi = max(s)
    result += s[maxi]



print(s,maxi)
