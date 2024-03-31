#include <stdio.h>
#include <stdbool.h>

int main(){

    //left and right align
    float item1 = 5.34;
    float item2 = 6.43;
    float item3 = 100.54;

    printf("Item 1: %-8.2f dollars\n", item1);
    printf("Item 1: %-8.2f dollars\n", item2);
    printf("Item 1: %-8.2f dollars\n", item3);
}