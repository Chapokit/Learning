#include <iostream>

using namespace std;

int main(){

    string phoneNum;

    cin >> phoneNum;

    if (phoneNum.length() == 10)
    {
        if (phoneNum[0] == '0')
        {
            if (phoneNum[1] == '6' || phoneNum[1] == '8' || phoneNum[1] == '9')
            {
                cout << "Mobile number";
            }
            else
            {
                cout << "Not a mobile number";
            }
        }
        else
        {
            cout << "Not a mobile number";
        }
    }
    else
    {
        cout << "Not a mobile number";
    }
}