def sop(f):
    table2 = [[0,0],
              [0,1],
              [1,0],
              [1,1]]

    table3 = [[0,0,0],
              [0,0,1],
              [0,1,0],
              [0,1,1],
              [1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]]

    table4 = [[0,0,0,0],
             [0,0,0,1],
             [0,0,1,0],
             [0,0,1,1],
             [0,1,0,0],
             [0,1,0,1],
             [0,1,1,0],
             [0,1,1,1],
             [1,0,0,0],
             [1,0,0,1],
             [1,0,1,0],
             [1,0,1,1],
             [1,1,0,0],
             [1,1,0,1],
             [1,1,1,0],
             [1,1,1,1]]
    result = ""
    if len(f) == 4:
        for i in range(len(f)):
            if f[i] == 1:
                for x in table2[i]:
                    result += " x" if x == 1 else " !x"
                result += " +"
        return result[1:-2]

    if len(f) == 8:
        for i in range(len(f)):
            if f[i] == 1:
                for x in table3[i]:
                    result += " x" if x == 1 else " !x"
                result += " +"
        return result[1:-2]

    if len(f) == 16:
        for i in range(len(f)):
            if f[i] == 1:
                for x in table4[i]:
                    result += " x" if x == 1 else " !x"
                result += " +"
        return result[1:-2]


def pos(f):
    table2 = [[0,0],
              [0,1],
              [1,0],
              [1,1]]

    table3 = [[0,0,0],
              [0,0,1],
              [0,1,0],
              [0,1,1],
              [1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]]

    table4 = [[0,0,0,0],
             [0,0,0,1],
             [0,0,1,0],
             [0,0,1,1],
             [0,1,0,0],
             [0,1,0,1],
             [0,1,1,0],
             [0,1,1,1],
             [1,0,0,0],
             [1,0,0,1],
             [1,0,1,0],
             [1,0,1,1],
             [1,1,0,0],
             [1,1,0,1],
             [1,1,1,0],
             [1,1,1,1]]
    result = ""
    if len(f) == 4:
        for i in range(len(f)):
            if f[i] == 0:
                result += "("
                for x in table2[i]:
                    result += " x +" if x == 0 else " !x +"
                result = f"{result[:-2]} )"

        return result

    if len(f) == 8:
        for i in range(len(f)):
            if f[i] == 0:
                result += "("
                for x in table3[i]:
                    result += " x +" if x == 0 else " !x +"
                result = f"{result[:-2]} )"
        return result

    if len(f) == 16:
        for i in range(len(f)):
            if f[i] == 0:
                result += "("
                for x in table4[i]:
                    result += " x +" if x == 0 else " !x +"
                result = f"{result[:-2]} )"

        return result





with open('zadania.txt',encoding="utf8") as file:
    ex = []
    for line in file:
        exe = line[line.index("[")+1: line.index("]")]
        for num in exe:
            ex.append(int(num))

        print(f"Zad {line[:-1]}")
        print(f"SOP f = {sop(ex)}")
        print(f"POS f = {pos(ex)}\n")
        ex=[]













