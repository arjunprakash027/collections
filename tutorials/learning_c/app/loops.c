#include<stdio.h>

int main(){
    int n;
    int print1to6();
    for(int i = 1;i<=500;i+=1){
        if(i==50){
            break;
        }
        printf("%d\n",i);
    }

    for(int i=0;i<=10;i++){
        n++;
    }

    for(float i=0.0;i<=10.7;i+=0.5){
        printf("%f\n",i);
    }

    for(int i = 40;i<=120;i++){
        printf("%c\n",(char)i);
    }
    printf("%d\n",n);

    // for(; ;){
    //     printf("what");
    // }
    n = 10;
    int sum = 0;
    do{
        printf("%d\n",n);
        n++;
    } while(n<=100);

    printf("vaue of n is %d\n",n);

    for(n;n<=500;n++){
        sum+=n;
    }

    printf("sum:%d\n",sum);
    print1to6();
}

int print1to6(){
    for(int i=1;i<=10;i++){
        if(i==6){
            continue;
        }
        printf("%d\n",i);
    }
}