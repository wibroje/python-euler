# 1.

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000.

# sum = 0
# for i in range(1, 1000):
# 	if i % 3 == 0 or i % 5 == 0:
# 		sum += i

# print(sum)

# The sum is 233168


# 2.

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# sum = 0
# a = 1
# b = 0
# while a < 4000000:
# 	a = b + a
# 	b = a - b
# 	if a % 2 == 0:
# 		sum = sum + a

# print(sum)

# The sum is 4613732


# 3.

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


# 4. 

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# 5. 

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


	










