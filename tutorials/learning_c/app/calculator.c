#include <stdio.h>

int add(int a, int b);
int sub(int a, int b);
int multiply(int a, int b);
float divide(float a, float b);

int main(){
    int a,b;
    printf("enter number 1:");
    scanf("%d",&a);
    printf("enter value of 2:");
    scanf("%d",&b);
    printf("add:%d , sub:%d , multiply:%d , div:%f \n",add(a,b),sub(a,b),multiply(a,b),divide(a,b));
    return 0;
}

int add(int a,int b){
    int c;
    c = a+b;
    return c;
}

int sub(int a, int b){
    int c;
    if (a>b){
        c = a-b;
    } else {
        c = b-a;
    }
    
    return c;
}

int multiply(int a, int b){
    int c;
    c = a*b;
    return c;
}

float divide(float a, float b){
    float c;
    c = a/b;
    return c;
}