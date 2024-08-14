#include <iostream>
using namespace std;

int main() {
    string name[2];
    float gpax[2];
    char comprog[2];
    char cal1[2];
    char cal2[2];

    for (int i = 0; i < 2; i++)
    {
        cin >> name[i] >> gpax[i] >> comprog[i] >> cal1[i] >> cal2[i];

        if (comprog[i] > 'A')
        {
            comprog[i] = '0';
        }
        if (cal1[i] > 'C')
        {
            cal1[i] = '0';
        }
        if (cal2[i] > 'C')
        {
            cal2[i] = '0';
        }
    }

    if (gpax[0] > gpax[1])
    {
        if (comprog[0] != '0' && cal1[0] != '0' && cal2[0] != '0')
        {
            cout << name[0];
        }
        else if (comprog[1] != '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            cout << name[1];
        } else
        {
            cout << "None";
        }
    }
    else if (gpax[0] < gpax[1])
    {
        if (comprog[1] != '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            cout << name[1];
        } else if (comprog[0] != '0' && cal1[0] != '0' && cal2[0] != '0')
        {
            cout << name[0];
        } else
        {
            cout << "None";
        }
    }
    else
    {
        if(comprog[0] != '0' && cal1[0] != '0' && cal2[0] != '0' && comprog[1] != '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            if (cal1[0] < cal1[1])
            {
                cout << name[0];
            }
            else if (cal1[0] > cal1[1])
            {
                cout << name[1];
            }
            else
            {
                if (cal2[0] < cal2[1])
                {
                    cout << name[0];
                }
                else if (cal2[0] > cal2[1])
                {
                    cout << name[1];
                } 
                else
                {
                    cout << "Both";
                }
            }
        }
        else if (comprog[0] != '0' && cal1[0] != '0' && cal2[0] != '0' && comprog[1] == '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            cout << name[0];
        }
        else if (comprog[0] == '0' && cal1[0] != '0' && cal2[0] != '0' && comprog[1] != '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            cout << name[1];
        }
        else if (comprog[0] != '0' && cal1[0] != '0' && cal2[0] != '0' && comprog[1] != '0' && cal1[1] == '0' && cal2[1] != '0')
        {
            cout << name[0];
        }
        else if (comprog[0] != '0' && cal1[0] == '0' && cal2[0] != '0' && comprog[1] != '0' && cal1[1] != '0' && cal2[1] != '0')
        {
            cout << name[1];
        }
        
        else
        {
            cout << "None";
        }
    }

    return 0;
}
