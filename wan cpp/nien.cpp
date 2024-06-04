#include <iostream>
#include <cmath>


int main(){

    char op;
    double num1, num2;

    std::cout << "+++++++++++CALCULATOR++++++++++++++"<< '\n';

    std::cout << "input num1 : ";
    std::cin >> num1;

    std::cout << "input num2 : ";
    std::cin >> num2;

    std::cout << "choose operator (+ - * /) : ";
    std::cin >> op;
    
    switch(op)
    {
        case '+':
            std::cout << "result is " << num1 + num2 << '\n';
            break;
        case '-':
            std::cout << "result is " << num1 - num2 << '\n';
            break;
        case '*':
            std::cout << "result is " << num1 * num2 << '\n';
            break;
        case '/':
            std::cout << "result is " << num1 / num2 << '\n';
            break;
        default:
            std::cout << "Please enter valid operator : "<< '\n';
    };

    std::cout << "+++++++++++++++++++++++++++++++++++";
    return 0;
}