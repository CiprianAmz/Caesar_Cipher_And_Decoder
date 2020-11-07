"""Author: Amzuloiu Andrei-Ciprian"""

from text_analysis.text_analysis import analyse_text_by_letters

"""Constant used to initialize the dictionary before shifting"""
LETERS = {'a' : 'a', 
        'b' : 'b', 
        'c' : 'c', 
        'd' : 'd', 
        'e' : 'e', 
        'f' : 'f', 
        'g' : 'g', 
        'h' : 'h', 
        'i' : 'i', 
        'j' : 'j', 
        'k' : 'k',
        'l' : 'l',
        'm' : 'm',
        'n' : 'n', 
        'o' : 'o',
        'p' : 'p',
        'q' : 'q',
        'r' : 'r',
        's' : 's',
        't' : 't',
        'u' : 'u',
        'v' : 'v',
        'w' : 'w',
        'x' : 'x',
        'y' : 'y',
        'z' : 'z'}

"""Shift the values of the given dictionary using the given value. It is valid only for the alphabed a-z dictionary template."""
def shift_dictionary(dictionary, value):
    for i in range(len(dictionary)):
        current_char = dictionary[chr(ord('a') + i)]
        dictionary[chr(ord('a') + i)] = chr((ord(current_char) - ord('a') + value) % len(dictionary) + ord('a'))

"""Encrypt the text using the given key"""
def encrypt(text, key):
    LetersDictionary = LETERS.copy()
    shift_dictionary(LetersDictionary, key)
    
    text = text.lower()
    newText = ''
    for i in text:
        if LetersDictionary.get(i, -1) == -1:
            newText += i
        else:
            newText += LetersDictionary[i]

    return newText.upper()

"""Decrypt based on text and key"""
def decrypt(text, key):
    result = encrypt(text, (-1) * key)
    return result

"""Decrypt using brute force"""
def brute_force_decrypt(text):
    result = []
    for i in range(len(LETERS) - 1):
        result.append(("+" + str(len(LETERS) - i - 1), decrypt(text, i + 1)))

    return result

"""Decrypt based on the most common letter (check the READ ME file)"""
def decrypt_based_on_common_letter(text):
    apparitions = analyse_text_by_letters(text)

    max_ap = max(apparitions, key=apparitions.get)

    result = decrypt(text, ord(max_ap) - ord('e'))
    return result
    