#include <iostream>

using namespace std;

int main(){

    int weight;

    cin >> weight;

    if (weight <= 100 && weight > 0) cout << "18";
    else if (weight <= 250 && weight > 0) cout << "22";
    else if (weight <= 500 && weight > 0) cout << "28";
    else if (weight <= 1000 && weight > 0) cout << "38";
    else if (weight <= 2000 && weight > 0) cout << "58";
    else cout << "Reject";
}