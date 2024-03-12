# %% Zadanie 1

class Animal():
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight

    
    @staticmethod
    def oldest_animal(animals):
        animal = max(animals, key=lambda x:x.age)
        return f"Najstarsze zwierze to {animal.name} i ma {animal.age} lat"
    

    def is_endangered(self):
        return self.species == "Tiger"


    def calculate_bmi(self):
        return f"BMI wynosi {self.weight / (1**2)}"




obj1 = Animal("Leo", 12, "Lion", 40)
obj2 = Animal("Sam", 16, "Cat", 20)
obj3 = Animal("Rex", 9, "Dog", 10)
obj4 = Animal("Diego", 21, "Tiger", 30)


print(Animal.oldest_animal([obj1, obj2, obj3, obj3]))
print(obj3.is_endangered())
print(obj4.is_endangered())
print(obj4.calculate_bmi())

# %% Zadanie 2
class Farm():
    animals = []
    def add_animal(self, new_animal):
        Farm.animals.append(new_animal)

    def feed_all(self):
        for animal in Farm.animals:
            print(f"{animal.name} został nakarmiony kukurydzą")

    
        
    @classmethod
    def create_farm_with_animals(cls, animals2):
        for animal2 in animals2:
            cls().add_animal(animal2)
        



farm = Farm()
cow = Animal("Berta", 5, "cow", 400)
farm.add_animal(cow)
chicken1 = Animal("Chirpy", 1, "chicken", 1)
farm.add_animal(chicken1)
chicken2 = Animal("Cluck", 2, "chicken", 1.2)
farm.add_animal(chicken2)
farm.feed_all()



animals = [
Animal("Berta", 5, "cow", 400),
Animal("Chirpy", 1, "chicken", 1),
Animal("Cluck", 2, "chicken", 1.2)
]

farm1 = Farm.create_farm_with_animals(animals)

# %% Zadanie 3

class Student():
    def __init__(self, first_name,last_name, age, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.gpa = gpa

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_on_prohibition(self):
        return self.gpa < 2.75
    
    @staticmethod
    def get_average_age(students):
        total_age = sum(student.age for student in students)
        return total_age / len(students)
    
    @staticmethod
    def get_student_by_year(students):
        dic = {
            "1 rok": [],
            "2 rok": [],
            "3 rok": [],
            "4 rok": [],
            "5 rok": []
        }
        for student in students:
            key = f"{student.year} rok"
            dic[key].append(student)

        return dic
    
    @staticmethod
    def print_students_by_year(students):
        dic = Student.get_student_by_year(students)
        for key, value in dic:
            print(key,value)



s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
s2 = Student("Anna", "Nowak", 22, 3, 2.8)
s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)

print(s1.get_full_name())
print(s3.is_on_prohibition())
print(Student.get_average_age([s1,s2,s3,s4]))
print(Student.get_student_by_year([s1,s2,s3,s4]))
Student.print_students_by_year([s1,s2,s3,s4])













