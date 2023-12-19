#factorization
def factorization(x):
    list = []
    if x < 2:
        False
    i = 2
    while i <= x:
        if x % i == 0:
            list.append(i)
            x /= i
        else:
            i+=1
    return list



#check if num is prime
def is_prime(x):
    if x < 2:
        False
    if x == 2:
        True
    for i in (3,x-1,2):
        if x % i == 0:
            return False
        else:
            return True



def eratostenes(x):
    list = []
    for i in range(2,x):
        list.append(True)
    for i in range(2,x):






if __name__ == '__main__':
    #print(is_prime(int(input())))
    #print(factorization(int(input())))
    print(eratostenes(int(input())))