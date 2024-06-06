#include <iostream>
#include <cmath>
#include <ctime>

void happyBirthday(std::string name, int age);


int main(){

    std::string name = "Wan";
    int age = 18;

    happyBirthday(name, age);
    
    return 0;
}

void happyBirthday(std::string name, int age)
{
    std::cout << "Happy birthday to " << name << '\n';
    std::cout << "Happy birthday to " << name << '\n';
    std::cout << "Happy birthday dear " << name << '\n';
    std::cout << "Happy birthday to " << name << '\n';
    std::cout << "You are " << age << " years old";
}