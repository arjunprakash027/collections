#include<stdio.h>

int main(){
    FILE *fptr;
    fptr = fopen("tet.txt","r");
    char buffer[100];
    int n;

    if(fptr == NULL){
        return 1;
    } else {
        char ch;
        ch = fgetc(fptr);
        while(ch != EOF){
            printf("%c",ch);
            ch = fgetc(fptr);
        }
        printf("\n");
        fclose(fptr);
    }
    return 0;

}