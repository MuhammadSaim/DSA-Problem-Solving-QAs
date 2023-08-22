"""

Problem Link: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

Question #04: reverse an array

Given an array arr[] of integers. reverse the array.

Example:

	Input: array[]= {2, 8, 9, 56}
	Output: {56, 9, 8, 2}

	Input: array[] = {10, 20, 15, 2, 23, 90, 67}
	Output: {67, 90, 23, 2, 15, 20, 10}

"""

# function to reverse an array from start to end
def reverse_list(array: list, start: int, end: int) -> None:

	while start < end:
		array[start], array[end] = array[end], array[start]

		start += 1
		end -= 1



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


print(f"Array before reverse: {array}\n\n")
reverse_list(array, 0, array_length - 1)
print(f"Array after reverse: {array}")