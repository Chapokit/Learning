#include<stdio.h>
#include<ctype.h>

int main(){
    
    int num1, num2, num3, min, max, med;    
    /*scanf("%d %d %d", &num1, &num2, &num3);                       //////METHOD 1
    if(num1>num2 && num1>num3){          //num1 is maximum
        max=num1;
        if(num2>num3){
            med=num2;
            min=num3;
        }
        else if(num3>num2){
            med=num3;
            min=num2;
        }
    }

    if(num2>num1 && num2>num3){          //num2 is maximum
        max=num2;
        if(num1>num3){
            med=num1;
            min=num3;
        }
        else if(num3>num1){
            med=num3;
            min=num1;
        }
    }

    if(num3>num2 && num3>num1){          //num3 is maximum
        max=num3;
        if(num2>num1){
            med=num2;
            min=num1;
        }
        else if(num1>num2){
            med=num1;
            min=num2;
        }
    }*/

    
    for(int i=0 ; i<3 ; i++){                                       //////METHOD 2   
        scanf("%d", &num1);
        if(i == 0){               //555
            min=num1; 
            med=num1;
            max=num1;
        }
        else if(num1<min){
            med=min;              //345 456
            min=num1;       
        }
        else if(num1>max){        //567
            med=max;                   
            max=num1;
        }
        else {
            med=num1;             //GGEZ
        }
    }
    
       
    char text[3];     //={0,1,2,3}
    scanf("%s", &text);
    for(int j=0 ; j<3 ; j++){
        if(text[j] == 'A'){
            printf("%d ", min);
        }
        else if(text[j] == 'B'){
            printf("%d ", med);
        }
        else if(text[j] == 'C'){
            printf("%d ", max);
        }
    }

    return 0;
}