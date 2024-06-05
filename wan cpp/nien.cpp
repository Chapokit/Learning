#include <iostream>
#include <cmath>


int main(){

    int row;
    int column;
    char symbol;

    std::cout << "How many rows : ";
    std::cin >> row;

    std::cout << "How many column : ";
    std::cin >> column;

    

    
    for (int i = 1; i <= row; i++)
    {
        if(i == 1 || i == row)
        {
            for (int j = 1; j <= column; j++)
            {
                std::cout << "_";
            }
            
        }
        else
        {
            for (int k = 1; k <= column; k++)
            {
                if(k == 1 || k == column)
                {
                    std::cout << "|";
                }
                else
                {
                    std::cout << ' ';
                }
            }
            
        }
        std::cout << '\n';
    }
    
    
    return 0;
}