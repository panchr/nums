# nums.sequences.py
# written by Rushy Panchal
# Version 1.0

'''Provides sequence generation

'nums.sequences.py' contains various functions of sequences and patterns found in mathematics and everyday life.
	
OVERVIEW:
	'nums.sequences.py' is a module in the 'nums' package that has sequences such as Triangle Numbers, primes, the Fibonacci Sequence, and the Collatz Sequence.
	Example of the module's capabilities (run nums.sequences.example() to see this example):

	-------------------------------------------------------
	from nums.sequences import *
	print('isPrime(9013) --> ', isPrime(9013))
	print('Primes up to 9013: ', prevPrimes(9013))
	print('Primes from 1000 to 9013: ', primeRange(1000, 9013))
	print('Triangle Numbers up to 9013: ', prevTriNums(9013))
	print('100th Fibonacci Number: ', fib(100))
	-------------------------------------------------------
'''

### Change Log:

	# v1.0: Initial release, after separation from 'nums.py' and inclusion in the 'nums' package

from __future__ import division
from nums.errors import *
import collections

### Main functions

def prevTriNums(n):
	"""Returns all of the triangle numbers up to 'n'
	>>> prevTriNums(25)
	[1, 3, 6, 10, 15, 21]"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	num, tri_numbers, x = 0, [], 0
	while num <= n:
		x += 1
		num += x
		if num > n: break
		tri_numbers.append(num)
	return tri_numbers

def triNum(n):
	"""Returns the 'n'th triangle number
	>>> triNum(25)
	325.0"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	return (n**2 + n) / 2
	
def isPrime(n):
	"""Checks if 'n' is prime
	>>> isPrime(967)
	True"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	x = 2
	if n == 0 or n == 1:
		return False
	for check in xrange(2, int(n**0.5+1)):
		if n % check == 0: return False
	return True

def primeRange(a, b = None):
	"""Generates primes from 'a' to 'b':
	>>> primeRange(5, 10)
	[5, 7]
	>>> primeRange(10)
	[2, 3, 4, 5, 7]"""
	primes = generate_primes(a) if b is None else prime_range(a, b)
	return [p for p in sorted(primes) if primes[p]]
	
def prevPrimes(n):
	"""Generates primes up to n:
	>>> prevPrimes(10)
	[2, 3, 4, 5, 7]"""
	primes = generate_primes(n)
	return [p for p in sorted(primes) if primes[p]]
	
def prime_range(a, b):
	'''Returns a dictionary of numbers on whether or not the nubmers are prime:
	>>> prime_range(5, 10)
	{5: True, 6: False, 7: True, 8: False, 9: False, 10: False}
	>>> prime_range(10)
	{2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False}'''
	if not isinstance(a, types): raise NumericalError(type_(getError('int')))
	if not isinstance(b, types): raise NumericalError(type_(getError('int')))
	if a < 2: raise NumericalError(value_("a must be greater than 2"))
	if a%2 == 0: a += 1
	primes = sorted(primeRange(int(b**0.5) + 1) + range(a, b + 1, 2))
	primes_dict = collections.OrderedDict({i : True for i in primes})
	for i in primes_dict:
		if primes_dict[i]:
			num = i
		while num * i <= b:
			primes_dict[num*i] = False
			num += 2
	if a <= 2: primes_dict[2] = True
	return {i: primes_dict[i] for i in primes_dict if (a <= i <= b)}
	
def generate_primes(n):
	"""Returns a dictionary of numbers on whether or not the numbers are prime:
	>>> generate_primes(10)
	{2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False}"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	if n < 2: raise NumericalError(value_("n must greater than 2"))
	primes_dict = collections.OrderedDict({i : True for i in xrange(3, n + 1, 2)})
	for i in primes_dict:
		if primes_dict[i]:
			num = i
		while num * i <= n:
			primes_dict[num*i] = False
			num += 2
	primes_dict[2] = True
	return primes_dict
	
def prime(n):
	"""Returns the 'n'th prime number
	>>> prime(25)
	97"""
	return max(n_primes(n))
	
def n_primes(n):
	'''Returns 'n' amount of primes'''
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	if n < 1: raise NumericalError(value_('n must be greater than 1'))
	primes, num = [2], 3
	while len(primes) <= n:
		if isPrime(num): primes.append(num)
		num += 2
		if len(primes) == n: break
	return primes
	
def fib(n):
	"""Returns the 'n'th number in the Fibonacci sequence
	>>> fib(25)
	46368"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	nums = [0, 1, 1]
	if n > 2:
		for index in xrange(3, n): 
			nums.append(nums[index-1] + nums[index-2])
	return nums[n-1]

def prevFibs(n):
	"""Returns the previous Fibonacci numbers up to 'n'
	>>> prevFibs(1000)
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	a, b, nums = 0, 1, [0, 1]
	while b <= n:
		a, b = b, a+b
		if b >= n: break
		nums.append(b)
	return nums
	
def isCollatz(n):
	"""Checks whether or not a number's Collatz sequence ends in 1
	>>> isCollatz(25)
	True"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	return collatz(n)[-1] == 1
	
def collatz(n):
	"""Returns the Collatz sequence; breaks if there are more than 5000 elements
	>>> collatz(25)
	[25, 76, 38.0, 19.0, 58.0, 29.0, 88.0, 44.0, 22.0, 11.0, 34.0, 17.0, 52.0, 26.0, 13.0, 40.0, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	iterCount, nums = 0, [n]
	while n != 1 and iterCount <= 5000:
		if n%2 == 0:
			n /= 2
			nums.append(n)
		else:
			n = (3 * n) + 1
			nums.append(n)
		iterCount += 1
	return nums
	
def decRange(start = 0, stop = 11, step = 1):
	"""Generates numbers from start [,stop, step]
	>>> decRange(start = 0, stop = 10, step = 1)
	[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
	>>> decRange(stop = 1, step = 0.1)
	[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]"""
	for elem in (start, stop, step):
		if not isinstance(elem, types): raise NumericalError(type_(getError('float')))
	results, roundN = [], len(str(step)) - 2
	if roundN < 0: roundN = 0
	start -= step
	while start <= stop:
		start += step
		yield round(start, roundN)
		
### Example to show the module's capabilities

def example():
	print('isPrime(9013) --> ', isPrime(9013))
	print('Primes up to 9013: ', prevPrimes(9013))
	print('Primes from 1000 to 9013: ', primeRange(1000, 9013))
	print('Triangle Numbers up to 9013: ', prevTriNums(9013))
	print('100th Fibonacci Number: ', fib(100))