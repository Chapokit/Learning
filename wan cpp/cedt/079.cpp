#include <iostream>
#include <string>

using namespace std;

int main(){

     
    int count = 0;
    string input, rahus[27] = {"01", "02", "20", "21", "22", "23", "24", 
    "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", 
    "36", "37", "38", "39", "40", "51", "53", "55", "58"};

    cin >> input;


    for (int i = 0; i < 27; i++)
    {
        if (input.compare(rahus[i]) == 0)
        {
            count++;
            break;
        }
    }
    (count == 1) ? cout << "OK" : cout << "Error";
}