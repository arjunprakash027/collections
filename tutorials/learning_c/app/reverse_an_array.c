#include<stdio.h>

int swap();
int fib();
int main(){
    //swap();
    fib();
}

int swap(){
    int arr[] = {1,2,3,4,5,8,7,6,5,3};

    int len = sizeof(arr)/sizeof(arr[0]);

    for(int i=0,j=len-1;i<=(len-1)/2,j>=len/2;i++,j--){
        int first = arr[i];
        int last = arr[j];
        printf("f%d\n",first);
        printf("l%d\n",last);
        arr[i] = last;
        arr[j] = first;
    }

    for(int i=0;i<=len-1;i++){
        printf("%d\n",arr[i]);
    }
}

int fib(){
    int fib[50];
    fib[0] = 0;
    fib[1] = 1;

    printf("%d\t%d\t",fib[0],fib[1]);
    for(int i = 2;i<50;i++){
        fib[i] = fib[i-1] +fib[i-2];
        printf("%d\t",fib[i]);
    }
    printf("\n");
}