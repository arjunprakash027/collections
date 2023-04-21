#include<stdio.h>

int main(){
    int total;
    FILE *fptr;
    fptr = fopen("students.txt","w");
    printf("total number of students:\n");scanf("%d",&total);
    //printf("%d",total);

    for(int i=1;i<=total;i++){
        char name[20];
        int age;
        char department[30];
        printf("enter details of student %d in the order \nname\nage\ndepartment\n",i);
        scanf("%s",&name);
        scanf("%d",&age);
        scanf("%s",&department);
        fptr = fopen("students.txt","a");

        fprintf(fptr,"%s\t%d\t%s\n",name,age,department);
    }
    fclose(fptr);
    return 0;
}