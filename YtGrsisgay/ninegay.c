#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main(){

    char operator;
    double num1, num2;
    double result;

    printf("Enter an operator (+ - * /) : ");
    scanf("%c", &operator);

    printf("Enter Number 1 : ");
    scanf("%lf", &num1);

    printf("Enter Number 2 : ");
    scanf("%lf", &num2);

    switch(operator){
        case '+':
            result = num1 + num2;
            printf("%lf", result);
            break;
        case '-':
            result = num1 - num2;
            printf("%lf", result);
            break;
        case '*':
            result = num1 * num2;
            printf("%lf", result);
            break;
        case '/':
            result = num1 / num2;
            printf("%lf", result);
            break;
        default:
            printf("?????");
    }

    return 0;
}