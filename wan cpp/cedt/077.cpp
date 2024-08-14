#include <iostream>
#include <cmath>

using namespace std;

int main(){

    double input[4] = {0}, temp;

    for (int i = 0; i < 4; i++)
    {
        cin >> input[i];
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3 - i; j++)
        {
            if (input[j] > input[j+1])
            {
                temp = input[j];
                input[j] = input[j+1];
                input[j+1] = temp;
            }
        }
    }
    cout <<  round(((input[2] + input[1]) / 2.0 )*100.0)/100.0;
}