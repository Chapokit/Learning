#include <iostream>
#include <cmath>
//6011000990139424

int Digit(int num);
int sumEven(std::string num);
int sumOdd(std::string num);

int main(){

    std::string ccnum;

    std::cout << "Input your credit card number : ";
    std::cin >> ccnum;

    if ((sumEven(ccnum) + sumOdd(ccnum)) % 10 == 0)
    {
        std::cout << "Your credit card is valid";
    }
    else
    {
        std::cout << "Your credit card is invalid";
    }
    
   

}

int Digit(int num)
{
    num = (num % 10) + ((num / 10) % 10);
    return num;
}
int sumEven(std::string num)
{
    int sum = 0;
    for (int i = num.size() - 2; i >= 0; i-=2)
    {
        sum += Digit((num.at(i) - '0') * 2);
    }
    return sum;
}
int sumOdd(std::string num)
{
    int sum = 0;
    for (int i = num.size() - 1; i >= 0; i-=2)
    {
        sum += (num.at(i) - '0');
    }
    return sum;
}