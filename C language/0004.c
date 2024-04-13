#include<stdio.h>
#include<ctype.h>
#include<string.h>

int main(){

    char word[10000];
    scanf("%s", &word);
    int length, count = 0;
    length = strlen(word);
    

    for(int i=0 ; i < length ; i++){
        if(isupper(word[i])){
            count++;
        }        
    }

    /*for(int i=0 ; i < length ; i++){
        if( word[i]>=65 && word[i]<=90){
            count++;
        }
    }*/

    //printf("%d %d", count, length);

    if(count==length){
        printf("All Capital Letter");
    }
    else if(count==0){
        printf("All Small Letter");
    }
    else{
        printf("Mix");
    }
    
        
    return 0;
}