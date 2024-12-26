import math
filename = 'alkohole.csv'
vodkas = {}

with open(filename, 'r', errors="ignore") as csvfile:
    i = 1
    for line in csvfile:
        if i == 1:
            vodka = line.strip()
            vodkas[vodka] = []
        elif i == 2:
            space = line.index("=")
            vodkas[vodka].append((float(line[:line.index("l")]),float(line[line.index("=")+2:].strip())))
        elif i == 3:
            vodkas[vodka].append((1,float(line.strip())))

            i = 0
        i+=1

    vodkas = dict(sorted(
        ((name, values) for name, values in vodkas.items()),key=lambda x: x[1][0][1]
    ))

    # Najlepsze wódki w danym budżecie
    def best_vodka_in_price_limit():
        max_price = int(input("podaj max cene"))
        people = int(input("Podaj liczbe osób pijących wódke"))
        amount_quality = int(input("1-5 nacisk na ilość / nacisk na jakość alkoholu"))

        amounts = {
            1 : 350,
            2 : 300,
            3 : 250,
            4 : 200,
            5 : 150
        }


        amount = people * amounts[amount_quality]/1000
    
        tierlist = dict(sorted(
            ((name, values) for name, values in vodkas.items() if values[0][1] * math.ceil(amount / values[0][0])<= max_price), 
            key=lambda x: x[1][0][1],reverse=True
        ))

        print(f"Najlepszy wybór wódek dla {people} osób w budżecie: {max_price}zł.")
        print(f"Potrzebna ilość alkoholu: {amount}l")

        nr = 1
        for name, values in tierlist.items():
            l,zl = values[0]
            price = math.ceil(amount / l)*zl
            volume = math.ceil(amount / l)*l
            print(f"{nr}. {name}\n -> {price} zł za {volume} l")
            nr+=1


    # Maksymalna ilość wódki za daną kwote
    def max_vodka_volume_for_price():
        max_price = int(input("podaj max cene"))
        people = int(input("Podaj liczbe osób pijących wódke"))


        tierlist = dict(sorted(
            ((name, values) for name, values in vodkas.items() if values[0][1] <= max_price), 
            key=lambda x: math.floor(max_price / x[1][0][1])*x[1][0][0],reverse=True
        ))

        print(f"Maksymalna ilość wódki do kupienia za {max_price}zł.")
        nr = 1
        for name, values in tierlist.items():
            max_bottles = math.floor(max_price/values[0][1])
            max_volume = max_bottles*values[0][0]
            price = max_bottles * values[0][1]
            print(f"{nr}. {name}\n -> Za {price}zł możesz kupić {max_bottles} butelki.\n -> Całkowita ilość wódki: {max_volume}l.\n -> ilość wódki na 1 osobe: {round(max_volume/people,2)}l.")
            nr+=1

best_vodka_in_price_limit()
max_vodka_volume_for_price()