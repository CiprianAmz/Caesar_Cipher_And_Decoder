"""Author: Amzuloiu Andrei-Ciprian"""

from text_analysis.text_analysis import analyse_text_by_letters, analyse_text_by_symbols, read_data
from caesar_cypher.caesar_cypher import encrypt, decrypt, brute_force_decrypt, decrypt_based_on_common_letter
import pandas as pd
import matplotlib.pyplot as plt

INPUT_TEXT_FILE_PATH = "input_data/input.txt"
ENCRYPTED_TEXT_FILE_PATH = "output_data/encrypted_text.txt"
BRUTE_FORCE_RESULT_PATH = "output_data/brute_force_result.txt"
SIMPLE_DECRYPTION_RESULT_PATH = "output_data/simple_decrypt_result.txt"
MOST_APPARITIONS_RESULT_PATH = "output_data/most_apparitions_decrypt_result.txt"
OUTPUT_CSV_PATH = "output_data/output.csv"
OUTPUT_GRAPH1_PATH = "output_data/graphByApparitions.png"
OUTPUT_GRAPH2_PATH = "output_data/graphByPercentage.png"

"""Needed operations for options 1 and 2"""
def apparition_option(data, target = "Letter"): 
    # Add the percentage column
    data = data.rename(columns={0: target, 1 : 'Apparitions'})
    percentage = data['Apparitions'] / sum(i for i in data['Apparitions']) * 100
    data['Percentage'] = percentage

    # Plot the computed data, show it and save it
    app_pivot = data.pivot_table(index = target, values = 'Apparitions')
    app_pivot.plot(kind = 'bar', color = 'blue')
    plt.savefig(OUTPUT_GRAPH1_PATH)
    plt.show()

    app_pivot = data.pivot_table(index = target, values = 'Percentage')
    app_pivot.plot(kind = 'bar', color = 'blue')
    plt.savefig(OUTPUT_GRAPH2_PATH)
    plt.show()
    
    data.to_csv(OUTPUT_CSV_PATH)

    print("The results were saved in output_data folder.")

"""The main function"""
def main():
    print("1 - Check the appations of all symbols \n\
2 - Check the apparitions of letters only\n\
3 - Encrypt the input file\n\
4 - Decrypt the file encrypted file using brute force\n\
5 - Decrypt the file encrypted file using an input key\n\
6 - Decrypt the file based on the letter with the most apparitions (read more about this in ReadMe file)*\n\
Other - Exit\n\
Enter your option: ")
    
    while(True):
        option = int(input())
        text = read_data(INPUT_TEXT_FILE_PATH)

        if option == 1:
            data = pd.DataFrame(analyse_text_by_symbols(text).items())
            target = "Symbol"
            apparition_option(data, target)
        elif option == 2:
            data = pd.DataFrame(analyse_text_by_letters(text).items())
            target = "Letter"
            apparition_option(data, target)
        elif option == 3:
            print("Enter the key: ")
            key = int(input())
            encrypted_text = encrypt(text, key)
            file = open(ENCRYPTED_TEXT_FILE_PATH, 'w')
            file.write(encrypted_text)
            file.close()

            print("Result saved in " + ENCRYPTED_TEXT_FILE_PATH)
        elif option == 4:
            file = open(ENCRYPTED_TEXT_FILE_PATH, 'r')
            encrypted_text = file.read()
            file.close()

            file = open(BRUTE_FORCE_RESULT_PATH, 'w')
            for i in brute_force_decrypt(encrypted_text):
                file.write("Shift: " + i[0] + " -->\n" + i[1] + "\n")
                file.write("\n-------------------------------\n")
            file.close()

            print("Result saved in " + BRUTE_FORCE_RESULT_PATH)
        elif option == 5:
            print("Enter the key: ")
            key = int(input())
            file = open(ENCRYPTED_TEXT_FILE_PATH, 'r')
            encrypted_text = file.read()
            file.close()

            file = open(SIMPLE_DECRYPTION_RESULT_PATH, 'w')
            file.write(decrypt(encrypted_text, key))
            file.close()

            print("Result saved in " + SIMPLE_DECRYPTION_RESULT_PATH)
        elif option == 6:
            file = open(ENCRYPTED_TEXT_FILE_PATH, 'r')
            encrypted_text = file.read()
            file.close()

            file = open(MOST_APPARITIONS_RESULT_PATH, 'w')
            file.write(decrypt_based_on_common_letter(encrypted_text))
            file.close()

            print("Result saved in " + MOST_APPARITIONS_RESULT_PATH)
        else:
            break

if __name__ == "__main__":
    main()