#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <limits>
#include <algorithm>

// Zadanie 1
void calculateSphereVolume() {
    double radius;

    std::cout << "Enter the radius of the sphere: ";
    std::cin >> radius;

    double volume = (4.0 / 3.0) * M_PI * pow(radius, 3);
    std::cout << "The volume of the sphere is: " << volume << std::endl;
}

// Zadanie 2
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

// Zadanie 3
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

// Zadanie 4
void length_and_1st_last_char(){
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    std::cout << "Length of the string: " << str.length() << std::endl;
    std::cout << "First character: " << str[0] << std::endl;
    std::cout << "Last character: " << str[str.length() - 1] << std::endl;
}

// Zadanie 5
void convertToUppercase() {
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    for (char &c : str) {
        c = std::toupper(c);
    }

    std::cout << "String in uppercase: " << str << std::endl;
}

// Zadanie 6
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

// Zadanie 7
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

// Zadanie 8
void find_min_in_array() {
    int arr[10];
    std::cout << "Enter 10 numbers: ";
    for (int i = 0; i < 10; ++i) {
        std::cin >> arr[i];
    }
    int min = arr[0];
    for (int i = 1; i < 10; ++i) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    std::cout << "Smallest number is: " << min << std::endl;
}

// Zadanie 9
void vector_grades_avg() {
    std::vector<double> oceny;
    double suma = 0;
    std::cout << "Enter 5 grades: ";
    for(int i = 0; i < 5; ++i) {
        double x;
        std::cin >> x;
        oceny.push_back(x);
        suma += x;
    }
    std::cout << "Average grade: " << suma / oceny.size() << std::endl;
}

// Zadanie 10
class Punkt {
    public:
        double x, y;
        Punkt(double x, double y) : x(x), y(y) {}
    
        double odlegloscOd(const Punkt& other) const {
            return std::sqrt(std::pow(this->x - other.x, 2) + std::pow(this->y - other.y, 2));
        }
    };
    
    void test_punkt() {
        double x1, y1, x2, y2;
        std::cout << "Enter x y for point 1: ";
        std::cin >> x1 >> y1;
        std::cout << "Enter x y for point 2: ";
        std::cin >> x2 >> y2;
        Punkt p1(x1, y1), p2(x2, y2);
        std::cout << "Distance: " << p1.odlegloscOd(p2) << std::endl;
    }

// Zadanie 11
void vector_above_50() {
    int n;
    std::cout << "How many numbers? ";
    std::cin >> n;
    std::vector<int> liczby;
    std::cout << "Enter numbers: ";
    for(int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        liczby.push_back(x);
    }
    std::cout << "Numbers > 50: ";
    for(int x : liczby) {
        if(x > 50) std::cout << x << " ";
    }
    std::cout << std::endl;
}

// Zadanie 12
void bubble_sort() {
    int arr[10];
    std::cout << "Enter 10 numbers: ";
    for(int i = 0; i < 10; ++i) {
        std::cin >> arr[i];
    }
    for(int i = 0; i < 9; ++i) {
        for(int j = 0; j < 9-i; ++j) {
            if(arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
            }
        }
    }
    std::cout << "Sorted: ";
    for(int i = 0; i < 10; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    calculateSphereVolume();
    check_if_in_section();
    calculateQuadraticFunction();
    length_and_1st_last_char();
    convertToUppercase();
    count_a();
    nth_fibonacci();
    find_min_in_array();
    vector_grades_avg();
    test_punkt();
    vector_above_50();
    bubble_sort();

    return 0;
}

