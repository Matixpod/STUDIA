# importing csv module
import csv
from tabulate import tabulate
import math
from collections import Counter


# csv file name
filename = "movies.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r', errors="ignore") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
    x = 0
    średnia_arytmetyczna_rating = 0
    średnia_arytmetyczna_metascore = 0
    średnia_arytmetyczna_runtime = 0

    wariancja_rating = 0
    wariancja_metascore = 0
    wariancja_runtime = 0

    rating = []
    metascore = []
    runtime = []
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        rating.append(float(row[3]))
        runtime.append(float(row[8]))
        średnia_arytmetyczna_rating += float(row[3])
        wariancja_rating += float(row[3])**2
        if row[4] != "NA":
            metascore.append(float(row[4]))
            średnia_arytmetyczna_metascore += float(row[4])
            wariancja_metascore += float(row[4])**2
            x += 1
        średnia_arytmetyczna_runtime += float(row[8])
        wariancja_runtime += float(row[8])**2

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))


n = 9999

średnia_arytmetyczna_rating = średnia_arytmetyczna_rating/n
średnia_arytmetyczna_metascore = średnia_arytmetyczna_metascore/x
średnia_arytmetyczna_runtime = średnia_arytmetyczna_runtime/n

wariancja_rating = wariancja_rating/n - średnia_arytmetyczna_rating**2
wariancja_metascore = wariancja_metascore/x - średnia_arytmetyczna_metascore**2
wariancja_runtime = wariancja_runtime/n - średnia_arytmetyczna_runtime**2

odchylenie_standardowe_rating = math.sqrt(wariancja_rating)
odchylenie_standardowe_metascore = math.sqrt(wariancja_metascore)
odchylenie_standardowe_runtime = math.sqrt(wariancja_runtime)

dominanta_rating = Counter(rating).most_common(1)
dominanta_metascore = Counter(metascore).most_common(1)
dominanta_runtime = Counter(runtime).most_common(1)

rating = sorted(rating)
metascore = sorted(metascore)
runtime = sorted(runtime)
m = int(len(metascore) / 2)
print(m)

mediana_rating = rating[5000]
mediana_metascore = metascore[m+1]
mediana_runtime = runtime[5000]

kwartyl_1_dolny = (n + 1)/4
kwartyl_1_dolny_metascore = (m+1)/4

kwartyl_3_gorny = (3*n+3)/4
kwartyl_3_gorny_metascore = (3*m+3)/4

odchylenie_cwiartkowe =  (kwartyl_3_gorny- kwartyl_1_dolny)/2
odchylenie_cwiartkowe_metascore = (kwartyl_3_gorny_metascore - kwartyl_1_dolny_metascore)/2

print(odchylenie_standardowe_rating,odchylenie_standardowe_metascore,odchylenie_standardowe_runtime)
print(dominanta_rating,dominanta_metascore,dominanta_runtime)
print(mediana_rating,mediana_metascore,mediana_runtime)
print(kwartyl_1_dolny,kwartyl_1_dolny_metascore,kwartyl_1_dolny)
print(kwartyl_3_gorny,kwartyl_3_gorny_metascore,kwartyl_3_gorny)
print(odchylenie_cwiartkowe, odchylenie_cwiartkowe_metascore,odchylenie_cwiartkowe)








# printing the field names

# print(tabulate(rows,tablefmt='fancy_grid'))
