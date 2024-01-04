import string

LETTERS_AND_SPACE = string.ascii_uppercase + string.ascii_lowercase + ' \t\n'

def load_dict(file_dict):
    with open(file_dict, 'r', encoding='utf8') as ff:
        english_dict = {}
        for word in ff:
            english_dict.setdefault(word.strip())
    return english_dict

english_dict = load_dict('dictionary.txt')

def count_words(text):
    text = remove_nonletters(text).upper()
    posible_words = text.split()
    count = 0

    if len(posible_words) == 0:
        return 0.0

    for word in posible_words:
        if word in english_dict:
            count += 1
    return count/len(posible_words)

def is_english(text, word_p = 60, word_)



def remove_nonletters(text):
    letters_only = []
    for ch in text:
        if ch in LETTERS_AND_SPACE:
            letters_only.append(ch)
    return "".join(letters_only)

print(x)
