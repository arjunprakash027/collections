#include<stdio.h>

int mark();
int countodd(int *arr,int count,int len);
int main(){
    
    int count = 0;
    int arr[50];
    int len = sizeof(arr)/sizeof(arr[0]);
    printf("%d\n",len);
    countodd(arr,count,len);
}

int mark(){
    int marks[2][3];

    for(int i=0;i<3;i++){
        for(int j=0;j<4;j++){
            marks[i][j] = i+j;
        }
    }

    for(int i=0;i<3;i++){
        for(int j=0;j<4;j++){
            printf("%d\n",marks[i][j]);
        }
    }
    return 0;
}

int countodd(int *arr,int count,int len){
    
    for(int i=0;i<51;i++){
        *(arr+i) = i;
    }
    for(int i=0;i<len+1;i++){
        printf("%d\n",*(arr+i));
        if(*(arr+i) % 2 == 1){
            count++;
        }
    }
    printf("count=%d\n",count);
    return 0;
}

