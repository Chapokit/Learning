#include <iostream>
#include <cmath>
#include <ctime>

std::string concatStrings(std::string string1, std::string string2);

int main(){

    std::string firstName = "Wan";
    std::string lastName = "Nachapol";
    std::string fullName = concatStrings(firstName, lastName);

    std::cout << "Hello " << fullName;

    return 0;
}

std::string concatStrings(std::string string1, std::string string2)
{
    return string1 + " " + string2;
}