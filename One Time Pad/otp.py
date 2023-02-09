def key_generator(text, alphabet, key):
    result = ''
    j = 0
    if len(key) > len(text):
        for i in range(len(text)):
            char = text[i]
            if j >= len(key):
                j = 0
            if char.lower() in alphabet:
                char = key.lower()[j]
                j += 1
                result += char.lower()
            if char not in alphabet:
                result += char
                j += 1
    if len(text) == len(key):
        return key
    if len(text) > len(key):
        for i in range(len(text)):
            char = text[i]
            if j >= len(key):
                j = 0
            if char.lower() in alphabet:
                char = key.lower()[j]
                j += 1
                result += char.lower()
            if char not in alphabet:
                result += char
                j += 1
    return result

def otp_encrypt(text, alphabet, key):
    result = ''
    for i in range(len(text)):
        char = text[i]
        cipher = key[i]
        char_idx = alphabet.index(char.lower())
        cipher_idx = alphabet.index(cipher)
        last = char_idx + cipher_idx
        if last <= 25:
            if char.islower():
                result += alphabet[last]
            elif char.isupper():
                result += alphabet[last].upper()
        elif last >= 26:
            if char.islower():
                result += alphabet[last - 26]
            elif char.isupper():
                result += alphabet[last - 26].upper()
    return result

def otp_decrypt(text, alphabet, key):
    result = ''
    for i in range(len(text)):
        char = text[i]
        cipher = key[i]
        char_idx = alphabet.index(char.lower())
        cipher_idx = alphabet.index(cipher)
        last = char_idx - cipher_idx
        if last >= 0:
            if char.islower():
                result += alphabet[last]
            elif char.isupper():
                result += alphabet[last].upper()
        elif last < 0:
            if char.islower():
                result += alphabet[last + 26]
            elif char.isupper():
                result += alphabet[last + 26].upper()
    return result


alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input('Enter the text: ')
key = input('Enter key: ')
keyy = key_generator(text, alphabet, key)
which = input('Encrypt or decrypt: ')
if which == "encrypt" or which == "ENCRYPT":
    print(otp_encrypt(text, alphabet, keyy))
elif which == "decrypt" or which == "DECRYPT":
    print(otp_decrypt(text, alphabet, keyy))
