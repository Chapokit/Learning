#include <iostream>
#include <cmath>
//6011000990139424

int main(){

    long long int num;
    int sum1 = 0;
    int sum2 = 0;

    std::cout << "*****Credit Card Checker*****" << '\n';
    std::cout << "Please enter your credit card : ";
    std::cin >> num;
    
    long long num1 = round(num / 10);
    long long num2 = num;
    

    for (int i = 1; num1 > 0; i++)
    {
       
        int rm1;
        
        rm1 = num1 % 10;
        rm1 *= 2;
        if (rm1 < 10)
        {
            sum1 += rm1;
            num1 /= 100;
        }
        else
        {
            rm1 = (rm1 % 10) + 1;
            sum1 += rm1;
            num1 /= 100;
        }
          
    }
    for (int j = 1; num2 > 0; j++)
    {
        int rm2;
        rm2 = num2 % 10;
        sum2 += rm2;
        num2 /= 100;
    }
    
    if ((sum1 + sum2) % 10 == 0)
    {
        std::cout << "Your credit card is valid";
    }
    else
    {
        std::cout << "You have invalid credit card";
    }
    
    
}