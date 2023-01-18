<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. 
A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. 
The encryption of the original text is done using the Vigenère square or Vigenère table.

<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

Vigenere Cipher in Python

The table consists of the alphabets written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar Ciphers.
At different points in the encryption process, the cipher uses a different alphabet from one of the rows.
The alphabet used at each point depends on a repeating keyword.

For generating key, the given keyword is repeated
in a circular manner until it matches the length of 
the plain text.

<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
