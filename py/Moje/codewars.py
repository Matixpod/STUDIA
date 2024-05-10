# %% Zad 1
def bomb_has_been_planted(m, time):
    k = []
    for i in range(len(m)):
        if "CT" in m[i]:
            ct = [m[i].index("CT"),i]

        if "B" in m[i]:
            b = [m[i].index("B"),i]

        if "K" in m[i]:
            k = [m[i].index("K"),i]

    steps_needed = max([abs(ct[0]-b[0]),abs(ct[1]-b[1])])
    if k:
        steps_needed2 = max([abs(ct[0]-k[0]),abs(ct[1]-k[1])]) + max([abs(b[0]-k[0]),abs(b[1]-k[1])])
        # print(ct,b,k)
        print(steps_needed2,"ilosc krokow z kitem")
    print(steps_needed, "ilosc krokow bez kitu")
    return bool(k and time - steps_needed2 >= 5 or time - steps_needed >= 10)
        

# %% Zad 2






map1 = [
        ["CT", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "B"]
    ]

map5 = [
    ["0", "0", "0", "0", "0", "0"],
    ["CT", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "B"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "K", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"]
]
        

print(bomb_has_been_planted(map1,13))
print(bomb_has_been_planted(map5, 13))





