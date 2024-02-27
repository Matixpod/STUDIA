from tabulate import tabulate


class Database(object):

    def read_database(self):
        print(f"Aktualny plik: {self.path}")
        print(tabulate(self.data_table,headers='firstrow',tablefmt='fancy_grid'))
        self.menu()

    def menu(self):
        print(tabulate([[f"Jaką operację chcesz wykonać?\n 1. Aby dodać rekord do bazy danych. \n 2. Aby usunąć rekord z bazy danych. \n 3. Aby wyświetlić bazę danych. \n 4. Aby zapisać wprowadzone zmiany. \n 5. Aby wczytać plik. \n 6. Aby zakończyć program."]],tablefmt='fancy_grid'))
        operation = input("Wybierz pozycje z menu: ")

        if operation == "1":
            self.add_student()
        elif operation == "2":
            self.delete_student()
        elif operation == "3":
            self.read_database()
        elif operation == "4":
            self.save_changes()
        elif operation == "5":
            self.load_data()
        elif operation == "6":
            print("Koniec działania programu.")
        else:
            print('\n\nZła operacja!\n\n')
            self.menu()

    def add_student(self):
        name = input('Podaj imię studenta: ')
        surname = input('Podaj nazwisko studenta: ')
        number = input('Podaj numer albumu studenta: ')
        self.data_table.append([name,surname,number])
        print("\n\nOperacja wykonana pomyślnie.\n\n")
        self.menu()

        
    def delete_student(self):
        index = input('Wpisz numer albumu ucznia którego chcesz usunąć.')
        for i,student in enumerate(self.data_table):
            if index in student:
                del self.data_table[i]
        print("\n\nOperacja wykonana pomyślnie.\n\n")
        self.menu()
    

    def save_changes(self):
        with open(self.path,'w',encoding='utf-8') as file:
            for student in self.data_table[1:]:
                file.write(' '.join(student))
                file.write('\n')
        print("\n\nOperacja wykonana pomyślnie.\n\n")
        self.menu()

    def load_data(self):
        self.path = input('Podaj ścieżkę do pliku: ')
        try:
            with open(self.path, encoding='utf-8') as file:
                self.data_table = [['Imię','Nazwisko','Numer albumu']]
                self.data_table.extend(line.strip().split(" ") for line in file)
                print(tabulate(self.data_table,headers='firstrow',tablefmt='fancy_grid'))
                self.menu()
        except FileNotFoundError:
            print("\nNie znaleziono pliku, podaj poprawną ścieżkę\n")

    

Database().load_data()
