#include<stdio.h>
#include<string.h>

char salt(char pass[]);

int main(){
    char pass[100];
    scanf("%s",pass);
    //fgets(pass,20,stdin);
    salt(pass);
}

char salt(char pass[]){
    char salt[20] = "3456";
    char newpass[100];

    strcpy(newpass,pass);
    strcat(newpass,salt);

    puts(newpass);
}