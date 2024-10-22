# importing csv module
import csv
from tabulate import tabulate
import math
from collections import Counter


filename = "movies.csv"

fields = []
rows = []

# reading csv file
with open(filename, 'r', errors="ignore") as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    del fields[-1]
    rows.append(fields)
    m = 0
    średnia_arytmetyczna_rating = 0
    średnia_arytmetyczna_metascore = 0
    średnia_arytmetyczna_runtime = 0

    wariancja_rating = 0
    wariancja_metascore = 0
    wariancja_runtime = 0

    rating = []
    metascore = []
    runtime = []
    for row in csvreader:
        del row[-1]
        rows.append(row)
        rating.append(float(row[3]))
        runtime.append(float(row[8]))
        średnia_arytmetyczna_rating += float(row[3])
        wariancja_rating += float(row[3])**2
        if row[4] != "NA":
            metascore.append(float(row[4]))
            średnia_arytmetyczna_metascore += float(row[4])
            wariancja_metascore += float(row[4])**2
            m += 1
        średnia_arytmetyczna_runtime += float(row[8])
        wariancja_runtime += float(row[8])**2



n = 9999

średnia_arytmetyczna_rating = średnia_arytmetyczna_rating/n
średnia_arytmetyczna_metascore = średnia_arytmetyczna_metascore/m
średnia_arytmetyczna_runtime = średnia_arytmetyczna_runtime/n

wariancja_rating = wariancja_rating/n - średnia_arytmetyczna_rating**2
wariancja_metascore = wariancja_metascore/m - średnia_arytmetyczna_metascore**2
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
x = int(len(metascore) / 2)

mediana_rating = rating[5000]
mediana_metascore = metascore[x+1]
mediana_runtime = runtime[5000]

kwartyl_1_dolny_rating = rating[int((n + 1)/4)]
kwartyl_1_dolny_metascore = metascore[int((m+1)/4)]
kwartyl_1_dolny_runtime = runtime[int((n + 1)/4)]

kwartyl_3_gorny_rating = rating[int((3*n+3)/4)]
kwartyl_3_gorny_metascore = metascore[int((3*m+3)/4)]
kwartyl_3_gorny_runtime = runtime[int((3*n+3)/4)]

odchylenie_cwiartkowe_rating =  (kwartyl_3_gorny_rating- kwartyl_1_dolny_rating)/2
odchylenie_cwiartkowe_metascore = (kwartyl_3_gorny_metascore - kwartyl_1_dolny_metascore)/2
odchylenie_cwiartkowe_runtime =  (kwartyl_3_gorny_runtime- kwartyl_1_dolny_runtime)/2



# print(średnia_arytmetyczna_rating, średnia_arytmetyczna_metascore, średnia_arytmetyczna_runtime)
# print(odchylenie_standardowe_rating,odchylenie_standardowe_metascore,odchylenie_standardowe_runtime)
# print(dominanta_rating,dominanta_metascore,dominanta_runtime)
# print(mediana_rating,mediana_metascore,mediana_runtime)
# print(kwartyl_1_dolny_rating,kwartyl_1_dolny_metascore,kwartyl_1_dolny_runtime)
# print(kwartyl_3_gorny_rating,kwartyl_3_gorny_metascore,kwartyl_3_gorny_runtime)
# print(odchylenie_cwiartkowe_rating, odchylenie_cwiartkowe_metascore,odchylenie_cwiartkowe_runtime)


rows.append(["-->", "Średnia arytmetyczna","",średnia_arytmetyczna_rating,średnia_arytmetyczna_metascore,"","","",średnia_arytmetyczna_runtime])
rows.append(["-->", "Odchylenie standardowe","",odchylenie_standardowe_rating,odchylenie_standardowe_metascore,"","","",odchylenie_standardowe_runtime])
rows.append(["-->", "Dominanta","",dominanta_rating,dominanta_metascore,"","","",dominanta_runtime])
rows.append(["-->", "Mediana","",mediana_rating,mediana_metascore,"","","",mediana_runtime])
rows.append(["-->", "Kwartyl 1 dolny","",kwartyl_1_dolny_rating,kwartyl_1_dolny_metascore,"","","",kwartyl_1_dolny_runtime])
rows.append(["-->", "Kwartyl 3 gorny","",kwartyl_3_gorny_rating,kwartyl_3_gorny_metascore,"","","",kwartyl_3_gorny_runtime])
rows.append(["-->", "Odchylenie ćwiartkowe","",odchylenie_cwiartkowe_rating,odchylenie_cwiartkowe_metascore,"","","",odchylenie_cwiartkowe_runtime])





print(tabulate(rows,tablefmt='fancy_grid'))
