#include <iostream>
#include <algorithm>

using namespace std;

void plusString(string text1, string text2);
void multiplyString(string text1, string text2);

int main(){

    string text1, text2;
    char operation;

    cin >> text1 >> operation >> text2;

    switch (operation)
    {
        case '+':
            plusString(text1, text2);
            break;
        case '*':
            multiplyString(text1, text2);
            break;
    }

}

void plusString( string text1, string text2)
{
    int length1 = text1.length();
    int length2 = text2.length();

    if ( length1 > length2)
    {
        text1[length1 - length2] = '1';
        cout << text1;
    }
    else if (length2 > length1)
    {
        text2[length2 - length1] = '1';
        cout << text2;
    }
    else
    {
        text2[0] = '2';
        cout << text2;
    }
}
void multiplyString(string text1, string text2)
{
    int length1 = text1.length();
    int length2 = text2.length();

    cout << '1';

    for (int i = 0; i < length1 + length2 - 2; i++)
    {
        cout << '0';
    }
    
}