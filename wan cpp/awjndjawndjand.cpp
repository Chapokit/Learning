#include <iostream>
#include <string>


int main(){

    std::string question[] = {"1.What year was C++ created? :",
                              "2.Who invented C++? : ",
                              "3.What is the predecessor of C++? :",
                              "4.Is nien gay? : "};

    std::string options[][4] = {{"A. 1969", "B. 1975", "C. 1985", "D. 1989"},
                                {"A. Guido van Rossum", "B. Bjarne Stroustrup", "C. John Carmack", "D. Mark Zuckerburg"},
                                {"A. C", "B. C+", "C. C--", "D. B++"},
                                {"A. Yes", "B. No", "C. Nah", "D. Nope"}};

    char answer[] = {'C', 'B', 'A', 'A'};

    int size = sizeof(question) / sizeof(question[0]);
    char guess;
    int score = 0;

    for (int i = 0; i < size; i++)
    {
        std::cout << "*************************************************\n";
        std::cout << question[i] << '\n';
        std::cout << "*************************************************\n";
        for (int j = 0; j < sizeof(options[i]) / sizeof(options[i][0]); j++)
        {
            std::cout << options[i][j] << '\n';
        }

        std::cin >> guess;

        guess = toupper(guess);

        if (guess == answer[i])
        {
            score++;
            std::cout << "Correct!!!" << '\n';
        }
        else
        {
            std::cout << "Nice try" << '\n';
        }
        
    }

    std::cout << "*************************************************\n";
    std::cout << "Thank you for playing Score = " << score << " / 4\n";
    std::cout << "*************************************************\n";
}