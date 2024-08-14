#include <iostream>
#include <cmath>

using namespace std;

int main(){

    long long sub;
    
    cin >> sub;

    int l = log10(sub) + 1;

    if (l < 4)
    {
        cout << sub;
    }
    else if (l < 5)
    {
        cout << round(((double)sub / 1000)*10)/10.0 << "K";
    }
    else if (l < 7)
    {
        cout << round((double)sub / 1000) << "K";
    }
    else if (l < 8)
    {
        cout << round(((double)sub / 1000000)*10)/10.0 << "M";
    }
    else if (l < 10)
    {
        cout << round((double)sub / 1000000) << "M";
    }
    else if (l < 11)
    {
        cout << round(((long double)sub / 1000000000)*10)/10.0 << "B";
    }
    else
    {
        cout << round((long double)sub / 1000000000) << "B";
    }
}