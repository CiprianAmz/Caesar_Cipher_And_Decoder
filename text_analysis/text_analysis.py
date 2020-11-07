"""Author: Amzuloiu Andrei-Ciprian"""

import regex as re

"""Read the data from txt file.

Used to read the data from the specified path. If the parameter is not given, it reads from the default input path.
"""
def read_data(file_name = "input_data/input.txt"):
    try:
        file = open(file_name, "r")
        content = file.read()
        file.close()
        return content
    except:
        print("File not found. An empty string is returned.")
        return ""

"""Count the appariotion of all the text symbols."""
def analyse_text_by_symbols(text_input):
    data = dict()

    for i in text_input:
        if data.get(i, -1) == -1:
            data.update({i: 1})
        else:
            data[i] += 1

    return data

"""Count the appariotion of all the text letters."""
def analyse_text_by_letters(text_input):
    # Define a dictionary to store the apparitions
    data = { "a" : 0, 
            "b" : 0, 
            "c" : 0, 
            "d" : 0, 
            "e" : 0, 
            "f" : 0, 
            "g" : 0, 
            "h" : 0, 
            "i" : 0, 
            "j" : 0, 
            "k" : 0, 
            "l" : 0, 
            "m" : 0, 
            "n" : 0, 
            "o" : 0, 
            "p" : 0,
            "q" : 0,
            "r" : 0,
            "s" : 0,
            "t" : 0,
            "u" : 0,
            "v" : 0,
            "w" : 0,
            "x" : 0,
            "y" : 0,
            "z" : 0
            }
    
    # Clean the text input
    formated_text = text_input.lower()
    formated_text = re.sub("/s", "", formated_text)
    formated_text = re.sub("/n/t", "", formated_text)
    formated_text = re.sub("[^a-z]", "", formated_text)
    
    # Parse the text input and count the letters
    for i in formated_text:
        data[i] += 1

    return data
