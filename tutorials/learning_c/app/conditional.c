#include<stdio.h>

int main(){
    int age_func();
    int mark_func();
    int switch_ex();

    age_func();
    mark_func();
    switch_ex();
}

int age_func(){
    int age;
    printf("enter age:");scanf("%d",&age);
    age>=21 ? printf("you can drink\n") : printf("do not drink\n");
    return 0;
}

int mark_func(){
    int mark;
    printf("enter your marks:");scanf("%d",&mark);

    if(mark>79){
        printf("distinction\n");
    }
    else if(mark>=60 && mark<=79){
        printf("first class\n");
    }
    else if(mark>=35 && mark<=59){
        printf("Secound class\n");
    }
    else{
        printf("failed sorrry!!\n");
    }
    return 0;
}

int switch_ex(){
    char day;
    printf("enter your day:");scanf(" %c",&day);

    switch(day){
        case 'm' : printf("monday\n");break;
        case 't' : printf("tuesday\n");break;
        case 'w' : printf("wednesday\n");break;
        default:printf("only mon tue wed can be entered\n");
    }
    return 0;
}


