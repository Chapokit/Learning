#include <iostream>
#include <ctime>

using namespace std;

int Days(int dueng);
void Dayfinder(int one);

int main(){

    int one, dueng;

    cin >> one >> dueng;

    one += Days(dueng);;

    one = one % 7;

    Dayfinder(one);
}


int Days(int dueng)
{
    int day;
    switch (dueng)
    {
    case 1:
        day = 0;
        return day;
        break;
    case 2:
        day = 31;
        return day;
        break;
    case 3:
        day = 59;
        return day;
        break;
    case 4:
        day = 90;
        return day;
        break;
    case 5:
        day = 120;
        return day;
        break;
    case 6:
        day = 151;
        return day;
        break;
    case 7:
        day = 181;
        return day;
        break;
    case 8:
        day = 212;
        return day;
        break;
    case 9:
        day = 243;
        return day;
        break;
    case 10:
        day = 273;
        return day;
        break;
    case 11:
        day = 304;
        return day;
        break;
    case 12:
        day = 334;
        return day;
        break;
    }
    return 0;
}
void Dayfinder(int one)
{
    switch (one)
    {
    case 1:
        cout << "Thursday";
        break;
    case 2:
        cout << "Friday";
        break;
    case 3:
        cout << "Saturday";
        break;
    case 4:
        cout << "Sunday";
        break;
    case 5:
        cout << "Monday";
        break;
    case 6:
        cout << "Tuesday";
        break;
    case 0:
        cout << "Wednesday";
        break;
    }
}