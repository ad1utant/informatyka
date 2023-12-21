#column_cipher
def column_cipher(prompt,key):
    text = ''
    prompt = prompt + 'X' * (key - (len(prompt) % key))
    prompt = prompt.upper()

    for i in range(key):
        for j in range (i,len(prompt),key):
            text += prompt[j]
    return text

print(column_cipher('ala ma kota i psa',4))
