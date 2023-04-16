#include<stdio.h>
//A variable that stores memory address of another variable
int example();

int main(){
    int age = 2;
    int *ptr = &age; //*-> value at adress operator, &-> address of variable
    int _age = *ptr;
    printf("%d\n",_age);
    printf("%p\n",ptr);
    printf("%u\n",ptr);

    example();
    return 0;
    }

int example(){
    int x;
    int *ptr;

    ptr = &x;
    *ptr = 45;


    printf("%d\n",x);
    printf("%d\n",*ptr);

    *ptr  += 5;
    printf("%d\n",x);

    (*ptr)++;
    printf("%d\n",x);

    return 0;
}