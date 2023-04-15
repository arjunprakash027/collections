#include<stdio.h>

int main(){
    int fact(int a);
    int a;

    printf("enter a number to find factorial:");scanf("%d",&a);
    fact(a);
}

int fact(int a){
    int result=1;

    for(int i = 1; i<=a ; i++){
        result = result*i;
    }
    printf("factorial of %d is %d\n",a,result);
    return 0;
}