"""

Question #02: Find a 2nd smallest number in an array

Given an array arr[] of integers. Find a 2nd smallest element.

Example:

	Input: array[]= {2, 8, 9, 56}
	Output: 8
	Explanation: The element 8 is the 2nd smallest in an array.

	Input: array[] = {10, 20, 15, 2, 23, 90, 67}
	Output: 10
	Explanation: The element 10 is the 2nd smallest in an array.

"""
import sys



def find_the_second_smallest(array: list, length: int) -> int:

	smallest_elem: int = sys.maxsize
	second_smallest_elem: int = sys.maxsize

	for i in range(length):

		if (array[i] < smallest_elem):
			second_smallest_elem = smallest_elem
			smallest_elem = array[i]

		if (array[i] < second_smallest_elem and array[i] > smallest_elem):
			second_smallest_elem = array[i]


	return second_smallest_elem



# an empty list to store values in later
array: list = []

# get the input from the user
array_length: int = int(input("Enter the length of an array: "))


# run the loop to get the input in the list from the user
for i in range(array_length):
	array.append(
			int(
				input(f"Insert the value at {i} index: ")
			)
		)


value: int = find_the_second_smallest(array, array_length)
print(f"2nd smallest element in array is {value}")