#include <stdio.h>
#include <math.h>

int main(){

    double A, B ,C;

    printf("Enter side A : ");
    scanf("%lf", &A);

    printf("Enter side B : ");
    scanf("%lf", &B);

    C = sqrt(pow(A,2) + pow(B,2));

    printf("side C = %lf", C);

    return 0;
}