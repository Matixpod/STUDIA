# %%
class Test :
    def __del__ ( self ) :
        print ('Bye Class ')
obj = Test ()
obj2 = obj
del obj
del obj2
print ('End ')
# %%
class A:
    def foo ( self ) :
        print (" Metoda foo w klasie A")
class B( A):
    def foo ( self ) :
        print (" Metoda foo w klasie B")
class C( A):
    def foo ( self ) :
        print (" Metoda foo w klasie C")
class D(B , C):
    pass 
obj = D ()
obj . foo ()
print (D. __mro__ ) # Sprawd ź MRO dla klasy D
print (D. mro () ) # Lub


# %%
class Ninja:
    def __init__ ( self):
        self.__x = 100
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_value):
        self.__x = new_value

nin = Ninja()
print(nin.x)
nin._Ninja__x = 10
# nin.x = 10
print(nin.x)
# %%



class Bank_account():
    def __init__(self,name,surname) -> None:
        self.name = name
        self.surname = surname
        self.__id = id(self)
        self.__money = 0


    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self,value):
        self.__money = value
        

    def __repr__(self) -> str:
        return f"Konto {self.name} {self.surname}\n stan konta: {self.__money} zł"
    
    def __del__(self):
        return "Konto zamknięte!"

acc1 = Bank_account('Mateusz','Podporski')
print(acc1)
acc1.money = 1000000
print(acc1)
del acc1






