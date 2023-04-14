#include<stdio.h>
#include<math.h>

int main(){
    int a,y,z;
    int power;
    int c,d=30;
    a=y=z=2;
    power = pow(d,2);
    int modulo1 = 5%2;
    int modulo2 = 4%8;
    int modulo3 = -8%3;
    int size1 = sizeof(4);
    int size2 = sizeof(4.67576584368456);
    int size3 = sizeof('c');
    int conv = (int) 1.9999999;

    printf("%d %d %d %d %d %d %d %d %d %d %d %d %d\n",a,y,z,c,d,power,modulo1,modulo2,modulo3,size1,size2,size3,conv);
    return 0;
}