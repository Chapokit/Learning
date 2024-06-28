#include <iostream>
#include <cmath>
#include <ctime>

void showbalance(double balance);
double deposite(double deposite, double balance);
double withdraw(double withdraw, double balance);

int main()
{
    double balance = 0, depo, with;
    int choice = 0;

    

    
    do
    {
        std::cout << "What you want to do (1 show balance ,2 deposite , 3 withdraw, 4 exit): ";
        std::cin >> choice;
        if (choice == 2) 
        {
        std::cout << "How much you want to deposite : ";
        std::cin >> depo;
        balance = deposite(depo, balance);
        std::cout << "Balance is " << balance << " $\n";
        }
        else if(choice == 3)
        {
        std::cout << "How much you want to withdraw : ";
        std::cin >> with;
        balance = withdraw(with, balance);
        std::cout << "Balance is " << balance << " $\n";
        }
        else if (choice == 1)
        {
            showbalance(balance);
        }
        else if (choice == 4)
        {
            std::cout << "THANK YOU\n";
        }
} while (choice != 4);

    
    
}

void showbalance(double balance)
{
    std::cout << "Your balance is " << balance << " $"<< std::endl;
}

double deposite(double deposite, double balance)
{
    balance = balance + deposite;
    std::cout << "You have deposite " << deposite << " $" << std::endl;
    return balance;
}

double withdraw(double withdraw, double balance)
{
    if (balance < withdraw)
    {
        std::cout << "You don't have enough money " << std::endl;
    }
    else
    {
        balance = balance - withdraw;
        std::cout << "You have withdraw " << withdraw << " $" << std::endl;  
    }
    return balance;
}