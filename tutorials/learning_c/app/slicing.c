#include<stdio.h>

void slice(char string[],int start,int end);
int main(){
    char string[100] = "I AM ARJUN";
    slice(string,2,7);
}

void slice(char string[],int start,int end){
    char new[100];
    int j = 0;
    for(int i=start;i<=end;i++,j++){
        new[j] = string[i];
    }
    new[j] = '\0';
    puts(new);
}