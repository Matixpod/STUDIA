import collections
import datetime
import abc
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Transaction(abc.ABC):
    def __init__(self, amount, title, category, method, description="Brak opisu"):
        self.id = id(self)
        self.__title = title
        self.__description = description
        self.__amount = amount
        self.__category = category
        self.__method = method
        self.__date = datetime.date.today()

    def __str__(self):
        return f"Numer transakcji {self.id} Tytuł {self.__title}\n Opis: {self.__description}\n Kwota {self.__amount} zł\n Data: {self.__date}"

    def __repr__(self):
        return f"Numer transakcji {self.id} Tytuł {self.__title}\n Opis: {self.__description}\n Kwota {self.__amount} zł\n Data: {self.__date}"

    def __add__(self, other):
        return self.__amount + other.__amount

    def __sub__(self, other):
        return self.__amount - other.__amount

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value    

    @property
    def amount(self):
        return self.__amount

class Income(Transaction):
    pass

class Expense(Transaction):
    pass

class TransactionHistory(collections.UserDict):
    pass

class FinanceReport:
    def __init__(self):
        self.transaction_history = TransactionHistory()

    def add_transaction(self, transaction):
        self.transaction_history[transaction.id] = transaction

    def calculate_income(self):
        return sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Income))

    def calculate_expenses(self):
        return sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Expense))

    def get_balance(self):
        income = self.calculate_income()
        expense = self.calculate_expenses()
        return income - expense

    def generate_balance_report(self):
        income = self.calculate_income()
        expense = self.calculate_expenses()
        balance = self.get_balance()
        return f"Raport finansowy\n Aktualny stan konta: {balance} zł\n Zarobki: {income} zł\n Wydatki: {expense} zł"

    def summary(self):
        monthly_income = collections.defaultdict(float)
        monthly_expense = collections.defaultdict(float)

        for transaction in self.transaction_history.values():
            month_year = transaction.date.strftime("%Y-%m")
            if isinstance(transaction, Income):
                monthly_income[month_year] += transaction.amount
            elif isinstance(transaction, Expense):
                monthly_expense[month_year] += transaction.amount

        return monthly_income, monthly_expense

class FinanceApp:
    def __init__(self, root, report):
        self.root = root
        self.report = report
        self.root.geometry('600x400')
        self.root.title("System zarządzania finansami")

        self.setup_ui()

    def setup_ui(self):
        btn_add_transaction = Button(self.root, text="Dodaj transakcję", command=lambda: self.add_transaction())
        btn_add_transaction.pack()
        
        btn_income = Button(self.root, text="Zarobki", command=lambda: self.show_income())
        btn_income.pack()
        
        btn_expense = Button(self.root, text="Wydatki", command=lambda: self.show_expenses())
        btn_expense.pack()
        
        btn_balance = Button(self.root, text="Saldo", command=lambda: self.show_balance())
        btn_balance.pack()
        
        btn_report = Button(self.root, text="Raport", command=lambda: self.show_report())
        btn_report.pack()

        btn_summary_plot = Button(self.root, text="Wykres", command=lambda: self.show_summary_plot())
        btn_summary_plot.pack()

    def show_income(self):
        income = self.report.calculate_income()
        Label(self.root, text=f"Zarobki: {income} zł").pack()

    def show_expenses(self):
        expense = self.report.calculate_expenses()
        Label(self.root, text=f"Wydatki: {expense} zł").pack()

    def show_balance(self):
        balance = self.report.get_balance()
        Label(self.root, text=f"Saldo: {balance} zł").pack()

    def show_report(self):
        report = self.report.generate_balance_report()
        Label(self.root, text=report).pack()

    def show_summary_plot(self):
        monthly_income, monthly_expense = self.report.summary()
        
        months = sorted(set(monthly_income.keys()).union(set(monthly_expense.keys())))
        income_values = [monthly_income[month] for month in months]
        expense_values = [monthly_expense[month] for month in months]

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(months, income_values, color='green', label='Zarobki')
        ax.plot(months, expense_values, color='red', label='Wydatki')
        ax.legend()
        ax.set_title('Zarobki i Wydatki Miesięcznie')
        ax.set_xlabel('Miesiąc')
        ax.set_ylabel('Kwota')
        ax.tick_params(axis='x')
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def add_transaction(self):
        transaction_type = simpledialog.askstring("Rodzaj transakcji", "Podaj rodzaj transakcji (income/expense):")
        amount = simpledialog.askfloat("Kwota", "Podaj kwotę:")
        title = simpledialog.askstring("Tytuł", "Podaj tytuł:")
        category = simpledialog.askstring("Kategoria", "Podaj kategorię:")
        method = simpledialog.askstring("Metoda", "Podaj metodę płatności:")
        description = simpledialog.askstring("Opis", "Podaj opis (opcjonalnie):")

        if transaction_type.lower() == "income":
            transaction = Income(amount, title, category, method, description)
        elif transaction_type.lower() == "expense":
            transaction = Expense(amount, title, category, method, description)
        else:
            Label(self.root, text="Nieprawidłowy rodzaj transakcji!").pack()
            return

        self.report.add_transaction(transaction)
        Label(self.root, text="Transakcja dodana!").pack()

if __name__ == "__main__":
    zarobek_1 = Income(690, "lód", "Seks", "Blik")
    zarobek_2 = Income(610, "lód", "Seks", "Blik")
    zarobek_3 = Income(730, "lód", "Seks", "Blik")
    zarobek_4 = Income(830, "lód", "Seks", "Blik")
    zarobek_5 = Income(920, "lód", "Seks", "Blik")
    zarobek_6 = Income(1200, "lód", "Seks", "Blik")

    wydatek_1 = Expense(591, "lód", "Seks", "Blik")
    wydatek_2 = Expense(123, "lód", "Seks", "Blik")
    wydatek_3 = Expense(532, "lód", "Seks", "Blik")
    wydatek_4 = Expense(100, "lód", "Seks", "Blik")
    wydatek_5 = Expense(234, "lód", "Seks", "Blik")
    wydatek_6 = Expense(123, "lód", "Seks", "Blik")

    zarobek_1.date = zarobek_1.date.replace(month=1)
    zarobek_2.date = zarobek_2.date.replace(month=2)
    zarobek_3.date = zarobek_3.date.replace(month=3)
    zarobek_4.date = zarobek_4.date.replace(month=4)
    zarobek_5.date = zarobek_5.date.replace(month=5)
    zarobek_6.date = zarobek_6.date.replace(month=6)
    wydatek_1.date = wydatek_1.date.replace(month=1)
    wydatek_2.date = wydatek_2.date.replace(month=2)
    wydatek_3.date = wydatek_3.date.replace(month=3)
    wydatek_4.date = wydatek_4.date.replace(month=4)
    wydatek_5.date = wydatek_5.date.replace(month=5)
    wydatek_6.date = wydatek_6.date.replace(month=6)

    konto = FinanceReport()
    konto.add_transaction(zarobek_1)
    konto.add_transaction(zarobek_2)
    konto.add_transaction(zarobek_3)
    konto.add_transaction(zarobek_4)
    konto.add_transaction(zarobek_5)
    konto.add_transaction(zarobek_6)
    konto.add_transaction(wydatek_1)
    konto.add_transaction(wydatek_2)
    konto.add_transaction(wydatek_3)
    konto.add_transaction(wydatek_4)
    konto.add_transaction(wydatek_5)
    konto.add_transaction(wydatek_6)

    root = Tk()
    app = FinanceApp(root, konto)
    root.mainloop()
