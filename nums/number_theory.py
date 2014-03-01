# nums.number_theory.py
# written by Rushy Panchal
# Version 1.22

'''Simple number-manipulation and number-theory library

'nums.number_theory.py' contains various functions and classes of functions found in mathematics (of various levels). 
These functions can be applied in number-theory and complex calculations.
	
OVERVIEW:
	'nums.number_theory.py' has numerous functions and classes that can be used in number-theory applications and sequence-generation. It is a part of the 'nums' package.
	There are functions from checking if a given number is prime and generating all the primes up to a given number to finding the integral of a given function.
	Example (run nums.number_theory.example() to see this example):

	-------------------------------------------------------
	from nums.number_theory import *
	n = 9013
	f = 'x**2'

	print('Integral of x^2:', integral(f))
	print('Is n prime:', isPrime(n))
	print('Number of primes upto 9013',  len(primeRange(n)))
	-------------------------------------------------------
'''

### Change Log:

	# v1.0: Initial release, with primitive functions
	# v1.1: Fraction + NumericalError classes, and improved, more efficient functions
		# v1.11: Allow the usage of '+' and '-' operators
	# v1.2: 'nums.py' becomes 'number_theory.py' and a 'nums' package is created
		# v1.21 'Fraction' and 'NumericalError' class become separate files
		# v1.22 Added examples for each function
		
from __future__ import division
import decimal
import types
import math
import re

from nums.sequences import *
from nums.bases import *
from nums.errors import *
	
__version__ = 1.22
__author__ = "Rushy Panchal"
	
### Constants

pi = decimal.Decimal(math.pi)
tau = pi * 2
e = decimal.Decimal(math.e)

### Main functions
	
