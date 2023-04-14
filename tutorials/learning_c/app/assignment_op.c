#include<stdio.h>

int main(){
    int a,b,c;
    int check_div(int num);
    a = 1;
    b = 4;
    a+=b;
    printf("%d \n",a);

    printf("enter a number to check division by 2: ");
    scanf("%d",&c);
    printf("%d\n",check_div(c));
    return 0;
}

int check_div(int num){
    return num%2==0;
}