#include <iostream>

void sortArray(int array[], int size);

int main(){

    
    int arrays[] = {8, 3, 5, 1, 4, 9, 7, 2, 10, 6};
    int size = sizeof(arrays) / sizeof(arrays[0]);
    
    

    for (int i : arrays)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    sortArray(arrays, size);
    
    for (int i : arrays)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    
}

void sortArray(int array[], int size)
{
    int temp = 0;
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
             
        }

    }
}