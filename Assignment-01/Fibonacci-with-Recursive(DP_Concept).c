 #include<stdio.h>
 #include<time.h>
void printFibonacci(int n){
    static double n1=0,n2=1,n3;
    if(n>0){
         n3 = n1 + n2;
         n1 = n2;
         n2 = n3;
         printf("%lf ",n3);
         printFibonacci(n-1);
    }
}
int main(){

    int n;
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    clock_t t;
    t = clock();
    printf("Fibonacci Series: ");
    printf("%d %d ",0,1);
    printFibonacci(n-2);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; //
    printf("\n");
    printf("\n time taken by Fibonacci function = %f seconds \n", time_taken);
  return 0;
 }


