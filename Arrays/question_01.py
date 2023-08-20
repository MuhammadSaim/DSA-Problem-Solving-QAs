"""

Problem Link: https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

Question #01: Find a peak element which is not smaller than its neighbours

Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors.

Note: For corner elements, we need to consider only one neighbor.

Example:

	Input: array[]= {5, 10, 20, 15}
	Output: 20
	Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

	Input: array[] = {10, 20, 15, 2, 23, 90, 67}
	Output: 20 or 90
	Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

"""


def find_peak_element(array: list, length:int) -> int:
	
	# check for the first and the last elements
	if length == 1:
		return 0

	if array[0] >= array[1]:
		return 0

	if array[length - 1] >= array[length - 2]:
		return length - 1

	# check for the other elements
	for i in range(length):
		if array[i] >= array[i - 1] and array[i] >= array[i + 1]:
			return i




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


index: int = find_peak_element(array, array_length)
print(f"Index of the peak point is {index} => {array[index]}")
