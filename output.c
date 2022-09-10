// Enable Input and Output system
#include <stdio.h>

// Start main function
int main(){

// Code here:
int num1;
int num2;
int result;

printf("Enter a number: \n");
scanf("%i", &num1);

printf("Enter other name: \n");
scanf("%i", &num2);

result = num1 + num2;

printf("The result is: %i", result);

// End main function
return 0; }