#include<stdio.h>
double fib(double n)
{
if (n <=1 )
	return n;
else
    return fib(n-1) + fib(n-2);
}

int main ()
{
double n = 50;
printf("%lf", fib(n));
return 0;
}
