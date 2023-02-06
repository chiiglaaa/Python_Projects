import vigenereModule, sys
# vigenereModule is the vigenere_cipher file also made by me

iterationlimiter = sys.getrecursionlimit() + 44333
sys.setrecursionlimit(iterationlimiter) # in here we are increasing the recursion limit to 45333 bc we have 45333 word in our dictionary file
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dictionaryy = open("/home/chiiglaaa/Desktop/dictionary", "r") # you have to download the dictionary.txt file in order to use this code and make sure to use the correect path
Lines = dictionaryy.readlines()
encryptedtext = input("Enter the encrypted text: ")
count = 0
readedlines = ''


def dictionary_attack(text, alphabet, Lines, count):
    print("\033[34m" + text, "<--> Encrypted Text" + "\033[0m")
    readedlines = ''
    for line in Lines:
        readedlines += line.strip()
        readedlines += ' '
        count += 1
        key = vigenereModule.key_generator(encryptedtext, alphabet, key=line.strip())
        print("\033[33m" + key, "<--> Generated Key", count, "\033[0m")
        decrypted = vigenereModule.vigenere_decrypt(text, alphabet, key)
        print("\033[31m" + decrypted, "<--> Decrypted Text" + "\033[0m")
        print("\033[32m" + '     <=-=-=-=-=-=-=-=-=-=-=-=->' + "\033[0m")
        print()
        while True:
            checker = input("Check if the decrypted text is making sense and answer with Y/N: ")
            if checker == "y" or checker == "Y":
                print("Decrypted Text is: ", decrypted)
                print("Key is: ", line.strip())
                return ''
            if checker == "N" or checker == "n":
                break
            if checker != "N" or checker != "n":
                print("Try again")

print(dictionary_attack(encryptedtext, alphabet, Lines, count))
