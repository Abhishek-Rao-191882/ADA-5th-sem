// write a program to implement the fibonacci series and plot the run time

#include<stdio.h>
#include<time.h>
// Fibonacci Function
void printFibonacci(int n){
    double i, first, second, next;
    // these are first two terms
    first=0;
    second=1;
    // for loop using to print the terms
    for(i=1; i<=n; i++)
    {
      printf(" %0.2lf",first);
      next=first+second;
      first=second;
      second=next;
    }
}

int main(){
    int n;
    // taking user input  for the number of terms
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    // declaring variable for time calculating function
    clock_t t;
    t = clock();
    // printing the fibonacci series by calling the above defined function
    printf("Fibonacci Series: ");
    printFibonacci(n);
    // function for time calculation of the given function
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("\n");
    printf("\n time taken by Fibonacci function = %f seconds \n", time_taken);
  return 0;
 }


