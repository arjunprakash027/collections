#include<stdio.h>
#include<string.h>

#define ASCII_SIZE 256

char macoccur(char *str){
    int count[ASCII_SIZE] = {0};
    int max = -1;
    char element;

    for(int i=0;str[i]!='\0';i++){
        count[str[i]]++;
    }

    for(int i=0;i<ASCII_SIZE;i++){
        if(max<count[i]){
            max = count[i];
            element = i;
        }
    }

    return element;

}

int main(){
    char str[100] = "arjunraok poor";
    printf("%c\n",macoccur(str));
}