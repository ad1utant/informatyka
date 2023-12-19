def g(x):
    return x ** 3 - 6 * 2 ** x + 4 * x + 12

a,b = 3,5

def find_zero_of_function(a,b,f):
    s = (a+b) / 2
    while abs(f(s)) > 0:
        if f(a) * f(s) < 0 :
            b = s
        else:
            a = s
        s = (a+b)/2
    return s

print(find_zero_of_function(a,b,g))