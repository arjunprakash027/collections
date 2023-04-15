#include<stdio.h>

int main(){
    int a,b,c;
    char d = '5';
    int avga(int a,int b,int c);
    int isdig(char a);
    int psmal(int a, int b);
    printf("enter 3 numbers for avg and comparisn");
    scanf("%d%d%d",&a,&b,&c);
    printf("avg is %d and smallest number among a and b is %d \n",avga(a,b,c),psmal(a,b));
    printf("the char is a digit 1or 0:%d\n",isdig(d));
}

int avga(int a,int b,int c){
    int d = (a+b+c)/3;
    return d;
}

int isdig(char a){
    return (a>='0' && a<='9');
}

int psmal(int a, int b){
    return ((a<b) ? a:b);
}