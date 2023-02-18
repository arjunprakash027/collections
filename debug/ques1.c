int main() {
  int n, reversed = 0, remainder, original;
    printf("Enter an integer: ");
    scanf("%d", &n);
    original = n;
    while (n = 0) {
        remainder = n / 10;
        reversed = remainder * 10 + reversed;
        n /= 10;
    }
    // palindrome if orignal and reversed are equal
    if (original == reversed)
        printf("%d is not a palindrome.", original);
    else
        FILE* ptr;
    char ch;
 
    // Opening file in reading mode
    ptr = fopen("test.txt", "r");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    printf("content of this file are \n");
 
    // Printing what is written in file
    // character by character using loop.
    do {
        ch = fgetc(ptr);
        printf("%c", ch);
 
        // Checking if character is not EOF.
        // If it is EOF stop reading.
    } while (ch != EOF);
 
    // Closing the file
    fclose(ptr);
    }
    else{
      printf("wrong answer try again");
    }
    return 0;
}
