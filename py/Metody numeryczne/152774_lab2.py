def metoda_Babilonska(s):
    x = [s / 2]
    n = 0

    while abs(x[n-1] - x[n]) > 0.01 or n < 1:
        x.append((x[n] + s/x[n])/2)
        n += 1
    return x[-1]

print(metoda_Babilonska(2))


def draw(
    
)
