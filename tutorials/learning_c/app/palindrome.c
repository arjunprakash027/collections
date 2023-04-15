#include<stdio.h>

int main(){
    int num,rev=0,temp,rem;
    int n=0;
    printf("enter a number to check palindrome:");scanf("%d",&num);

    temp = num;
    while(temp!=0){
        rem = temp%10;
        rev = rev*10 + rem;
        temp /= 10;
    }
    printf("%d\n",rev);
    if(rev==num){
        printf("palindrome\n");
    } else {
        printf("Not a palindrome\n");
    }
}