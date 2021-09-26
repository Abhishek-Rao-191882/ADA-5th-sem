# Implement  using Recursion method and plot the runtime for 100, 500, 1000, 1500, 2000, 2500, 3000 random integers.
import random
import sys
import time

sys.setrecursionlimit(3100)

def insertionSort(arr,n):
	# base case
	if n<=1:
		return
	
	# Sort first n-1 elements
	insertionSort(arr,n-1)
	# Insert last element at its correct position in sorted array.
	last = arr[n-1]
	j = n-2
	
	# Move elements of arr[0..i-1], that are
	# greater than key, to one position ahead
	# of their current position
	while (j>=0 and arr[j]>last):
		arr[j+1] = arr[j]
		j = j-1

	arr[j+1]=last
	
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
insertionSort(randomlist, n)
# printing the sorted array of random numbers
print("Sorted Array:")
printArray(randomlist, n)
# method to get the end time of the function. (using time library)
end = time.time()

# printing the time taken by the function (i.e. difference of end and starting time of the program) 
print(f"Runtime of the program is {end - start} seconds")

