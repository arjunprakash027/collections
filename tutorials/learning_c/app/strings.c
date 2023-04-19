#include<stdio.h>
#include<string.h>
// a character terminated by \0-> null character
void printstr(char arr[]);
void println(char arr[]);
void myownfgets();
int main(){
    char name2[] = {'a','r','j','u','n','\0'};
    char nam[] = "arjun";
    char nam2[] = "arjun";

    char *firstname = "hehe this can easily change";
    char name[50];
    //scanf("%s",firstname);
    fgets(name,100,stdin);
    println(name);
    printf("%d\n",strlen(name));
    puts(firstname);

    puts(strcat(nam,name2));
    printf("%d\n",strcmp(nam,nam2));

    myownfgets();
    //printstr(firstname);
    return 0;
}

void printstr(char arr[]){
    //printf("%c\n",arr[1]);
    char *ptr = arr;
    for(int i=0;*(ptr+i)!='\0';i++){
        printf("%c\n",*(ptr+i));
    }

    printf("your string is %s\n",arr);
}

void println(char arr[]){
    int count = 0;
    for(int i=0;arr[i]!='\0';i++){
        if(arr[i]=='\0'){
            count--;
        }else{
            count++;
        }
    }
    printf("length is %d\n",count);
}

void myownfgets(){
    char str[100];
    char ch;
    int i=0;

    while(ch!='\n'){
        scanf("%c",&ch);
        str[i] = ch;
        i++;
    }
    str[i] = '\0';

    puts(str);
}