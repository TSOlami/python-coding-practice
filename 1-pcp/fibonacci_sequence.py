#!/usr/bin/python3
""" Script that calculates the Fibonacci sequence up to the nth term. """

        
def fibonacci_sequence(n: int) -> int:
	""" Function that calculates the Fibonacci sequence up to the nth term. """
	
	# Initiate a dictionary to store the Fibonacci sequence
	fib_dict = {0: 0, 1: 1}

	# Loop through the numbers up to the nth term
	for i in range(2, n + 1):

		# Calculate the Fibonacci number
		fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

	# Return the nth term
	return(fib_dict[n])
