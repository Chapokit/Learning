#include <iostream>

using namespace std;

int main(){

    string answer, solution;
    int count = 0;

    cin >> solution;
    cin.ignore();
    getline(cin, answer);

    if (solution.length() > answer.length())
    {
        cout << "Incomplete answer";
    }
    else
    {
        for (int i = 0; i < solution.length(); i++)
        {
            if (solution[i] == answer[i])
            {
                count++;
            }
            
        }
        cout << count;
    }
}
