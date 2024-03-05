class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded_text = ""
        length_text = len(text)
        length_key = len(self.key)
        whole, unity = length_text // length_key, length_text % length_key
        word = self.key * whole + self.key[:unity]
        alphabet_index = {letter: i for i, letter in enumerate(self.alphabet)}


        for i, letter in enumerate(word):
            if text[i] not in self.alphabet:
                encoded_text += text[i]
            else:
                index1 = alphabet_index[letter]
                index2 = alphabet_index[text[i]]
                encoded_text += self.alphabet[(index1 + index2) % len(self.alphabet)]
        return encoded_text



    def decode(self, text):
        decoded_text = ""
        length_text = len(text)
        length_key = len(self.key)
        whole, unity = length_text // length_key, length_text % length_key
        word = self.key * whole + self.key[:unity]
        alphabet_index = {letter: i for i, letter in enumerate(self.alphabet)}

        for i, letter in enumerate(word):
            if text[i] not in self.alphabet:
                decoded_text += text[i]
            else:
                index1 = alphabet_index[letter]
                index2 = alphabet_index[text[i]]

                decoded_text += self.alphabet[(index2 - index1) % len(self.alphabet)]
        return decoded_text


def result(keyword, alphabet, action, text):
    if action == '1' or action == "encode":
        print(VigenereCipher(keyword, alphabet).encode(text))
    elif action == '2' or action == "decode":
        print(VigenereCipher(keyword, alphabet).decode(text))

    repeat = input("Do you want to use Cipher again? (y/n): ")
    if repeat == 'y':
        action = input("1. encode \n2. decode ")
        text = input("Enter text to Encode/Decode: ")
        result(keyword, alphabet, action, text)




alphabet = input("Enter alphabet (Leave blank to enter English alphabet): ")
if alphabet == "":
    alphabet = "abcdefghijklmnopqrstuvwxyz"

result(input("Enter keyword: "), alphabet, input("1. encode \n 2. decode "), input("Enter text to Encode/Decode: "))

