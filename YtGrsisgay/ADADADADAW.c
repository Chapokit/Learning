#include <stdio.h>

typedef struct 
{
    char name[15];
    float gpa;

}Student;



int main(){

    Student student1 = {"Wadadad", 2.5};
    Student student2 = {"aaaaaaaaaaaaaaa", 3.0};
    Student student3 = {"naaaaa", 4.1};

    Student student[] = {student1, student2, student3};

    for (int i = 0; i < sizeof(student) / sizeof(student[0]); i++)
    {
        printf("%-12s\t", student[i].name);
        printf("%.2f\n", student[i].gpa);
    }
    
}