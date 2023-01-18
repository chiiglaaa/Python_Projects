# Caesar Cypher Brute Force using for loops *'Python'*


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


def caesar_bruteforce():
    for i in range(1, 26):
        print(f"Key {i}: {caesar_decrypt(encrypted, alphabet, i)}")


alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted = input("Enter the encrypted message: ")

print(caesar_bruteforce())
