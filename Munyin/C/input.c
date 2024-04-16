#include <stdio.h>
#include <string.h>

int main(){

    int age;
    char name[25]; // bytes

    printf("What's your name?");
    //scanf("%s", &name);
    fgets(name, 25 ,stdin); // can new line char
    name[strlen(name)-1] = '\0';

    printf("How old are you?");
    scanf("%d", &age);

    printf("\nYou are %d years old", age);
    printf("\nYou are %s", name);

    char[];



    return 0;

}