# Name: Chandler Hobby
# Course: Data Mining
# Section: 01
# Semester: Fall 2021
# Assignment: Term Project, Evaluating Xbox Game Sales

import csv

if __name__ == '__main__':
    # Below is the importation of the csv that contains the Xbox Game Sales data set, along with
    # the declaration of the file reader
    with open('XboxOne_GameSales.csv', encoding='unicode_escape') as f:
        csv_read_1 = csv.reader(f)
        # Each of the arrays below represents a classification level for game sales. There are also array
        # sets to store the genre of each game that is classified at each level.
        best_sell = []
        bgame_genre = []
        decent_sell = []
        dgame_genre = []
        poor_sell = []
        pgame_genre = []
        lowest_sell = []
        lgame_genre = []
        zero = []
        zgame_genre = []

        s_count = 0
        a_count = 0
        sp_count = 0
        r_count = 0
        m_count = 0

        def resetVar():
            global s_count, a_count, sp_count, r_count, m_count
            s_count -= s_count
            a_count -= a_count
            sp_count -= sp_count
            r_count -= r_count
            m_count -= m_count

        # For loop to iterate through the csv file. Reads the Global Sales recorded and classifies each
        # game based on their global sales and stores their respective genre.
        # The header line prints the title of the project
        for line_no, line in enumerate(csv_read_1, 1):
            if line_no == 1:
                print("Categorization of Video Games, Based on Global Sales : Xbox Series")
            elif float(line[9]) >= 4.00:
                best_sell.append(line[1])
                bgame_genre.append(line[3])
            elif 4.00 > float(line[9]) >= 2.00:
                decent_sell.append(line[1])
                dgame_genre.append(line[3])
            elif 2.00 > float(line[9]) >= 1.00:
                poor_sell.append(line[1])
                pgame_genre.append(line[3])
            elif 1.00 > float(line[9]) > 0.00:
                lowest_sell.append(line[1])
                lgame_genre.append(line[3])
            elif float(line[9]) <= 0.00:
                zero.append(line[1])
                zgame_genre.append(line[3])
        # Each of these loops below prints the contents of the storage arrays. Game titles are categorized
        # into one of the five arrays based on their popularity: Best Selling, Decent Selling, Poor Selling
        # Lowest Selling, and Zero Sales. The program also records what percentage each game genre makes up each level
        # of popularity, which can be used for further analysis later.
        print("\nBest Selling Games, Units Sold Above 4.00 Million Copies")
        print("--------------------------------------------------------")
        for x in range(len(best_sell)):
            print(x + 1, ".", best_sell[x], "\t|\tGenre: ", bgame_genre[x])
            if bgame_genre[x] == "Shooter":
                s_count += 1
            elif bgame_genre[x] == "Sports":
                sp_count += 1
            elif bgame_genre[x] == "Racing":
                r_count += 1
            elif bgame_genre[x] == "Action" or bgame_genre[x] == "Action-Adventure":
                a_count += 1
            else:
                m_count += 1
        print("Shooter Genre Accounts for ", round(s_count / len(bgame_genre), 2) * 100, "% of Best Selling Games.")
        print("Sports Genre Accounts for ", round(sp_count / len(bgame_genre), 2) * 100, "% of Best Selling Games.")
        print("Racing Genre Accounts for ", round(r_count / len(bgame_genre), 2) * 100, "% of Best Selling Games.")
        print("Action Genre Accounts for ", round(r_count / len(bgame_genre), 2) * 100, "% of Best Selling Games.")
        print("Miscellaneous Genres Account for", round(m_count / len(bgame_genre), 2) * 100, "% of Best Selling Games")
        resetVar()

        print("\nDecent Selling Games, Units Sold Between 4.00 and 2.00 Million Copies")
        print("--------------------------------------------------------")
        for x in range(len(decent_sell)):
            print(x + 1, ".", decent_sell[x], "\t|\tGenre: ", dgame_genre[x])
            if dgame_genre[x] == "Shooter":
                s_count += 1
            elif dgame_genre[x] == "Sports":
                sp_count += 1
            elif dgame_genre[x] == "Racing":
                r_count += 1
            elif dgame_genre[x] == "Action" or dgame_genre[x] == "Action-Adventure":
                a_count += 1
            else:
                m_count += 1
        print("Shooter Genre Accounts for ", round(s_count / len(dgame_genre), 2) * 100, "% of Decent Selling Games.")
        print("Sports Genre Accounts for ", round(sp_count / len(dgame_genre), 2) * 100, "% of Decent Selling Games.")
        print("Racing Genre Accounts for ", round(r_count / len(dgame_genre), 2) * 100, "% of Decent Selling Games.")
        print("Action Genre Accounts for ", round(r_count / len(dgame_genre), 2) * 100, "% of Decent Selling Games.")
        print("Miscellaneous Genres Account for", round(m_count / len(dgame_genre), 2) * 100, "% of Decent Selling "
                                                                                              "Games")
        resetVar()

        print("\nPoor Selling Games, Units Sold Between 2.00 and 1.00 Million Copies")
        print("--------------------------------------------------------")
        for x in range(len(poor_sell)):
            print(x + 1, ".", poor_sell[x], "\t|\tGenre: ", pgame_genre[x])
            if pgame_genre[x] == "Shooter":
                s_count += 1
            elif pgame_genre[x] == "Sports":
                sp_count += 1
            elif pgame_genre[x] == "Racing":
                r_count += 1
            elif pgame_genre[x] == "Action" or pgame_genre[x] == "Action-Adventure":
                a_count += 1
            else:
                m_count += 1
        print("Shooter Genre Accounts for ", round(s_count / len(pgame_genre), 2) * 100, "% of Poor Selling Games.")
        print("Sports Genre Accounts for ", round(sp_count / len(pgame_genre), 2) * 100, "% of Poor Selling Games.")
        print("Racing Genre Accounts for ", round(r_count / len(pgame_genre), 2) * 100, "% of Poor Selling Games.")
        print("Action Genre Accounts for ", round(r_count / len(pgame_genre), 2) * 100, "% of Poor Selling Games.")
        print("Miscellaneous Genres Account for", round(m_count / len(pgame_genre), 2) * 100, "% of Poor Selling Games")
        resetVar()

        print("\nLowest Selling Games, Units Sold Between 1.00 and 0.00 Million Copies")
        print("--------------------------------------------------------")
        for x in range(len(lowest_sell)):
            print(x + 1, ".", lowest_sell[x], "\t|\tGenre: ", lgame_genre[x])
            if lgame_genre[x] == "Shooter":
                s_count += 1
            elif lgame_genre[x] == "Sports":
                sp_count += 1
            elif lgame_genre[x] == "Racing":
                r_count += 1
            elif lgame_genre[x] == "Action" or lgame_genre[x] == "Action-Adventure":
                a_count += 1
            else:
                m_count += 1
        print("Shooter Genre Accounts for ", round(s_count / len(lgame_genre), 2) * 100, "% of Lowest Selling Games.")
        print("Sports Genre Accounts for ", round(sp_count / len(lgame_genre), 2) * 100, "% of Lowest Selling Games.")
        print("Racing Genre Accounts for ", round(r_count / len(lgame_genre), 2) * 100, "% of Lowest Selling Games.")
        print("Action Genre Accounts for ", round(r_count / len(lgame_genre), 2) * 100, "% of Lowest Selling Games.")
        print("Miscellaneous Genres Account for", round(m_count / len(lgame_genre), 2) * 100, "% of Lowest Selling "
                                                                                              "Games")
        resetVar()
        print("\nGames with Zero Copies Sold")
        print("---------------------------")
        for x in range(len(zero)):
            print(x + 1, ".", zero[x], "\t|\tGenre: ", zgame_genre[x])
            if zgame_genre[x] == "Shooter":
                s_count += 1
            elif zgame_genre[x] == "Sports":
                sp_count += 1
            elif zgame_genre[x] == "Racing":
                r_count += 1
            elif zgame_genre[x] == "Action" or zgame_genre[x] == "Action-Adventure":
                a_count += 1
            else:
                m_count += 1
        print("Shooter Genre Accounts for ", round(s_count / len(zgame_genre), 2) * 100, "% of Games with Zero Sales.")
        print("Sports Genre Accounts for ", round(sp_count / len(zgame_genre), 2) * 100, "% of Games with Zero Sales.")
        print("Racing Genre Accounts for ", round(r_count / len(zgame_genre), 2) * 100, "% of Games with Zero Sales.")
        print("Action Genre Accounts for ", round(r_count / len(zgame_genre), 2) * 100, "% of Games with Zero Sales.")
        print("Miscellaneous Genres Account for", round(m_count / len(zgame_genre), 2) * 100, "% of Games with Zero "
                                                                                              "Sales.")
        resetVar()

