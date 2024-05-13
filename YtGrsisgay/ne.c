#include <stdio.h>
#include <string.h>

typedef struct 
{
    char name[20];
    char vvvv[20];
    int score;

}Player;


int main(){

    Player n1 = {"Wan", "dalkjnakln", 52};
    Player n2 = {"naQ", "dadsdsadadasdad", 233};
    
    printf("%s\n", n1.name);
    printf("%s\n", n1.vvvv);
    printf("%d\n", n1.score);

    printf("%s\n", n2.name);
    printf("%s\n", n2.vvvv);
    printf("%d\n", n2.score);

    return 0;
}