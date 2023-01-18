def caesar_cypher(text, alphabet, s):
    result = ''
    if s == 0:
        return text
    for i in range(len(text)):
        char = text[i]
        if char.lower() in alphabet:
            if char.islower():
                char_index = alphabet.index(char)
                if (char_index + s) >= len(alphabet):
                    a = (char_index + s) - len(alphabet)
                    char = alphabet[a]
                    result += char
                else:
                    char = alphabet[char_index + s]
                    result += char
            if char.isupper():
                char_index = alphabet.index(char.lower())
                if (char_index + s) >= len(alphabet):
                    a = (char_index + s) - len(alphabet)
                    char = alphabet[a]
                    result += char.upper()
                else:
                    char = alphabet[char_index + s]
                    result += char.upper()
        if char not in alphabet:
            result += char
    return result

def caesar_decrypt(text, alphabet, s):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.lower() in alphabet:
            if char.islower():
                char_index = alphabet.index(char)
                if (char_index - s) < 0:
                    a = len(alphabet) + (char_index - s)
                    char = alphabet[a]
                    result += char
                else:
                    char = alphabet[char_index - s]
                    result += char
            if char.isupper():
                char_index = alphabet.index(char.lower())
                if (char_index - s) < 0:
                    a = len(alphabet) + (char_index - s)
                    char = alphabet[a]
                    result += char.upper()
                else:
                    char = alphabet[char_index - s]
                    result += char.upper()
        if char not in alphabet:
            result += char
    return result


text = input("Enter the text you want to encrypt: ")
s = int(input("Enter the key value: "))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

encrypted = caesar_cypher(text, alphabet, s)

print(f"Original text: {text}")
print(f"Shifted: {s}")
print("")
print(f"Encrypted: {caesar_cypher(text, alphabet, s)}")
print(f"Decrypted: {caesar_decrypt(encrypted, alphabet, s)}")