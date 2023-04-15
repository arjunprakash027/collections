#include<stdio.h>
#include<math.h>

int main(){
    int armstrong();
    int natural();

    armstrong();


}

int armstrong(int a){
    int num,temp,rem,n=0;
    float result=0.0;
    printf("enter the number:\n");scanf("%d",&num);

    temp = num;
    while(temp!=0){
        n++;
        temp /= 10;
    }

    temp = num;

    while(temp != 0){
        rem = temp%10;
        result += pow(rem,n);
        temp /= 10;
    }

    if((int)result == num){
        printf("the number is a armstrong number\n");
    } else {
        printf("the number is not a armstrong number\n");
    }

}