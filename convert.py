import string

num = input("type a number in any numeral system: ")
bp = int(input('type a numeral system: '))
#convert any base type to decimal
def convert_to_decimal(num,bp):
    j = 0
    result = 0
    digits = string.digits + string.ascii_uppercase
    for i in num[::-1]:
        i = int(i)
        result += i * bp ** j
        j+=1
    return result
print(convert_to_decimal(num,bp))