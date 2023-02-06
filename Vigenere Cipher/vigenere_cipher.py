def key_generator(text, alphabet, key):
    result = ''
    j = 0
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


def vigenere_encrypt(text, alphabet, key):
    result = ''
    for i in range(len(text)):
        char = text[i]
        cipher = key[i]
        if char.lower() not in alphabet:
            result += char
            i += 1
        if char.lower() in alphabet:
            cipher_index = alphabet.index(cipher)
            char_index = alphabet.index(char.lower())
            if cipher_index == 0:
                result += char
            else:
                if cipher_index + char_index >= len(alphabet):
                    result += alphabet[(cipher_index + char_index) - len(alphabet)]
                else:
                    result += alphabet[cipher_index + char_index]
    return result


def vigenere_decrypt(text, alphabet, key):
    result = ''
    for i in range(len(text)):
        char = text[i]
        cipher = key[i]
        if char.lower() not in alphabet:
            result += char
            i += 1
        if char.lower() in alphabet:
            cipher_index = alphabet.index(cipher)
            char_index = alphabet.index(char)
            if cipher_index == 0:
                result += char
            else:
                if cipher_index - char_index < 0:
                    result += alphabet[-(cipher_index - char_index)]
                else:
                    result += alphabet[char_index - cipher_index]
    return result


txt = input("Enter text: ")
key = input("Enter key: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = key_generator(txt, alphabet, key)
encrypted_txt = vigenere_encrypt(txt, alphabet, key)

print("")
print(f"origianl text: {txt}")
print(f"key: {key_generator(txt, alphabet, key)}")
print("")
print(f"encrypted: {vigenere_encrypt(txt, alphabet, key)}")
print(f"decrypted: {vigenere_decrypt(encrypted_txt, alphabet, key)}")
