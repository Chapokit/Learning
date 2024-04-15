#include <stdio.h>
#include <math.h>

int main(){

    char grade;

    printf("\nEnter grade : ");
    scanf("%c", &grade);

    switch(grade){
        case 'A':
            printf("W");
            break;
        case 'B':
            printf("you did well");
            break;
        case 'C':
            printf("not bad");
            break;
        case 'D':
            printf("kbo");
            break;
        case 'F':
            printf("L");
            break;
        default:
        printf("?");
    }

    return 0;
}