def factors(n):
	"""Returns all the factors of 'n'
	>>> factors(25)
	[5, 25]
	>>> factors(144)
	[1, 2, 3, 4, 6, 8, 9, 12, 24, 72, 144]"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	fList, num, limit = [], n, int(n**0.5) + 1
	for factor in xrange(1, limit):
		if n % factor == 0:
			fList.append(int(factor))
			num /= factor
			fList.append(int(num))
	fList = sorted(list(set(fList)))
	try: 
		if fList[0] == 1 or fList[0] == 0: del fList[0]
	except IndexError: fList = [1]
	return fList
	
def pFactors(n):
	"""Returns the prime factors of 'n'
	>>> pFactors(25)
	[5, 5]
	>>> pFactors(144)
	[2, 2, 2, 2, 3, 3]"""
	if not isinstance(n, types): raise NumericalError(type_(getError('int')))
	if n < 1: raise NumericalError(value_('must be greater than 1'))
	pFact, limit, check, num = [], int(n**0.5) + 1, 2, n
	if isPrime(n): return [n]
	for check in xrange(2, limit):
		if isPrime(check) and  num % check == 0:
			pFact.append(int(check))
			num /= check
		if isPrime(num):
			pFact.append(int(num))
			break
		while num % check == 0:
			pFact.append(int(check))
			num /= check
	return sorted(pFact)
 
def commonFactors(a, b):
	'''Returns the common factors of a and b
	>>> commonFactors(25, 144)
	[1]'''
	for elem in (a, b):
		if not isinstance(elem, types): raise NumericalError(type_(getError('num')))
	aFactors, bFactors, common_factors = factors(a), factors(b), []
	for factor in aFactors:
		if factor in bFactors: common_factors.append(factor)
	return common_factors if not common_factors == [] else [1]
	
def gcf(a, b):
	"""Returns the greatest common factors of 'a' and 'b'
	>>> gcf(25, 144)
	1"""
	for elem in (a, b):
		if not isinstance(elem, types): raise NumericalError(getError('int'))
	if a % b == 0 or b % a == 0: return min(a, b)
	return max(commonFactors(a, b))

_round = round

def round(n, base = 10):
	"""Rounds 'n' to the nearest 'base' = 10
	>>> round(5)
	10
	>>> round(160, 100)
	200"""
	return type(n)(_round(float(n) / base) * base)

def quadForm(a, b, c):
	'''Returns the x-intercepts of a quadratic equation
	>>> quadForm(1, -4, 0)
	(4.0, 0.0)'''
	for elem in (a, b, c):
		if not isinstance(elem, (types, FloatType)): raise NumericalError(type_(getError('float')))
	if b**2 > 4 * a * c:
		x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
		x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
		return (x1, x2)
	else:
		return (0, 0)

def integral(f, n = 1000, start = 0, stop = 100, method = 't', return_shapes = False):
	"""Returns the integral of function with 'n' shapes
	>>> integral('x**2')
	333333.4994999992
	>>> integral('x**2', n = 10000, start = 0, stop = 100, method = 'middle')
	333333.3324997804
	
	If return_shapes is True, then the shape dimensions are returned as well"""
	for elem in (n, start, stop):
		if not isinstance(elem, types): raise NumericalError(type_(getError('int')))
	if not isinstance(f, (StringType, FunctionType)): raise NumericalError(type_("must be str or function"))
	if not isinstance(method, str): raise NumericalError(type_(getError('str')))
	if not isinstance(return_shapes, bool): raise NumericalError(type_(getError('bool')))
	if n <= 0: raise NumericalError(value_(getError('greaterthanzero')))
	if stop <= start: raise NumericalError(value_("stop must be greater than start"))
	method = method.lower()[0]
	if method not in ('l', 'm', 'r', 't', 's'):
		raise NumericalError(value_("The method must be 'left', 'middle', 'right', 'trapezoid', or 'Simpsons'"))
	funct = lambda x: ((math_eval(f, {"__builtins__": math}, {'x': x})) if isinstance(f, str) else (f(x)))
	increment = (stop - start) / n
	num, x, shapes = 0, start, []
	if method == 'l':
		stop -= increment
		while x <= stop:
			y = funct(x)
			num += y
			if return_shapes:
				shapes.append([(x, 0), (x, y), (x + increment, y), (x + increment, 0)])
			x += increment
		return (increment * num, shapes) if return_shapes else increment * num
	elif method == 'r':
		start += increment
		x = start
		while x <= stop:
			y = funct(x)
			num += y
			if return_shapes:
				shapes.append([(x - increment, 0), (x - increment, y), (x, y), (x, 0)])
			x += increment
		return (increment * num, shapes) if return_shapes else increment * num
	elif method == 'm':
		change = increment * 0.5
		start += change
		x = start
		while x <= stop:
			y = funct(x)
			num += y
			if return_shapes:
				shapes.append([(x - change, 0), (x - change, y), (x + change, y), (x + change, 0)])
			x += increment
		return (increment * num, shapes) if return_shapes else increment * num
	elif method == 't':
		y = funct(x)
		num += y
		oY = y
		if return_shapes:
			shapes.append([(x, 0), (x, 0), (x + increment, y), (x + increment, 0)])
		x += increment
		while x <= stop:
			y = funct(x)
			num += 2 * y
			if return_shapes:
				shapes.append([(x - increment, 0), (x - increment, oY), (x, y), (x, 0)])
			x += increment
			oY = y
		y = funct(x)
		num += y
		if return_shapes:
			shapes.append([(x - increment, 0), (x - increment, oY), (x, y), (x, 0)])
		return (increment / 2 * num, shapes) if return_shapes else increment / 2* num
	elif method == 's':
		if n % 2 != 0: n += 1
		count = 2
		num += 2 * funct(x)
		while x <= (stop - increment):
			x += increment
			multiplier = 4 if count % 2 == 0 else 2
			y = multiplier * funct(x)
			num += y
			count += 1
		return (increment / 3* num, shapes) if return_shapes else increment / 3 * num
	
def triangleArea(a, b, c, h = None):
	"""Returns the area of a triangle with the largest side as the base
	>>> triangleArea(6, 8, 10)
	24.0
	>>> triangleArea(6, 8, 10, 5)
	25.0"""
	for n in (a, b, c):
		if not isinstance(n, (types, FloatType)): raise NumericalError(type_(getError('float')))
	if a + b < c: raise NumericalError(value_('a + b must be greater than c'))
	if b + c < a: raise NumericalError(value_('b + c must be greater than a'))
	if a + c < b: raise NumericalError(value_('a + c must be greater than b'))
	if h is None:
		s = 0.5 * (a + b + c)
		return (s * (s - a) * (s - b) * (s - c))**0.5
	return 0.5 * h * max(a, b, c)
	
def sinR(angle):
	"""sin(angle) measured in radians
	>>> sinR(pi*2)
	0
	>>> sinR(3*pi / 2)
	-1"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	sines = {0.0: 0, 0.5235987755982988: 0.5, 1.5707963267948966: 1, 3.6651914291880923: -0.5, 6.283185307179586: 0, 3.141592653589793: 0, 
	5.759586531581287: -0.5, 2.6179938779914944: 0.5, 4.71238898038469: -1}
	angle = round(angle, 17)
	return sines.get(angle, math.sin(angle))
	
