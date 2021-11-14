# Name: Chandler Hobby
# Course: Data Mining
# Section: 01
# Semester: Fall 2021
# Assignment: Term Project, Evaluating Xbox Game Sales

import csv

if __name__ == '__main__':
    # Below is the importation of the csv that contains the Xbox Game Sales data set, along with
    # the declaration of the file reader and the storage arrays
    with open('XboxOne_GameSales.csv', encoding='unicode_escape') as f:
        csv_read_1 = csv.reader(f)

        best_sell = []
        decent_sell = []
        poor_sell = []
        lowest_sell = []
        zero = []
        # For loop to iterate through the csv file. Reads the Global Sales recorded and classifies each
        # game based on their global sales. The header line prints the title of the project
        for line_no, line in enumerate(csv_read_1, 1):
            if line_no == 1:
                print("Categorization of Video Games, Based on Global Sales : Xbox Series")
            elif float(line[9]) >= 4.00:
                best_sell.append(line[1])
            elif 4.00 > float(line[9]) >= 2.00:
                decent_sell.append(line[1])
            elif 2.00 > float(line[9]) >= 1.00:
                poor_sell.append(line[1])
            elif 1.00 > float(line[9]) > 0.00:
                lowest_sell.append(line[1])
            elif float(line[9]) <= 0.00:
                zero.append(line[1])
        # Each of these loops below prints the contents of the storage arrays. Game titles are categorized
        # into one of the five arrays based on their popularity: Best Selling, Decent Selling, Poor Selling
        # Lowest Selling, and Zero Sales. The program also records what percentage each game category makes
        # up of the total amount of games on record.
        print("\nBest Selling Games, Units Sold Above 4.00 Million Copies")
        print("--------------------------------------------------------")
        for x in range(len(best_sell)):
            print(x + 1, ".", best_sell[x])
        print("Accounts for ", round(len(best_sell) / 613, 2) * 100, "% of Games in Records")

        print("\nDecent Selling Games, Units Sold Between 4.00 and 2.00 Million Copies")
        print("--------------------------------------------------------------")
        for x in range(len(decent_sell)):
            print(x + 1, ".", decent_sell[x])
        print("Accounts for ", round(len(decent_sell) / 613, 2) * 100, "% of Games in Records")

        print("\nPoor Selling Games, Units Sold Between 2.00 and 1.00 Million Copies")
        print("---------------------------------------------------------------------")
        for x in range(len(poor_sell)):
            print(x + 1, ".", poor_sell[x])
        print("Accounts for ", round(len(poor_sell) / 613, 2) * 100, "% of Games in Records")

        print("\nLowest Selling Games, Units Sold At or Below 1.00 Million Copies")
        print("---------------------------------------------------------")
        for x in range(len(lowest_sell)):
            print(x + 1, ".", lowest_sell[x])
        print("Accounts for ", round(len(lowest_sell) / 613, 2) * 100, "% of Games in Records")

        print("\nGames with No Copies Sold")
        print("------------------------")
        for x in range(len(zero)):
            print(x + 1, ".", zero[x])
        print("Accounts for ", round(len(zero) / 613, 2) * 100, "% of Games in Records")
