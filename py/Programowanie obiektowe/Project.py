import collections
import datetime
import abc
import matplotlib.pyplot as plt


class Transaction(abc.ABC):
    def __init__(self,amount,title,category,method,description="Brak opisu",):
        self.id = id(self)
        self.__title = title
        self.__description = description
        self.__amount = amount
        self.__category = category
        self.__method = method
        self.__date = datetime.date.today()


    
    def __str__(self):
        return f"Numer transakcji {self.id} Tytuł { self.__title}\n Opis: {self.__description}\n Kwota {self.__amount} zł\n Data: {self.__date}"

    def __repr__(self):
        return f"Numer transakcji {self.id} Tytuł { self.__title}\n Opis: {self.__description}\n Kwota {self.__amount} zł\n Data: {self.__date}"


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
        self.income = sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Income))
        self.expense = sum(transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Expense))
        self.balance = self.income - self.expense
        print(self.transaction_history)

    def calculate_Income(self):
        return f"Zarobki: {self.income} zł"

    def calculate_expenses(self):
        return f"Wydatki: {self.expense} zł"

        
    def get_balance(self):
        return f"Aktualny stan konta: {self.balance} zł"

    def generate_balance_raport(self):
        return f"Raport finansowy\n Aktualny stan konta: {self.balance} zł\n Zarobki: {self.income}zł\n Wydatki: {self.expense}zł"

    def summary(self):

        dates_income = [transaction.date for transaction in self.transaction_history.values() if isinstance(transaction, Income)]
        dates_expense = [transaction.date for transaction in self.transaction_history.values() if isinstance(transaction, Expense)]
        incomes = [transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Income)]
        expenses = [transaction.amount for transaction in self.transaction_history.values() if isinstance(transaction, Expense)]
        plt.plot(dates_income, incomes, color='green')
        plt.show()
        plt.plot(dates_expense,expenses, color="red")
        plt.show()


    



przelew_1 = Income(69,"lód","Seks","Blik")
przelew_2 = Income(61,"lód","Seks","Blik")
przelew_3 = Expense(691,"lód","Seks","Blik")
przelew_4 = Expense(123,"lód","Seks","Blik")
przelew_5 = Income(123,"lód","Seks","Blik")
przelew_6 = Income(123,"lód","Seks","Blik")
przelew_7 = Income(292,"lód","Seks","Blik")
przelew_8 = Income(621,"lód","Seks","Blik")
przelew_9 = Expense(532,"lód","Seks","Blik")
przelew_10 = Expense(100,"lód","Seks","Blik")
przelew_11 = Expense(234,"lód","Seks","Blik")
przelew_12 = Expense(123,"lód","Seks","Blik")






przelew_1.date = przelew_1.date.replace(month=1)
przelew_2.date = przelew_2.date.replace(month=2)
przelew_3.date = przelew_3.date.replace(month=3)
przelew_4.date = przelew_4.date.replace(month=4)
przelew_9.date = przelew_9.date.replace(month=9)
przelew_10.date = przelew_10.date.replace(month=10)
przelew_11.date = przelew_11.date.replace(month=11)
przelew_12.date = przelew_12.date.replace(month=12)
przelew_5.date = przelew_5.date.replace(month=5)
przelew_6.date = przelew_6.date.replace(month=6)
przelew_7.date = przelew_7.date.replace(month=7)
przelew_8.date = przelew_8.date.replace(month=8)
# print(przelew_1.date)


konto = FinanceReport()
konto.add_transaction(przelew_1)
konto.add_transaction(przelew_2)
konto.add_transaction(przelew_3)
konto.add_transaction(przelew_4)
konto.add_transaction(przelew_5)
konto.add_transaction(przelew_6)
konto.add_transaction(przelew_7)
konto.add_transaction(przelew_8)
konto.add_transaction(przelew_9)
konto.add_transaction(przelew_10)
konto.add_transaction(przelew_11)
konto.add_transaction(przelew_12)


print(konto.calculate_Income())
print(konto.calculate_expenses())
print(konto.get_balance())
print(konto.generate_balance_raport())
print(konto.summary())





