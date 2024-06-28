#include <iostream>
#include <cmath>

int main() {
    int num1, num2, hrm = 1;
    
    std::cin >> num1 >> num2;
    
    for (int i = std::min(num1, num2); i > 0; i--)
    {
        if (num1 % i == 0 && num2 % i == 0) {
            hrm = i;
            break;
        }
    }
    
    std::cout << hrm;
    return 0;
}
