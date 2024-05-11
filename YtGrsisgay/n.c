#include <stdio.h>


int main(){
    
    int mt1[3][3], mt2[3][3], mt3[3][3];

    printf("input matrix 1 : ");

    for(int k = 0; k < 3; k++)
    {
        for(int l = 0; l < 3; l++)
        {
            scanf("%d", &mt1[k][l]);
        }
    }

    printf("input matrix 2 : ");
    for(int m = 0; m < 3; m++)
    {
        for(int n = 0; n < 3; n++)
        {
            scanf("%d", &mt2[m][n]);
        }
    }
     for(int x = 0; x < 3; x++)
    {
        for(int z = 0; z < 3; z++)
        {
            mt3[x][z] = mt1[x][z] + mt2[x][z];
        }
        
    }

    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            printf("%d ", mt3[i][j]);
        }
        printf("\n");
    }
    
    
    return 0;
}