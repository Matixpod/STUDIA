from tabulate import tabulate

print(tabulate([["kutas","kutas","kutas","kutas",],["kutas","kutas","kutas","kutas",],["kutas","kutas","kutas","kutas",],["kutas","kutas","kutas","kutas",]],tablefmt='fancy_grid'))



with open('G:/Users/mateu/Pulpit/Github/STUDIA/py/baza_studentow.csv',encoding='utf-8') as file:
    for line in file:
        print(line.strip().split(" "))
        