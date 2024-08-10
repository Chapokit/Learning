#include <iostream>
#include <cmath>
#include <string>

using namespace std;

long gcd(long a, long b) {
 if (b == 0) return a;
 return gcd(b, a%b);
}

int main(){

    string text1, text2 , text3 , allstring;

    cin >> text1 >> text2 >> text3;

    int lastdigit = text3.length();
    int middigit = text2.length();

    int mid = stoi(text2);
    int front = stoi(text1);
    
    allstring = text2.append(text3); 

    int alldecimal = stoi(allstring);

    int oneee = 1;
    for (int i = 1; i < middigit; i++)
    {
        oneee = (oneee * 10) + 1;
    }
    
    int bon = alldecimal - mid;
    int lang = pow(10, lastdigit) * (oneee * 9);

    int lek = lang * front;

    int musthan = gcd(lek + bon, lang);

    cout << (lek + bon) / musthan << " / " << lang / musthan;
}