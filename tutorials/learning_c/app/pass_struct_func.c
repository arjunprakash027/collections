#include<stdio.h>

struct company{
    int capital;
    int employees;
    char *location;
    char *name;
};
//using struct in function
void printinfo(struct company s1){

    struct company *ptr;
    ptr = &s1;
    printf("company info\n");
    printf("capital:%d\nEmployees:%d\n",ptr->capital,ptr->employees);
    puts(ptr->location);
    puts(ptr->name);


}

int main(){
    struct company s1 = {250000,50,"Chennai","SarasuComputers"};
    printinfo(s1);
}