#include<stdio.h>

int maxnum(int a,int b,int *max);
int arrayrev();
int allenglish();

int main(){
    allenglish();
    int a = 20,b=30,max;
    maxnum(a,b,&max);
    printf("max number is %d\n",max);

    arrayrev();

}

int allenglish(){
    char a = 'A';
    char *ptr = &a;

    while(*ptr <= 'z'){
        printf("%c",*ptr);
        (*ptr)++;
    }
    printf("\n");
    return 0;
}

int maxnum(int a, int b, int *max){
    if(a>b){
        *max = a;
    } else {
        *max = b;
    }
    return 0;
}

int arrayrev(){
    int ar[] = {5,2,3,4,5};
    int len = sizeof(ar)/sizeof(ar[0]);
    int *ptr;
    ptr = ar + (len-1);
    for(int i=0;i<len;i++){
        printf("%d\n",*(ptr-i));
    }
}