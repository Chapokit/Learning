#include <iostream>

using namespace std;

int main(){

    int h, noy, h2;

    cin >> h;

    noy = h;

    h2 = h;

    for (int i = 1; i <= h2; i++)
    {
        for (int j = 1; j <= h; j++)
        {
            
            if (j == h || j == noy)
            {
                cout << "*";
            }
            else if (i == h2)
            {
                cout << "*";
            }
            else
            {
                cout << ".";
            }
        }
        cout << "\n";
        h++;
        noy--;
        
    }
}
