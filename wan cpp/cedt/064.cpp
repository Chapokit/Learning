#include <iostream>

using namespace std;

void bracketSwap(string text);

int main(){

    string text;

    getline(cin, text);

    bracketSwap(text);

}

void bracketSwap(string text)
{
    for (int i = 0; i < text.length(); i++)
    {
        if (text[i] == '(')
        {
            text[i] = '[';
        }
        else if (text[i] == ')')
        {
            text[i] = ']';
        }
        else if (text[i] == '[')
        {
            text[i] = '(';
        }
        else if (text[i] == ']')
        {
            text[i] = ')';
        }
    }
    cout << text;
}