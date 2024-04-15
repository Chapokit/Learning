#include <stdio.h>
#include <math.h>

int main(){

    int age;

    printf("Enter age : ");
    scanf("%d", &age);

    if(age >= 18){
        printf("You are able to get into jail");
    }
    else if(age < 0){
        printf("r u kidding ?????");
    }
    else{
        printf("Nabro u 2 young");
    }

    return 0;
}