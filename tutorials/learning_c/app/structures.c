//structure is a collection of different datatype 
//structure is a user defined datatype
#include<stdio.h>
#include<string.h>

int main(){
    struct student{
        char *name;
        int roll;
        float cgpa;
    };

    struct student s1;
    struct student s2;
    struct student s3;
    s1.cgpa = 9.9;
    s1.name = "Arjun";
    s2.name = "Naveen";
    s3.name = "Sushmeetha";

    char *studetails[4] = {s1.name,s2.name,s3.name};

    //puts(studetails[0]);

    for(int i =0;i<=2;i++){
        puts(studetails[i]);
    }

    printf("%f\n",s1.cgpa);

}