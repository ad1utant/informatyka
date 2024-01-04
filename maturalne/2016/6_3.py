import string


def test_keys(word1, word2):
    alphabet = string.ascii_uppercase + string.ascii_uppercase
    i = alphabet.index(word1[0])
    j = alphabet.index(word2[0])
    k = j - i
    for c1, c2 in zip(word1[1:], word2[1:]):
        i = alphabet.index(c1)
        j = alphabet.index(c2, i)
        if j - k != 0:
            return False
        return True

with open('informatyka-2016-maj-matura-rozszerzona-zalaczniki','r') as ff:
    pass