#include <stdio.h>
#include <math.h>

int main(){

    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    int d = a+b+c;

    if (d>=60){
        if (d<=64){
            printf("C");
        }
        else if (d<=69){
            printf("C+");
        }
        else if (d <= 74)
        {
            printf("B");
        }
        else if (d <= 79)
        {
            printf("B+");
        }
        else
        {
            printf("A");
        }
    }
    else if (d<60){
        if (d>=55){
            printf("D+");
        }
        else if (d>=50){
            printf("D");
        }
        else{
            printf("F");
        }
    }

}