#include<stdio.h>
//initialize the vector
typedef struct vector {
    int x;
    int y;
}vec; 

typedef struct complex{
    int real;
    int img;
}clx;


void sum(vec v1,vec v2,vec sum){
    vec *ptr1,*ptr2,*ptr3;
    ptr1 = &v1;
    ptr2 = &v2;
    ptr3 = &sum;

    ptr3->x = ptr1->x + ptr2->x;
    ptr3->y = ptr1->y + ptr2->y;

    printf("sum is : %di + %dj\n",ptr3->x,ptr3->y);

}

void complexnumbers(clx c1){
    clx *ptr;
    ptr = &c1;

    printf("the complex number is : %d + %di\n",ptr->real,ptr->img);
}
int main(){
    vec v1 = {3,4};
    vec v2 = {6,3};
    vec sums = {0}; //initialize the value of vectors to 0
    sum(v1,v2,sums);

    //storing and displaying complex number
    clx c1 = {20,30};
    complexnumbers(c1);
    return 0;
}