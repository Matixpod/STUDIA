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
    n = 0
    suma_rating = 0
    suma_votes = 0
    suma_runtime = 0

    suma2_rating = 0
    suma2_votes = 0
    suma2_runtime = 0

    suma_rating_votes = 0
    suma_rating_runtime = 0
    suma_votes_runtime = 0


    rating = []
    votes = []
    runtime = []
    for row in csvreader:
        del row[-1]
        rows.append(row)
        rating.append(float(row[3]))
        votes.append(float(row[6]))
        runtime.append(float(row[8]))
        suma_rating += float(row[3])
        suma2_rating += float(row[3])**2
        suma_votes += float(row[6])
        suma2_votes += float(row[6])**2
        suma_runtime += float(row[8])
        suma2_runtime += float(row[8])**2

        suma_rating_votes += float(row[3]) * float(row[6])
        suma_rating_runtime += float(row[3]) * float(row[8])
        suma_votes_runtime += float(row[6]) * float(row[8])



n = len(rows)-1

def X(suma,n):
    return suma/n

def S2(x2,n,śr_a):
    return x2/n - śr_a**2

def S(S2):
    return math.sqrt(S2)

def M(arr):
    n = len(arr)
    return arr[n // 2] if n % 2 == 1 else (arr[n // 2 - 1] + arr[n // 2]) / 2

def Q1_4(arr,n):
    return arr[int((n + 1)/4)]

def Q3_4(arr,n):
    return arr[int((3*n+3)/4)]

def Q(kwart_3_g,kwart_1_d):
    return (kwart_3_g - kwart_1_d)/2

def Vs(Q,x):
    return Q/x

def Vq(Q,M):
    return Q/M

def A1(arr,x,S):
    u3 = sum((i-x)**3 for i in arr)
    return u3/(S**3)

def A2(Q1_4,Q3_4,M,Q):
    return (Q1_4+Q3_4-2*M)/2*Q

def A3(x,D,S):
    return (x-D)/S

def rxy(xy,x_,y_,Sx,Sy,n):
    xy_ = X(xy,n)
    return (xy_ - x_ * y_) / (Sx * Sy)



średnia_arytmetyczna_rating = X(suma_rating,n)
średnia_arytmetyczna_votes = X(suma_votes,n)
średnia_arytmetyczna_runtime = X(suma_runtime,n)

wariancja_rating = S2(suma2_rating,n,średnia_arytmetyczna_rating)
wariancja_votes = S2(suma2_votes,n,średnia_arytmetyczna_votes)
wariancja_runtime = S2(suma2_runtime,n,średnia_arytmetyczna_runtime)

odchylenie_standardowe_rating = S(wariancja_rating)
odchylenie_standardowe_votes = S(wariancja_votes)
odchylenie_standardowe_runtime = S(wariancja_runtime)

dominanta_rating = Counter(rating).most_common(1)[0][0]
dominanta_votes = Counter(votes).most_common(1)[0][0]
dominanta_runtime = Counter(runtime).most_common(1)[0][0]

rating = sorted(rating)
votes = sorted(votes)
runtime = sorted(runtime)

mediana_rating = M(rating)
mediana_votes = M(votes)
mediana_runtime = M(runtime)

kwartyl_1_dolny_rating = Q1_4(rating,n)
kwartyl_1_dolny_votes = Q1_4(votes,n)
kwartyl_1_dolny_runtime = Q1_4(runtime,n)

kwartyl_3_gorny_rating = Q3_4(rating,n)
kwartyl_3_gorny_votes = Q3_4(votes,n)
kwartyl_3_gorny_runtime = Q3_4(runtime,n)

odchylenie_cwiartkowe_rating =  Q(kwartyl_3_gorny_rating,kwartyl_1_dolny_rating)
odchylenie_cwiartkowe_votes = Q(kwartyl_3_gorny_votes,kwartyl_1_dolny_votes)
odchylenie_cwiartkowe_runtime =  Q(kwartyl_3_gorny_runtime,kwartyl_1_dolny_runtime)

wspolczynnik_zmiennosci_klasyczny_rating = Vs(odchylenie_cwiartkowe_rating, średnia_arytmetyczna_rating)
wspolczynnik_zmiennosci_klasyczny_votes = Vs(odchylenie_cwiartkowe_votes, średnia_arytmetyczna_votes)
wspolczynnik_zmiennosci_klasyczny_runtime = Vs(odchylenie_cwiartkowe_runtime, średnia_arytmetyczna_runtime)

wspolczynnik_zmiennosci_pozycyjny_rating = Vq(odchylenie_cwiartkowe_rating, mediana_rating)
wspolczynnik_zmiennosci_pozycyjny_votes = Vq(odchylenie_cwiartkowe_votes, mediana_votes)
wspolczynnik_zmiennosci_pozycyjny_runtime = Vq(odchylenie_cwiartkowe_runtime, mediana_runtime)

asymetria_klasyczna_rating = A1(rating, średnia_arytmetyczna_rating, odchylenie_cwiartkowe_rating)
asymetria_klasyczna_votes= A1(votes, średnia_arytmetyczna_votes, odchylenie_cwiartkowe_votes)
asymetria_klasyczna_runtime= A1(runtime, średnia_arytmetyczna_runtime, odchylenie_cwiartkowe_runtime)

asymetria_pozycyjna_rating = A2(kwartyl_1_dolny_rating,kwartyl_3_gorny_rating, mediana_rating, odchylenie_cwiartkowe_rating)
asymetria_pozycyjna_votes = A2(kwartyl_1_dolny_votes,kwartyl_3_gorny_votes, mediana_votes, odchylenie_cwiartkowe_votes)
asymetria_pozycyjna_runtime = A2(kwartyl_1_dolny_runtime,kwartyl_3_gorny_runtime, mediana_runtime, odchylenie_cwiartkowe_runtime)

asymetria_klasyczno_pozycyjna_rating = A3(średnia_arytmetyczna_rating,dominanta_rating,odchylenie_cwiartkowe_rating)
asymetria_klasyczno_pozycyjna_votes = A3(średnia_arytmetyczna_votes,dominanta_votes,odchylenie_cwiartkowe_votes)
asymetria_klasyczno_pozycyjna_runtime = A3(średnia_arytmetyczna_runtime,dominanta_runtime,odchylenie_cwiartkowe_runtime)

koleracja_pearsona_rating_votes = rxy(suma_rating_votes,średnia_arytmetyczna_rating,średnia_arytmetyczna_votes,odchylenie_cwiartkowe_rating, odchylenie_cwiartkowe_votes, n)

koleracja_pearsona_rating_runtime = rxy(suma_rating_runtime,średnia_arytmetyczna_rating,średnia_arytmetyczna_runtime,odchylenie_cwiartkowe_rating, odchylenie_cwiartkowe_runtime, n)
koleracja_pearsona_votes_runtime = rxy(suma_votes_runtime,średnia_arytmetyczna_votes,średnia_arytmetyczna_runtime,odchylenie_cwiartkowe_votes, odchylenie_cwiartkowe_runtime, n)
print(koleracja_pearsona_rating_votes)
print(koleracja_pearsona_rating_runtime)
print(koleracja_pearsona_votes_runtime)

rows.append(["-->", "Średnia arytmetyczna","",średnia_arytmetyczna_rating,"","",średnia_arytmetyczna_votes,"",średnia_arytmetyczna_runtime])
rows.append(["-->", "Odchylenie standardowe","",odchylenie_standardowe_rating,"","",odchylenie_standardowe_votes,"",odchylenie_standardowe_runtime])
rows.append(["-->", "Dominanta","",dominanta_rating,"","",dominanta_votes,"",dominanta_runtime])
rows.append(["-->", "Mediana","",mediana_rating,"","",mediana_votes,"",mediana_runtime])
rows.append(["-->", "Kwartyl 1 dolny","",kwartyl_1_dolny_rating,"","",kwartyl_1_dolny_votes,"",kwartyl_1_dolny_runtime])
rows.append(["-->", "Kwartyl 3 gorny","",kwartyl_3_gorny_rating,"","",kwartyl_3_gorny_votes,"",kwartyl_3_gorny_runtime])
rows.append(["-->", "Odchylenie ćwiartkowe","",odchylenie_cwiartkowe_rating,"","",odchylenie_cwiartkowe_votes,"",odchylenie_cwiartkowe_runtime])
rows.append(["-->", "Współczynnik zmiennosci klasyczny","",wspolczynnik_zmiennosci_klasyczny_rating,"","",wspolczynnik_zmiennosci_klasyczny_votes,"",wspolczynnik_zmiennosci_klasyczny_runtime])
rows.append(["-->", "Współczynnik zmiennosci pozycyjny","",wspolczynnik_zmiennosci_pozycyjny_rating,"","",wspolczynnik_zmiennosci_pozycyjny_votes,"",wspolczynnik_zmiennosci_pozycyjny_runtime])
rows.append(["-->", "Asymetria klasyczna","",asymetria_klasyczna_rating,"","",asymetria_klasyczna_votes,"",asymetria_klasyczna_runtime])
rows.append(["-->", "Asymetria pozycyjna","",asymetria_pozycyjna_rating,"","",asymetria_pozycyjna_votes,"",asymetria_pozycyjna_runtime])
rows.append(["-->", "Asymetria klasyczno-pozycyjna","",asymetria_klasyczno_pozycyjna_rating,"","",asymetria_klasyczno_pozycyjna_votes,"",asymetria_klasyczno_pozycyjna_runtime])


result = []

print(tabulate(rows,tablefmt='fancy_grid'))


# print(średnia_arytmetyczna_rating, średnia_arytmetyczna_votes, średnia_arytmetyczna_runtime)
# print(odchylenie_standardowe_rating,odchylenie_standardowe_votes,odchylenie_standardowe_runtime)
# print(dominanta_rating,dominanta_votes,dominanta_runtime)
# print(mediana_rating,mediana_votes,mediana_runtime)
# print(kwartyl_1_dolny_rating,kwartyl_1_dolny_votes,kwartyl_1_dolny_runtime)
# print(kwartyl_3_gorny_rating,kwartyl_3_gorny_votes,kwartyl_3_gorny_runtime)
# print(odchylenie_cwiartkowe_rating, odchylenie_cwiartkowe_votes,odchylenie_cwiartkowe_runtime)