def cosR(angle):
	"""cos(angle) measured in radians
	>>> cosR(pi*2)
	1
	>>> cosR(3*pi / 2)
	0"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	cosines = {4.1887902047863905: -0.5, 2.0943951023931953: -0.5, 
	1.5707963267948966: 0, 3.141592653589793: -1, 6.283185307179586: 1, 5.235987755982989: 0.5, 4.71238898038469: 0, 1.0471975511965976: 0.5}
	angle = round(angle, 17)
	return cosines.get(angle, math.cos(angle))
	
def tanR(angle): 
	"""tan(angle) measured in radians
	>>> tanR(pi*2)
	0
	>>> tanR(pi)
	0"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	tangents = {3.9269908169872414: 1, 5.497787143782138: -1, 1.5707963267948966: None, 
	4.71238898038469: None, 0.7853981633974483: 1, 6.283185307179586: 0, 3.141592653589793: 0, 2.356194490192345: -1}
	angle = round(angle, 17)
	return tangents.get(angle, math.tan(angle))
	
def sinD(angle):
	"""sin(angle) measured in degrees
	>>> sinD(90)
	1
	>>> sinD(180)
	0"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	return sinR(degToRad(angle))

def cosD(angle):
	"""cos(angle) measured in degrees
	>>> cosD(90)
	0
	>>> cosD(180)
	-1"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	return cosR(degToRad(angle))

def tanD(angle):
	"""sin(angle) measured in degrees
	>>> tanD(90)
	0
	>>> tanD(270)
	0"""
	if not isinstance(angle, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	return cosR(degToRad(angle))
	
def degToRad(degrees):
	"""Converts degrees to radians
	>>> degToRad(90)
	1.5707963267948966"""
	if not isinstance(degrees, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	return math.radians(degrees)

def radToDeg(radians):
	"""Converts radians to degrees
	>>> radToDeg(pi)
	180.0"""
	if not isinstance(radians, types + (decimal.Decimal,)): raise NumericalError(type_(getError('num')))
	return math.degrees(radians)
	
def gaussSum(numbers):
	'''Returns the Gaussian Sum of a sequence of numbers
	Same as sum(numbers) but more efficient
	Assumes that the sequence is not sporadic
	>>> gaussSum(range(1, 101))
	5050.0
	>>> sum(range(1, 101))
	5050
	>>> timeit(stmt = 'gaussSum(range(1, 10001))', setup = 'from nums import gaussSum', number = 1000)
	0.48374609368082133
	>>> timeit(stmt = 'sum(range(1, 10001))', number = 1000)
	0.8427124772011041'''
	if not isinstance(numbers, (ListType, SetType, TupleType)): raise NumericalError(type_(getError('iters')))
	return (numbers[0] + numbers[-1]) * (len(numbers) / 2)
	
### Examples to display module's capabilites

def example():
	'''Shows module's capabilities'''
	n = 9013
	f = 'x**2'
	
	print('Integral of x^2:', integral(f))
	print('Is n prime:', isPrime(n))
	print('number of primes upto 9013',  len(primeRange(n)))
	
if __name__ == '__main__': 
	help('nums.number_theory')