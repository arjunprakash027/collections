#include<stdio.h>
// in call by value, the value is passed as arguement and not the variable. So the variable remains unaffected.
//we can pass the entire variable as argument and change its value using call by reference method.

int ref_fun(int *n);
int swap(int *a,int *b);

int main(){
    int number = 20;
    int a = 30;
    int b = 40;
    ref_fun(&number);
    printf("%d\n",number);

    printf("before swap a=%d,b=%d\n",a,b);
    swap(&a,&b);
    printf("after swap a=%d,b=%d\n",a,b);
    return 0;
}

int ref_fun(int *n){ //this is an example of call by reference
    printf("%p\n",n);
    *n = (*n) * (*n);
    printf("%d\n",*n);
    return 0;
}

int swap(int *a, int *b){ 
    int c;
    c = *a;
    *a = *b;
    *b = c;
}