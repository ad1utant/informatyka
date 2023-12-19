p = int(input())
if p <= 0:
    exit()
a = 1
b = p/a
x = -1
while True:
    a = (a+b)/2
    b = p/a
    if p == a or x == a:
        break
    x = a
    print(a)
