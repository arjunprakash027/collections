#include<stdio.h>

typedef struct ArtificialIntelligenceAndDataScienceDepartment{
        int students;
        int staffs;
        int papers;
        int projects;
        int budget;
        char *hod;
    } aids;

void printinfo(aids s1){

    aids *ptr;
    ptr = &s1;
    printf("dept info\n");
    printf("students:%d\nstaffs:%d\npapers:%d\nprojects:%d\nbudget:%d\n",ptr->students,ptr->staffs,ptr->papers,ptr->projects,ptr->budget);
    puts(ptr->hod);
}

int main(){
    //typedef creates a alias for our datatype

    aids year1 = {66,5,1,10,50000,"KanagaSubaRaja"};
    printinfo(year1);

}