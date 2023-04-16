#include<stdio.h>

//pointer to pointer stores the address of a pointer
//**pptr is pointer to pointer 
int main_ex();

int main(){
    main_ex();

}

int main_ex(){
    int price = 200;
    int *ptr = &price;
    int **pptr = &ptr;

    printf("%d %d %d \n",price,ptr,**pptr);
}