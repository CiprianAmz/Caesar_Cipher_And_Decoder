"""Author: Amzuloiu Andrei-Ciprian"""

from text_analysis.text_analysis import analyse_text_by_letters, analyse_text_by_symbols, read_data
import pandas as pd
import matplotlib.pyplot as plt

"""The main function"""
def main():
    print("1 - Check the appations of all symbols \n\
Any other key - Check the apparitions of letters only\n\
Enter your option: ")

    # Read the imput option and base on that check the number of apparitions
    if int(input()) == 1:
        data = pd.DataFrame(analyse_text_by_symbols(read_data("input_data/input.txt")).items())
        data = data.rename(columns={0: 'Symbol', 1 : 'Apparitions'})
        app_pivot = data.pivot_table(index = 'Symbol', values = 'Apparitions')
    else:
        data = pd.DataFrame(analyse_text_by_letters(read_data("input_data/input.txt")).items())
        data = data.rename(columns={0: 'Letter', 1 : 'Apparitions'})
        app_pivot = data.pivot_table(index = 'Letter', values = 'Apparitions')

    # Plot the computed data and show it
    app_pivot.plot(kind = 'bar', color = 'blue')
    plt.savefig("output_data/graph.png")

    # Save the results
    plt.show()
    data.to_csv("output_data/output.csv")

    print("The results were saved in output_data folder.")

if __name__ == "__main__":
    main()