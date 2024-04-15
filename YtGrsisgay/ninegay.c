#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main(){

    char unit;
    float temp;

    printf("\nF or C : ");
    scanf("%c", &unit);

    unit = toupper(unit);

    if(unit == 'C'){
        printf("Enter temp in C ");
        scanf("%f", &temp);
        temp = (temp * 9 / 5) + 32;
        printf("\nTemp in F is %.1f ", temp);
    }
    else if(unit == 'F'){
        printf("Enter temp in F ");
        scanf("%f", &temp);
        temp = (temp -32) * 5 / 9;
        printf("\nTemp in C is %.1f ", temp);
    }
    else{
        printf(" %c whattt ???", unit);
    }

    
    

    return 0;
}