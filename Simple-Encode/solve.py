import string
import hashlib

enc = '10010111001101100000111110111010001011000111000101010110110001101101001011100101110000111010110101111000101111001111110100000010001111000111011011011110101011111110011000111110111101001001000100011010001101111101'
target_hash = '16ab78b0c0654e663d7e2e22ac0a9b7a'
printable_chars = string.printable[:-6]

def md5_hash(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

def find_all_strings(binary_string, current_string, index):
    if index == len(binary_string):
        current_hash = md5_hash(current_string)
        if current_hash == target_hash:
            print("Flag:", current_string)
        return

    for char in printable_chars:
        char_binary_6bit = bin(ord(char))[2:].zfill(6)
        char_binary_7bit = bin(ord(char))[2:].zfill(7)

        if binary_string.startswith(char_binary_6bit, index):
            find_all_strings(binary_string, current_string + char, index + len(char_binary_6bit))
        elif binary_string.startswith(char_binary_7bit, index):
            find_all_strings(binary_string, current_string + char, index + len(char_binary_7bit))

find_all_strings(enc, "", 0)