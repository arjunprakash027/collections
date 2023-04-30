// programs variables stay in ram
//  contents are lost when program terminates
//files are used to persists this data

//types of files -> text,binary(mp3,jpg etc)
// FILE pointer is a hidden structure that is used to open a file
// a ptr is used to traverse this file

#include<stdio.h>

int main(){
    FILE *fptr; //initialization of filepointer
    fptr = fopen("test.txt","r"); // accessing  a file names test.txt and in mode r
    if(fptr==NULL){
        printf("Does not exist this file\n");
    } else {
        char ch;
        //fscanf(fptr,"%c",&ch);
        ch = fgetc(fptr);
        while(ch!=EOF){
            printf("%c",ch);
            ch = fgetc(fptr);
        }
        printf("\n");
        
        //fgetc(fptr);
        fclose(fptr);
    } //close the file 
    FILE *fptrw;
    fptrw = fopen("tet.txt","w");
    fprintf(fptrw,"%c",'A');
    fprintf(fptrw,"%c",'R');
    fprintf(fptrw,"%c",'j');

    return 0;
}