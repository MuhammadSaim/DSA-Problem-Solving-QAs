"""

Problem Link: https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

Question #05: Count number of occurrences (or frequency) in an array

Given an array arr[] of integers.

Example:

	Input: array[]= {2, 8, 2, 56} => x = 2
	Output: 2

	Input: array[] = {10, 20, 15, 10, 23, 10, 67} => x = 10
	Output: 3

"""


def count_occurrences_of_integer(array: list, number: int):
	count: int = 0

	for val in array:

		if val == number:
			count += 1

	return count



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


# input the number to check the occurrence
value: int = int(input("Enter a number to find occurrence in array: "))


# get the occurence
occurrence: int = count_occurrences_of_integer(array, value)

if occurrence == 0:
	print("No occurrence found in the array")
else:
	print(f"{value} is found {occurrence} time in an array")