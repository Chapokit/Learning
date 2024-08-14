#include <iostream>

using namespace std;

int main(){

    double input;

    cin >> input;

    if (input >= 80)
    {
        cout << "A";
    }
    else if (input >= 70)
    {
        cout << "B";
    }
    else if (input >= 60)
    {
        cout << "C";
    }
    else if (input >= 50)
    {
        cout << "D";
    }
    else 
    {
        cout << "F";
    }

}