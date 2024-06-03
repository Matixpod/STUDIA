import collections
import datetime
import abc
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

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
    month = datetime.date.today().strftime("%Y-%m")

    def __init__(self):
        self.transaction_history = TransactionHistory()
        self.view_mode = "monthly"

    def add_transaction(self, transaction):
        self.transaction_history[transaction.id] = transaction

    def calculate_income(self):
        if self.view_mode == "all_time":
            return sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Income))
        monthly_income, monthly_expense = self.summary()
        return monthly_income[self.month]

    def calculate_expenses(self):
        if self.view_mode == "all_time":
            return sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Expense))
        monthly_income, monthly_expense = self.summary()
        return monthly_expense[self.month]

    def get_balance(self):
        income = self.calculate_income()
        expense = self.calculate_expenses()
        return income - expense

    def generate_balance_report(self):
        income = self.calculate_income()
        expense = self.calculate_expenses()
        balance = self.get_balance()
        return f"Raport finansowy\n Stan konta: {balance} zł\n Zarobki: {income} zł\n Wydatki: {expense} zł"

    def generate_transaction_history_report(self):
        report = "Historia transakcji:\n"
        for transaction in self.transaction_history.values():
            if self.view_mode == "monthly" and transaction.date.strftime("%Y-%m") == self.month:
                report += str(transaction) + "\n"
            elif self.view_mode == "all_time":
                report += str(transaction) + "\n"
                
        return report

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
    
    def change_view(self):
        self.view_mode = "all_time" if self.view_mode == "monthly" else "monthly"

class FinanceApp:
    def __init__(self, root, report):
        self.root = root
        self.report = report
        self.root.geometry('800x600')
        self.root.title("System zarządzania finansami")

        self.setup_ui()
        self.update_display()

    def setup_ui(self):
        btn_add_transaction = Button(self.root, text="Dodaj transakcję", command=lambda: self.add_transaction(), width=25)
        btn_add_transaction.grid(row=0, column=5)

        btn_report = Button(self.root, text="Raport", command=lambda: self.show_report(), width=25)
        btn_report.grid(row=1, column=5)

        btn_history = Button(self.root, text="Historia transakcji", command=lambda: self.show_transaction_history(), width=25)
        btn_history.grid(row=3, column=5)

        btn_change_view = Button(self.root, text="Przełącz widok", command=lambda: self.change_view(), width=25)
        btn_change_view.grid(row=4, column=5)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=10, column=0, columnspan=3)

        self.income_label = Label(self.root, text="", font=("Helvetica", 18))
        self.income_label.grid(row=1, column=0)

        self.expense_label = Label(self.root, text="", font=("Helvetica", 18))
        self.expense_label.grid(row=1, column=1)

        self.balance_label = Label(self.root, text="", font=("Helvetica", 18))
        self.balance_label.grid(row=1, column=2)

    def update_display(self):
        income = self.report.calculate_income()
        expense = self.report.calculate_expenses()
        balance = self.report.get_balance()

        self.income_label.config(text=f"Zarobki: {income} zł")
        self.expense_label.config(text=f"Wydatki: {expense} zł")
        self.balance_label.config(text=f"Saldo: {balance} zł")

        self.show_summary_plot()

    def show_report(self):
        report = self.report.generate_balance_report()
        history = self.report.generate_transaction_history_report()
        full_report = report + "\n\n" + history

        report_window = Toplevel(self.root)
        report_window.title("Raport")
        
        report_label = Label(report_window, text=report, justify=LEFT)
        report_label.pack(anchor=W)
        
        history_label = Text(report_window)
        history_label.insert(END, history)
        history_label.pack()

        save_button = Button(report_window, text="Zapisz do pliku", command=lambda: self.save_report_to_file(full_report))
        save_button.pack()

    def save_report_to_file(self, full_report):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(full_report)
            messagebox.showinfo("Informacja", "Raport zapisany pomyślnie!")

    def show_summary_plot(self):
        if self.report.view_mode == 'all_time':
            monthly_income, monthly_expense = self.report.summary()

            months = sorted(set(monthly_income.keys()).union(set(monthly_expense.keys())))
            income_values = [monthly_income[month] for month in months]
            expense_values = [monthly_expense[month] for month in months]

            self.ax.clear()
            self.ax.plot(months, income_values, color='green', label='Zarobki')
            self.ax.plot(months, expense_values, color='red', label='Wydatki')
            self.ax.legend()
            self.ax.set_title('Zarobki i Wydatki przez cały czas')
            self.ax.set_xlabel('Miesiąc')
            self.ax.set_ylabel('Kwota')
            self.ax.tick_params(axis='x')
            
            self.canvas.draw()
        else:
            last_month_transactions = [transaction for transaction in self.report.transaction_history.values() if transaction.date.strftime("%Y-%m") == self.report.month]
            income = sum(transaction.amount for transaction in last_month_transactions if isinstance(transaction, Income))
            expense = sum(transaction.amount for transaction in last_month_transactions if isinstance(transaction, Expense))

            labels = ['Zarobki', 'Wydatki']
            values = [income, expense]
            colors = ['green', 'red']

            self.ax.clear()
            self.ax.bar(labels, values, color=colors)
            self.ax.set_title('Zarobki i Wydatki w tym miesiącu')
            self.ax.set_ylabel('Kwota w zł')
            
            self.canvas.draw()

    def add_transaction(self):
        transaction_type = simpledialog.askstring("Rodzaj transakcji", "Podaj rodzaj transakcji (income/expense):")
        amount = simpledialog.askfloat("Kwota", "Podaj kwotę:")
        title = simpledialog.askstring("Tytuł", "Podaj tytuł:")
        category = simpledialog.askstring("Kategoria", "Podaj kategorię:")
        method = simpledialog.askstring("Metoda", "Podaj metodę:")
        description = simpledialog.askstring("Opis", "Podaj opis (opcjonalnie):")

        if transaction_type == "income":
            transaction = Income(amount, title, category, method, description)
        elif transaction_type == "expense":
            transaction = Expense(amount, title, category, method, description)
        else:
            messagebox.showerror("Błąd", "Niepoprawny rodzaj transakcji!")
            return

        self.report.add_transaction(transaction)
        self.update_display()

    def show_transaction_history(self):
        history_report = self.report.generate_transaction_history_report()
        history_window = Toplevel(self.root)
        history_window.title("Historia transakcji")
        history_text = Text(history_window)
        history_text.insert(END, history_report)
        history_text.pack()

        save_button = Button(history_window, text="Zapisz do pliku", command=lambda: self.save_report_to_file(history_report))
        save_button.pack()

    def change_view(self):
        self.report.change_view()
        self.update_display()

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
