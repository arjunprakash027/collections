#include<stdio.h>

int comparisn();
int travel();

int main(){
    int age = 20;
    int *ptr = &age;
    printf("%u\n",ptr);
    ptr++; // it increses the datatype size but not move to next element
    printf("%u\n",ptr);

    comparisn();
    travel();
}

int comparisn(){
    int age1 = 20;
    int age2 = 30;

    int *ptr1 = &age1;
    int *ptr2 = &age2;

    printf("%u\n",ptr1-ptr2);

}

int travel(){
    int ar[5];
    int *ptr = ar;

    for(int i=0;i<6;i++){
        scanf("%d",(ptr+i));
    }

    for(int i=0;i<6;i++){
        printf("%d\n",*(ptr+i));
    }
    return 0;
}