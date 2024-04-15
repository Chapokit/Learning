#include <stdio.h>

int main(){
    const double PI = 3.14159;
    double radius,circumference,area;
    
    printf("Input radius of circle : ");
    scanf("%lf", &radius);

    circumference = 2 * PI * radius;
    area = PI * radius * radius;

    printf("circumference : %lf\n", circumference);
    printf("area : %lf",  area);

    return 0;
}