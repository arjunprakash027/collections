#include<stdio.h>

int main(){
    char ch;
    printf("enter a ch:");scanf("%c",&ch);

    if(ch>='A' && ch<='Z'){
        printf("upper case\n");
    } else if(ch>='a' && ch<='z'){
        printf("lower case\n");
    } else {
        printf("enter a english character\n");
    }
}