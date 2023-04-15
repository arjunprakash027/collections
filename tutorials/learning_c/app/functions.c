#include<stdio.h>
//block of code that performs a particular task is function

int main(){
    int example(); //this line is called as functon prototyping
    example(); //calling function

}


int example(){ //function declaration
    printf("hello world\n");
    return 0;
}

/*

trivia
-> execution starts from main in c,cpp and java
-> A function can call another function inside it(directly or indirectly)
-> functions can only return 1 value 

types
-> library function are inbuilt functions in C declared by developers
-> user defined function are declared and used by users like you and me

passing arguements
-> functions can take in values called arguements
-> functions return values called as return values 

argument vs parameter
-> parameters are used using function declaration
-> arguments are passed to fucntion while using it


*/