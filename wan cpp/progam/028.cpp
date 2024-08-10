#include <iostream>

int main(){

    int x, y;

    std::cin >> x >> y;

    if (x > y)
    {
        std::cout << 2;
        
    }
    else
    {
    if(y % x == 0)
        {
            std::cout << y / x;
        }
        else
        {
            std::cout << (y / x) + 1;
        }
    }
}