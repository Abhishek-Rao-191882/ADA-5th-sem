// write a program to implement the fibonacci series and plot the run time

#include<stdio.h>

// fibonacci function
double fib(double n)
{
    // if value of n is 0 or 1 (i.e. less than or equal to 1) then if will return 0 or 1
if (n <=1 )
	return n;
	// if value of n is greater than 1 then it will return the summation of previous two terms
else
    return fib(n-1) + fib(n-2);
}

// driver code
int main ()
{
    // taking the value of n
    double n=5;

    // printing the fibonacci series using for loop starting from value of n from 0 to n
    printf("Fibonacci Series: ");
    for(int i=0; i<=n; i++){
        printf(" %0.2lf", fib(i));
    }

return 0;
}
