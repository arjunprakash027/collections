#include <stdio.h>

int square(float side);
float circle(float radius);
int main(){
    float side;
    float radius;
    printf("enter the side:");
    scanf("%f",&side);
    printf("enter the radius:");
    scanf("%f",&radius);
    printf("area of square is %d \n",square(side));
    printf("area of circle is %f\n",circle(radius));
    return 0;
}

int square(float side){
    float area;
    area = side*side;
    return area;
}

float circle(float radius){
    float area;
    area = 3.14*radius*radius;
    return area;
}
