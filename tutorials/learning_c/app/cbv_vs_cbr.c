#include<stdio.h>

int callbyvalue(int n);
int callbyref(int *n);

int main(){
    int num1 = 20;
    printf("adress value of num is %u\n",&num1);
    callbyvalue(num1);
    callbyref(&num1);
}

int callbyvalue(int n){
    printf("adress value of num from cbv is %u\n",&n);
    return 0;
}

int callbyref(int *n){
    printf("adress value of num by cbr is %u\n",n);
    return 0;
}