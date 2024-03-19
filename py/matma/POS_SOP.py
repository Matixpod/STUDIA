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
                for i,x in enumerate(table2[i]):
                    result += f" x{i+1}" if x == 1 else f" x̄{i+1}"
                    result += " ·"
                result = result[:-1] + " + "
        return replace_numbers_with_subscripts(result[1:-2])
        

    if len(f) == 8:
        for i in range(len(f)):
            if f[i] == 1:
                for i,x in enumerate(table3[i]):
                    result += f" x{i+1}" if x == 1 else f" x̄{i+1}"
                    result += " ·"
                result = result[:-1] + " + "
        return replace_numbers_with_subscripts(result[1:-2])


    if len(f) == 16:
        for i in range(len(f)):
            if f[i] == 1:
                for i,x in enumerate(table4[i]):
                    result += f" x{i+1}" if x == 1 else f" x̄{i+1}"
                    result += " ·"
                result = result[:-1] + " + "
        return replace_numbers_with_subscripts(result[1:-2])
        
    





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
                for i,x in enumerate(table2[i]):
                    result += f" x{i+1} +" if x == 0 else f" x̄{i+1} +"
                result = f"{result[:-2]} )"
        return replace_numbers_with_subscripts(result)


    if len(f) == 8:
        for i in range(len(f)):
            if f[i] == 0:
                result += "("
                for i,x in enumerate(table3[i]):
                    result += f" x{i+1} +" if x == 0 else f" x̄{i+1} +"
                result = f"{result[:-2]} )"
        return replace_numbers_with_subscripts(result)


    if len(f) == 16:
        for i in range(len(f)):
            if f[i] == 0:
                result += "("
                for i,x in enumerate(table4[i]):
                    result += f" x{i+1} +" if x == 0 else f" x̄{i+1} +"
                result = f"{result[:-2]} )"

        return replace_numbers_with_subscripts(result)
    


subscript_map = {
    '1': '₁',
    '2': '₂',
    '3': '₃',
    '4': '₄'
    }



def replace_numbers_with_subscripts(text):
    for arabic, subscript in subscript_map.items():
        text = text.replace(arabic, subscript)
    return text







# with open('zadania.txt',encoding="utf8") as file:
#     arr = []
#     for line in file:
#         exe = line[line.index("[")+1: line.index("]")]
#         for num in exe:
#             arr.append(int(num))

#         print(f"Zad {line[:-1]}")
#         print(f"SOP f = {sop(arr)}")
#         print(f"POS f = {pos(arr)}\n")
#         arr=[]



print(f"SOP f = {sop([1,1,0,1])}")
print(f"POS f = {pos([1,1,0,1])}")









