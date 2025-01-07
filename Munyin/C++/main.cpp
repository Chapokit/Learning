#include <iostream>
using namespace std;

int main()
{
    int min;
    int max;
    int input;

    for (int i = 0; i < 6; i++)
    {
        cin >> input;
        if (i == 0)
        {
            min = input;
            max = input;
        }
        else
        {
            if (input < min)
            {
                min = input;
            }
            if (input > max)
            { // Change to 'if' instead of 'else if'
                max = input;
            }
        }
    }

    cout << min << endl;
    cout << max << endl;

    return 0;
}
