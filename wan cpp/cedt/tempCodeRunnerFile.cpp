#include <iostream>

using namespace std;

int main(){

    string wanted, text;
    int countbig = 0;

    cin >> wanted;
    cin.ignore();
    getline(cin ,text);

    for (int i = 0; i <= text.length() - wanted.length(); i++)
    {   
        int countsmall = 0;
        if (text[i] == wanted[0] && text[i - 1] == ' ' && i != 0)
        {
            countsmall++;
            for (int j = 1; j < wanted.length() ; j++)
            {
                if (text[i + j] == wanted[0 + j] && i != 0 && i != text.length() - wanted.length())
                {
                    countsmall++;
                }
                else 
                {
                    break;
                }
                if (j == wanted.length() - 1 && text[i + wanted.length()] != ' ')
                {
                    countsmall = 0;
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