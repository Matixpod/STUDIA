#include <iostream>
#include <cmath>
#include <string>

void calculateSphereVolume() {
    double radius;

    std::cout << "Enter the radius of the sphere: ";
    std::cin >> radius;

    double volume = (4.0 / 3.0) * M_PI * pow(radius, 3);
    std::cout << "The volume of the sphere is: " << volume << std::endl;
}

void check_if_in_section() {
    int x;
    std::cout << "Enter number: ";
    std::cin >> x;
    if (x >= 10 && x <= 100){
        std::cout << "Number is in section [10-100]" << std::endl;
    } else {
        std::cout << "Number is not in section [10-100]" << std::endl;
    }
}

void calculateQuadraticFunction() {
    double a, b, c, x;

    std::cout << "Enter coefficient a: ";
    std::cin >> a;
    std::cout << "Enter coefficient b: ";
    std::cin >> b;
    std::cout << "Enter coefficient c: ";
    std::cin >> c;
    std::cout << "Enter argument x: ";
    std::cin >> x;

    double result = a * pow(x, 2) + b * x + c;
    std::cout << "The value of the quadratic function f(x) = ax^2 + bx + c is: " << result << std::endl;
}

void length_and_1st_last_char(){
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    std::cout << "Length of the string: " << str.length() << std::endl;
    std::cout << "First character: " << str[0] << std::endl;
    std::cout << "Last character: " << str[str.length() - 1] << std::endl;
}

void convertToUppercase() {
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    for (char &c : str) {
        c = std::toupper(c);
    }

    std::cout << "String in uppercase: " << str << std::endl;
}

void count_a(){
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    int count = 0;
    for (char c : str){
        if (c == 'a' || c == 'A'){
            count++;
        }
    }

    std::cout << "Number of 'a' or 'A' in the string: " << count << std::endl;
}

void nth_fibonacci() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    int a = 0, b = 1,next = 0;
    if (n == 1) {
        std::cout << "nth fibonacci number: " << a << std::endl;
        return;
    } else if (n == 2) {
        std::cout << "nth fibonacci number: " << a << ", " << b << std::endl;
        return;
    }else{
        for (int i = 2; i<=n;i++){
            next = a + b;
            a = b;
            b = next;
        }
    }
    std::cout << n <<"th Fibonacci number: " << next << std::endl;

}

int main() {
    // calculateSphereVolume();
    // check_if_in_section();
    // calculateQuadraticFunction();
    // length_and_1st_last_char();
    // convertToUppercase();
    // count_a();
    // nth_fibonacci();


    return 0;
}

