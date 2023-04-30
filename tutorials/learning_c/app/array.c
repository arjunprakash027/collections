//array is collection of similar datatype stored in contigeous memory location

#include<stdio.h>

int arrayin();

int main(){
    int m1 = 20;
    int m2 = 30;
    int m3 = 40;

    int marks[] = {m1,m2,m3};
    int len = sizeof(marks)/sizeof(marks[0]);

    for(int i=0;i<len;i++){
        printf("%d\n",marks[i]);
    }

    arrayin();
   return 0;
}

int arrayin(){
    int mar[5];

    for(int i=0;i<5;i++){
        scanf("%d",&mar[i]);
    }

    int leng = sizeof(mar)/sizeof(mar[0]);
    for(int i=0;i<leng;i++){
        printf("%d\n",mar[i]);
    }

}