#include <stdio.h>

int main(){
    int min, max, a, b;
    scanf("%d", &b);
    for(int i=1 ; i <= b; i++){
        scanf("%d", &a);
        if(i == 1){
            min=a;
            max=a;
        }
        if(a<min){
            min=a;
        }
        if(a>max){
            max=a;
        }
        
    }
    
    printf("%d\n%d", min, max);
    return 0;
}