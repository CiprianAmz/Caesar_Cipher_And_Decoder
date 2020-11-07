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
        target = "Symbol"
    else:
        data = pd.DataFrame(analyse_text_by_letters(read_data("input_data/input.txt")).items())
        target = "Letter"

    # Add the percentage column
    data = data.rename(columns={0: target, 1 : 'Apparitions'})
    percentage = data['Apparitions'] / sum(i for i in data['Apparitions']) * 100
    data['Percentage'] = percentage

    # Plot the computed data, show it and save it
    app_pivot = data.pivot_table(index = target, values = 'Apparitions')
    app_pivot.plot(kind = 'bar', color = 'blue')
    plt.savefig("output_data/graphByAparitions.png")
    plt.show()

    app_pivot = data.pivot_table(index = target, values = 'Percentage')
    app_pivot.plot(kind = 'bar', color = 'blue')
    plt.savefig("output_data/graphByPercentage.png")
    plt.show()
    
    data.to_csv("output_data/output.csv")

    print("The results were saved in output_data folder.")

if __name__ == "__main__":
    main()