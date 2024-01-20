#!/usr/bin/python3
""" Script to find the two numbers in a list that add up to a target number. """


def two_sums(self, nums: List[int], target: int) -> List[int]:
	""" Function to find the two numbers in a list that add up to a target number. """
	
	# Initiate a dictionary to store the numbers
	num_dic = {}
	# Loop through the list of numbers
	for i, num in enumerate(nums):
		# Find the complement of the current number
		complement = target - num
		# Check if the complement is in the dictionary
		if complement in num_dic:
			# Return the indices of the two numbers
			return ([i, num_dic[complement]])
		# Add the current number to the dictionary
		elif num not in num_dic:
			num_dic[num] = i
	# Return an empty list if no two numbers add up to the target
    return([])
		
        
        

        
            