#include<stdio.h>
//when a function calls itself its called recursion
int recur(int count);
int fact(int num);
int firstn(int num);
int CtoF(float temp);
int fibbonacci(int num);
int sumdigits(int num);

int main(){
    recur(20);
    printf("%d\n",fact(5));
    printf("%d\n",firstn(5));
    CtoF(35.00);
    printf("%d\n",fibbonacci(6));
    sumdigits(12345);
    return 0;
} 

int recur(int count){
    if (count == 0){
        return 0;
    }
    printf("number : %d\n",count);
    recur(count-1);
}

int fact(int num){
    if(num == 1){
        return 1;
    }
    int prevfact = fact(num-1);
    int val = prevfact*num;
    return val;

}

int firstn(int num){
    if (num == 1){
        return 1;
    }
    int prevsum = firstn(num - 1);
    int sum = prevsum + num;
    return sum;

}

int CtoF(float temp){
    printf("%f\n",temp*(9.0/5.0)+32);
    return 0;
}

int fibbonacci(int num){
    if (num == 0 || num==1){
        if(num==0){
            return 0;
        }
        if(num==1){
            return 1;
        }
    }
    int sum = fibbonacci(num-1) + fibbonacci(num-2);
    //printf("%d\n",sum);
    return sum;

}

int sumdigits(int num){
    int temp,res = 0,dig;
    temp = num;
    while(temp > 0){
        dig = temp%10;
        res = res+dig;
        temp /= 10;
    }
    printf("%d\n",res);
    return 0;
}
/*
Trivia 
-> everything that can be done using recursion can be done using iteration and vice versa
-> can sometimes give the most simple solution
->base case stops recursion
->Iteration has infinite loop while recursion has stack overflow
*/