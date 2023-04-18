#include<stdio.h>

int arrpnt(int *arr,int n);
int main(){
    int arr[] = {1,4,7,5,6,7,8,9,0};
    int n = sizeof(arr)/sizeof(arr[0]);
    arrpnt(arr,n);
}

int arrpnt(int *arr,int n){

    for(int i=0;i<n;i++){
        printf("%d\t",*(arr+i));
    }
    printf("\n");
}