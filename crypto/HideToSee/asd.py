#  steghide extract -sf atbash.jpg
import string


def atbash(text):
    alphabet = string.ascii_lowercase
    cipher_dict = {letter: alphabet[::-1][i] for i, letter in enumerate(alphabet)}
    ciphertext = "".join(cipher_dict.get(letter, letter) for letter in text.lower())
    return ciphertext


with open("encrypted.txt", "r") as f:
    c = f.readline()
    print(atbash(c))
