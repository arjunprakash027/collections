#include<stdio.h>

int main(){
    struct student{
        int roll;
        float cgpa;
        char *name;
    };

    //trying array of structures
    struct student ainds[100];
    ainds[0].roll = 310620243001;
    ainds[0].cgpa = 8.6;
    ainds[0].name = "Aaqil";

    ainds[1].roll = 310620243002;
    ainds[1].cgpa = 8.9;
    ainds[1].name = "Adarsh";

//trying with single line assignment
    struct student s2 = {310620243005,8.5,"arjun"};

//tryinf pointers of structures
    struct student s3;
    struct student *ptr3;
    ptr3 = &s2;

    puts(ainds[1].name);
    puts((*ptr3).name);

    //arrow operator
    puts(ptr3->name);
    printf("%f\n",ptr3->cgpa);
    return 0;

}