import string
from itertools import permutations

encoded_message = 'acbc'
decoded_message = ''

words_sjp = set()
with open('slowa.txt','r') as ff:
    for i in ff:
        if len(i) == 5:
            words_sjp.add(i)

current_dict = {}

def cipher_permutations(alphabet, encoded_message, decoded_message):
    input_list = list(alphabet)
    all_permutations = permutations(input_list)
    print(all_permutations)

    for perm in all_permutations:
        current_dict = {
            ' ' : ' ',
            'a' : perm[0],
            'b' : perm[1],
            'c' : perm[2]

        }




        for letter in encoded_message:
            for key, value in current_dict.items():
               if key == letter:
                    decoded_message += value
                    break
        print(decoded_message)
        decoded_message = ''




# Example usage with a smaller set for demonstration purposes






#
# alphabet = string.ascii_uppercase
# list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25]
# archive,all = [],[]
# file = open('newKod.txt','w')
#
#
#     list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25]
#     newKod = ''

    #
    # if dict not in all:
    #     all.append(dict)
    #     if kod in set and kod1 in set:
    #         print(dict)
    #         print(newKod)
    #         file.write(newKod)
    #         file.write(str(dict))
    #         file.write('\n')
    #
    # else:
    #     x +=1

cipher_permutations('abc', encoded_message, decoded_message)