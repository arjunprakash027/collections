#include<stdio.h>

int main(){
    FILE *fptr;
    fptr = fopen("sum.txt","r");
    if(fptr == NULL){
        fptr = fopen("sum.txt","w");
        fclose(fptr);
        fptr = fopen("sum.txt","r");
    }

    int sum=0;

    for(int i=0;i<=2;i++){
        int n;
        fscanf(fptr,"%d",&n);
        sum = sum+n;
    }
    fclose(fptr);
    fptr = fopen("sum.txt","w");

    fprintf(fptr,"%d",sum);
    fclose(fptr);


}