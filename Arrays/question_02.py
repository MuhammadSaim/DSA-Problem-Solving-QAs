"""

Question #02: Find a 2nd largest number in an array

Given an array arr[] of integers. Find a 2nd largest element.

Example:

	Input: array[]= {2, 8, 9, 56}
	Output: 9
	Explanation: The element 9 is the 2nd largest in an array.

	Input: array[] = {10, 20, 15, 2, 23, 90, 67}
	Output: 67
	Explanation: The element 67 is the 2nd largest in an array.

"""


def find_the_second_largest(array: list, length: int) -> int:

	largest_elem: int = 0
	second_largest_elem: int = 0

	for i in range(length):

		if (array[i] > largest_elem):
			second_largest_elem = largest_elem
			largest_elem = array[i]
		elif (array[i] > second_largest_elem and array[i] != largest_elem):
			second_largest_elem = array[i]


	return second_largest_elem



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


value: int = find_the_second_largest(array, array_length)
print(f"2nd largest element in array is {value}")