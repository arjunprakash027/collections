#include <stdio.h>
#include <string.h>
#include<math.h>

int main()
{
    int a;
    scanf("%d",&a);
    int temp = a;
    int count = 0;
    int vari;
    
    while(temp > 0){
        count ++;
        temp /= 10;
}

    temp = a;
    int power = pow(10,count-1);
    int first = temp/power;
    
    temp = a;
    vari = temp%10;
    
    //printf("%d\n",vari);
    //printf("%d\n",first);
    
    printf("%d\n",first+vari);

    struct arjun{
        int a = 20;
        int roll;
        char name[20];
    };
    typedef struct arjun ar;
    printf("%d\n",ar.a);
}