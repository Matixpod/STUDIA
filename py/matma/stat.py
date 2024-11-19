import csv
from tabulate import tabulate
import math
from collections import Counter

filename = "movies.csv"

fields = []
rows = []
result = [["", "Rating", "Votes", "Runtime"]]

# Wczytanie pliku CSV
with open(filename, 'r', errors="ignore") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    del fields[-1]
    rows.append(fields)
    n = 0
    rating = []
    votes = []
    runtime = []
    for row in csvreader:
        del row[-1]
        rows.append(row)
        rating.append(float(row[3]))
        votes.append(float(row[6]))
        runtime.append(float(row[8]))

rating = sorted(rating)
votes = sorted(votes)
runtime = sorted(runtime)

rating_25, rating_50, rating_75, rating_100 = rating[0:2500], rating[2500:5000], rating[5000:7500], rating[7500:10000]
votes_25, votes_50, votes_75, votes_100 = votes[0:2500], votes[2500:5000], votes[5000:7500], votes[7500:10000]
runtime_25, runtime_50, runtime_75, runtime_100 = runtime[0:2500], runtime[2500:5000], runtime[5000:7500], runtime[7500:10000]

n = len(rows)-1
n_2 = len(rating_25)

# Funkcje statystyczne
def Suma2(arr):
    arr2 = []
    for i in arr:
        arr2.append(i**2)
    return sum(arr2)

def X(arr,n):
    suma = sum(arr)
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

def rxy(arr1,arr2,x_,y_,Sx,Sy,n):
    xy = []
    for i in range(n):
        xy.append(arr1[i]*arr2[i])
    xy_ = X(xy,n)
    return (xy_ - x_ * y_) / (Sx * Sy)

# Obliczenia
def calculation(rating,votes,runtime,n,szereg=""):
    średnia_arytmetyczna_rating = X(rating,n)
    średnia_arytmetyczna_votes = X(votes,n)
    średnia_arytmetyczna_runtime = X(runtime,n)

    wariancja_rating = S2(Suma2(rating),n,średnia_arytmetyczna_rating)
    wariancja_votes = S2(Suma2(votes),n,średnia_arytmetyczna_votes)
    wariancja_runtime = S2(Suma2(runtime),n,średnia_arytmetyczna_runtime)

    odchylenie_standardowe_rating = S(wariancja_rating)
    odchylenie_standardowe_votes = S(wariancja_votes)
    odchylenie_standardowe_runtime = S(wariancja_runtime)

    dominanta_rating = Counter(rating).most_common(1)[0][0]
    dominanta_votes = Counter(votes).most_common(1)[0][0]
    dominanta_runtime = Counter(runtime).most_common(1)[0][0]

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

    koleracja_pearsona_rating_votes = rxy(rating,votes,średnia_arytmetyczna_rating,średnia_arytmetyczna_votes,odchylenie_standardowe_rating, odchylenie_standardowe_votes, n)
    koleracja_pearsona_rating_runtime = rxy(rating,runtime,średnia_arytmetyczna_rating,średnia_arytmetyczna_runtime,odchylenie_standardowe_rating, odchylenie_standardowe_runtime, n)
    koleracja_pearsona_votes_runtime = rxy(votes,runtime,średnia_arytmetyczna_votes,średnia_arytmetyczna_runtime,odchylenie_standardowe_votes, odchylenie_standardowe_runtime, n)

    result.append(["Średnia arytmetyczna", średnia_arytmetyczna_rating, średnia_arytmetyczna_votes, średnia_arytmetyczna_runtime])
    result.append(["Odchylenie standardowe", odchylenie_standardowe_rating, odchylenie_standardowe_votes, odchylenie_standardowe_runtime])
    result.append(["Dominanta", dominanta_rating, dominanta_votes, dominanta_runtime])
    result.append(["Mediana", mediana_rating, mediana_votes, mediana_runtime])
    result.append(["Kwartyl 1 dolny", kwartyl_1_dolny_rating, kwartyl_1_dolny_votes, kwartyl_1_dolny_runtime])
    result.append(["Kwartyl 3 górny", kwartyl_3_gorny_rating, kwartyl_3_gorny_votes, kwartyl_3_gorny_runtime])
    result.append(["Odchylenie ćwiartkowe", odchylenie_cwiartkowe_rating, odchylenie_cwiartkowe_votes, odchylenie_cwiartkowe_runtime])
    result.append(["Współczynnik zmienności klasyczny", wspolczynnik_zmiennosci_klasyczny_rating, wspolczynnik_zmiennosci_klasyczny_votes, wspolczynnik_zmiennosci_klasyczny_runtime])
    result.append(["Współczynnik zmienności pozycyjny", wspolczynnik_zmiennosci_pozycyjny_rating, wspolczynnik_zmiennosci_pozycyjny_votes, wspolczynnik_zmiennosci_pozycyjny_runtime])
    result.append(["Asymetria klasyczna", asymetria_klasyczna_rating, asymetria_klasyczna_votes, asymetria_klasyczna_runtime])
    result.append(["Asymetria pozycyjna", asymetria_pozycyjna_rating, asymetria_pozycyjna_votes, asymetria_pozycyjna_runtime])
    result.append(["Asymetria klasyczno-pozycyjna", asymetria_klasyczno_pozycyjna_rating, asymetria_klasyczno_pozycyjna_votes, asymetria_klasyczno_pozycyjna_runtime])
    result.append(["Korelacja Pearsona", koleracja_pearsona_rating_votes, koleracja_pearsona_rating_runtime, koleracja_pearsona_votes_runtime])
    result.append([""])
    result.append([szereg])

calculation(rating, votes, runtime, n, "SZEREG ROZDZIELCZY 0-2500")
calculation(rating_25, votes_25, runtime_25, n_2, "SZEREG ROZDZIELCZY 2500-5000")
calculation(rating_50, votes_50, runtime_50, n_2, "SZEREG ROZDZIELCZY 5000-7500")
calculation(rating_75, votes_75, runtime_75, n_2, "SZEREG ROZDZIELCZY 7500-10000")
calculation(rating_100, votes_100, runtime_100, n_2)

# Zapisanie do pliku RTF
def save_to_rtf(result):
    rtf_header = "{\\rtf1\\ansi\\ansicpg1250\\deff0\\nouicompat\\deflang1045{\\fonttbl{\\f0\\fnil\\fcharset0 Arial;}}"
    rtf_footer = "}"

    # Tworzenie tabeli RTF
    rtf_table = "{\\trowd\\trgaph108\\trleft-108"
    for row in result:
        rtf_table += "\\cellx" + str(4000)
        for cell in row:
            rtf_table += "\\intbl " + str(cell) + " "
    rtf_table += "\\row}"

    rtf_file = rtf_header + rtf_table + rtf_footer

    with open("output.rtf", "w", encoding="utf-8") as file:
        file.write(rtf_file)

save_to_rtf(result)
