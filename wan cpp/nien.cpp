#include <iostream>
#include <cmath>


int main(){

    int temp;
    char unit;

    std::cout << "input temperture unit (C or F) : ";
    std::cin >> unit;

    unit = toupper(unit);

    std::cout << "Input temperture : ";
    std::cin >> temp;

    switch (unit)
    {
    case 'C':
        std::cout << "The temperture is " << (double)temp * 9 / 5 + 32 << " Fahrenheit" ;
        break;
    case 'F':
        std::cout << "The temperture is " << (double)(temp - 32) * 5 / 9 << " Celsius" ;
        break;
    default:
        std::cout << "Please input valid unit ";
        break;
    }

    return 0;
}