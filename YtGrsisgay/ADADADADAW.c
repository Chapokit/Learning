#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    srand(time(0));

    int Num = (rand() % 100) + 1;
    int guess, i = 0;

    printf("enter number : ");
    scanf("%d", &guess);

    while(guess != Num)
    {
        if(guess < Num)
        {
            printf("lower\nguess new number between : ");
            scanf("%d", &guess);
            i += 1;
        }
        if(guess > Num)
        {
            printf("higher\nguess new number between : ");
            scanf("%d", &guess);
            i += 1;
        }
    }
    if(guess = Num)
    {
        printf("correct");
        printf("you have guess %d times", i);
    }

}