# Implement  using Recursion method and plot the runtime for 100, 500, 1000, 1500, 2000, 2500, 3000 random integers.
import random
import sys
import time

# sys.setrecursionlimit has been used to increase the recursion limit becuase we have to call the funcion recursively til 3000 terms.
# default recursion limit is 997
sys.setrecursionlimit(3100)

def bubbleSortRecursive(arr, n):
    
        # Base case
        if n <= 1:
            return
 
        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
 
        # Largest element is fixed,
        #  recur for remaining array
        bubbleSortRecursive(arr, n - 1)

	
# defining function to print the elements of given array
def printArray(arr,n):
	for i in range(n):
		print(arr[i])

# defining function to generate random numbers of desired length and limit and storing them in list
def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res


# Driver program

# Taking the user input of the required values such as how many number are to be printed by number,
# starting number of random array by lower and last number of random array by upper.

number = int(input("Enter number of elements to sort: "))
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))



# calling the function to generate the random numbers in a user given range and storing them in a list-  randomlist.
randomlist = Rand(lower, upper, number)

n = len(randomlist)
# printing the unsorted array of random numbers
print("Unsorted Array:")
printArray(randomlist, n)
# method to get the starting time of the function. (using time library)
start = time.time()
bubbleSortRecursive(randomlist, n)
# printing the sorted array of random numbers
print("Sorted Array:")
printArray(randomlist, n)
# method to get the end time of the function. (using time library)
end = time.time()

# printing the time taken by the function (i.e. difference of end and starting time of the program) 
print(f"Runtime of the program is {end - start} seconds")

