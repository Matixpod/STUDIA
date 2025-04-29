#include <iostream>
#include <cmath>
#include <string>

void displayVariables() {
    int intVar = 10;
    double doubleVar = 5.7;
    std::string stringVar = "Hello, World!";
    
    int convertedVar = static_cast<int>(doubleVar);

    std::cout << "Integer: " << intVar << std::endl;
    std::cout << "Double (converted to int): " << convertedVar << std::endl;
    std::cout << "String: " << stringVar << std::endl;
}

void performArithmeticOperations() {
    int num1, num2;
    std::cout << "Enter two integers: ";
    std::cin >> num1 >> num2;

    std::cout << "Sum: " << (num1 + num2) << std::endl;
    std::cout << "Difference: " << (num1 - num2) << std::endl;
    std::cout << "Product: " << (num1 * num2) << std::endl;
    if (num2 != 0) {
        std::cout << "Quotient: " << (num1 / num2) << std::endl;
    } else {
        std::cout << "Division by zero is not allowed." << std::endl;
    }
}

void calculateCircleArea() {
    double radius;
    std::cout << "Enter the radius of the circle: ";
    std::cin >> radius;

    const double area = M_PI * radius * radius;
    std::cout << "The area of the circle is: " << area << std::endl;
}

void checkEvenOrOdd() {
    std::cout << "Enter number to check if it's even or odd: ";
    int num;
    std::cin >> num;
    if (num % 2 == 0) {
        std::cout << num << " is even." << std::endl;
    } else {
        std::cout << num << " is odd." << std::endl;
    }
}

void displayAsciiCode() {
    char character;
    std::cout << "Enter a character: ";
    std::cin >> character;
    std::cout << "The ASCII code of '" << character << "' is: " << static_cast<int>(character) << std::endl;
}

void display_1_to_10(){
    std::cout << "Number from 1 to 10:" << std::endl;
    for (int i = 1; i <= 10; i++){
        std::cout << i << " ";
    }
}

void display_sum_of_odds_1_100(){
    int sum = 0;
    for (int i = 1; i<100;i++){
        if (i%2!=0){
            sum+=i;
        }
    }
    std::cout << "Sum of odd numbers from 1 to 100 is: " << sum << std::endl;
}

int main() {
    // displayVariables();
    // performArithmeticOperations();
    // calculateCircleArea();
    // checkEvenOrOdd();
    // displayAsciiCode();
    // display_1_to_10();
    display_sum_of_odds_1_100();

    return 0;
}

struct Student {
    std::string imie;
    int wiek;
};

void displayStudentInfo() {
    Student student;
    std::cout << "Podaj imie studenta: ";
    std::cin >> student.imie;
    std::cout << "Podaj wiek studenta: ";
    std::cin >> student.wiek;

    std::cout << "Imie: " << student.imie << ", Wiek: " << student.wiek << std::endl;
}