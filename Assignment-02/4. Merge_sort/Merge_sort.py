# Implement  using Recursion method and plot the runtime for 100, 500, 1000, 1500, 2000, 2500, 3000 random integers.
import random
import sys
import time

# sys.setrecursionlimit has been used to increase the recursion limit becuase we have to call the funcion recursively til 3000 terms.
# default recursion limit is 997
sys.setrecursionlimit(3100)

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

	
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
mergeSort(randomlist)
# printing the sorted array of random numbers
print("Sorted Array:")
printArray(randomlist, n)
# method to get the end time of the function. (using time library)
end = time.time()

# printing the time taken by the function (i.e. difference of end and starting time of the program) 
print(f"Runtime of the program is {end - start} seconds")

