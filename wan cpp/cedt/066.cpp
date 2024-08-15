#include <iostream>

using namespace std;

bool isDelimiter(char ch);

int main(){

    string wanted, text;
    int countbig = 0;

    cin >> wanted;
    cin.ignore();
    getline(cin ,text);

    for (int i = 0; i <= text.length() - wanted.length(); i++)
    {   
        int countsmall = 0;
        if ((i == 0 || isDelimiter(text[i - 1])) && (i + wanted.length() == text.length() || isDelimiter(text[i + wanted.length()])))
        {
            for (int j = 0; j < wanted.length() ; j++)
            {
                if (text[i + j] == wanted[j])
                {
                    countsmall++;
                }
                else 
                {
                    break;
                }
                
            }
            
        }
        if (countsmall == wanted.length())
        {
            countbig++;
        }  
    }
    cout << countbig;
}

bool isDelimiter(char ch) 
{
    return !(ch >= 'a' && ch <= 'z') && !(ch >= 'A' && ch <= 'Z') && !(ch >= '0' && ch <= '9');
}