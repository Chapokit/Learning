#include <stdio.h>

int main()
{
    int a, b, c, sum, A, B, C;
    0<=a<=30;
    0<=b<=30;
    0<=c<=40;

    scanf("%d %d %d", &a, &b, &c);    
    sum = a + b + c;
    

    if (sum>=65){
        if(sum<=69){
          printf("C+");
        }
        else if(sum<=74){
            printf("B");
        }
        else if(sum<=79){
            printf("B+");
        }
        else{
            printf("A");
        }
    }

    if (sum<65){
        if(sum>=60){
            printf("C");
        }        
        else if(sum>=55){
            printf("D+");
        }
        else if(sum>=50){
            printf("D");
        }
        else {
            printf("F");
        }
    } 

   
    
}