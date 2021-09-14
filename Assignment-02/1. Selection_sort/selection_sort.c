#include <stdio.h>
#include<time.h>
#include<stdlib.h>

//swapping function
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

//sorting function: Selection Sort
void *selectionSort(int arr[], int n)
{
    int i, j, min_element;
    for (i = 0; i < n-1; i++)
    {
        min_element = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_element])
            min_element = j;
        swap(&arr[min_element], &arr[i]);
    }
return arr;
}

// sorting algorithm implementation using Random numbers Generated in a user given range
int main(){
    // declaring variable
    int n, i, lower, upper;
    // taking user inputs
        printf("Enter no of elements to sort: \n");
        scanf("%d", &n);
        printf("Enter lower limit.\n");
        scanf("%d",&lower);
        printf("Enter upper limit.\n");
        scanf("%d",&upper);
   int input_array[n], *sorted_array;
        printf("unsorted array: \n ");
    //Random number generation
   srand(time(0));
   for(int i=0; i<n ; i++){
    input_array[i]= (rand() % (upper - lower + 1)) + lower;
    printf("%d \t", input_array[i]);
   }
   // declaring variable for calculating time taken by a function
   clock_t t;
    t = clock();
    //calling the sorting function
   sorted_array = selectionSort(input_array, n);
   //printing the sorted array
        printf("\n sorted array: \n ");
        for( int i = 0; i<n ; i++){
            printf("%d \t", sorted_array[i]);
   }
   // implementation of function for time taken calculation of a given function of Sorting Algorithm Function
   t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; //
    printf("\n");
    printf("\n time taken by Sorting Algorithm = %f seconds \n", time_taken);
return 0;
}
