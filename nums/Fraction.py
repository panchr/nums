# nums.Fraction.py
# written by Rushy Panchal
# version 1.12

'''Fraction library

'nums.Fraction.py' includes the Fraction class, which has numerous uses.
	
OVERVIEW:
	The 'Fraction' library has the Fraction class, which can be used to depict fractions. 
	Fraction instances support operators. They also have various built-in methods, including inherited methods from the built-in 'object' class.
	Example (run nums.Fraction.example() to see this example):

	-------------------------------------------------------
	from nums.Fraction import *
	a = Fraction(1, 2)
	b = Fraction(1, 2)
	print('a: {a}, b: {b}'.format(a = a, b = b))
	print('a + b = {result}'.format(result = a + b))
	print('a - b = {result}'.format(result = a - b))
	print('a * b = {result}'.format(result = a * b))
	print('a / b = {result}'.format(result = a / b))
	-------------------------------------------------------
'''

### Change Log:

	# v1.0: Initial release, with primitive functions
	# v1.1: Operator overloading: Added '+' and '-' operators for addition and subtraction, respectively
		# v1.11: Added '*' and '/' operators for multiplication and division, respectively
		# v1.12: Added '>', '>=', '<', '<=', '==', and '!=' logical operators; also, examples for each method were added
	
from __future__ import division
from nums.number_theory import gcf, commonFactors
from nums.errors import *

__version__ = 1.11
__author__ = "Rushy Panchal"

### Main Fraction class

class Fraction(object):
	"""Class for explicit fractions"""
	def __init__(self, numerator, denominator = None):
		"""Creates a fraction with numerator / denominator
		>>> Fraction(1, 5)
		<nums.Fraction.Fraction instance at 0x21796b0>: 1/5
		>>> Fraction(0.2)
		<nums.Fraction.Fraction instance at 0x213c4b0>: 0.2/1
		>>> Fraction('1/5')
		<nums.Fraction.Fraction instance at 0x21ecef0>: 1.0/5.0
		>>> f = Fraction(1, 2)"""
		if denominator is None:
			if isinstance(numerator, str):
				parts = numerator.split("/")
				numerator, denominator = float(parts[0]), float(parts[1])
			else:
				denominator = 1
		elif denominator == 0:
			raise NumericalError(value_(getError('nonzero')))
		for elem in (numerator, denominator):
			if not isinstance(elem, types): raise NumericalError(type_(getError('num')))
		self.num, self.dom = numerator, denominator
		
	def fraction(self):
		'''Returns a tuple of (numerator, denominator)
		>>> f.fraction()
		(1, 2)'''
		return (self.num, self.dom)
		
	def decimal(self):
		'''Returns the decimal value of a fraction
		>>> f.decimal()
		0.5'''
		return self.num/self.dom
		
	def simplify(self):
		'''Simplifies a fraction
		>>> x = Fraction(5, 10)
		>>> x.simplify()
		<nums.Fraction.Fraction instance at 0x21ec7f0>: 1.0/2.0'''
		self.gcf = int(gcf(self.num, self.dom))
		if self.gcf == 0: self.gcf = 1
		while self.num % self.gcf != 0 and self.num % self.gcf != 0: self.gcf -= 1
		return Fraction(self.num/self.gcf, self.dom/self.gcf)
		
	def change(self, numerator, denominator):
		'''Changes the values of a fraction
		>>> f.change(1, 5)
		>>> f
		<nums.Fraction.Fraction instance at 0x2249650>: 1/5'''
		self.__init__(numerator, denominator)
		
	def lcd(self, fraction):
		'''Lowest common denominator of two fractions
		>>> f.lcd(x)
		1'''
		if isinstance(fraction, Fraction):
			d1, d2 = self.dom, fraction.dom
		elif isinstance(fraction, TupleType):
			d1, d2 = self.dom, fraction[1]
		else:
			 raise NumericalError(type_("must be fraction or tuple"))
		return min(commonFactors(d1, d2))
		
	def reciprocal(self):
		'''Reciprocal of the fraction
		>>> f.reciprocal()
		<nums.Fraction.Fraction instance at 0x21ec7f0>: 5/1'''
		return Fraction(self.dom, self.num)
		
	def makeFraction(self, n):
		'''Makes an integer into a Fraction using this instance's denominator as the denominator of the new fraction
		>>> f.makeFraction(25)
		<nums.Fraction.Fraction instance at 0x21ec7f0>: 25/1'''
		f = Fraction(n, 1)
		f.makeDenom(self.dom)
		return f.simplify()
		
	def makeSame(self, fraction):
		'''Changes 'fraction' to have the same denominator as the current instance
		>>> a = Fraction(1, 5)
		>>> b = Fraction(23, 15)
		>>> a.makeSame(b)
		>>> a
		<nums.Fraction.Fraction instance at 0x21ecf50>: 1/5
		>>> b
		<nums.Fraction.Fraction instance at 0x2249630>: 7.66666666667/5'''
		fraction.makeDenom(self.dom)
		
	def makeDenom(self, denom):
		'''Makes the denominator to 'denom' and scales the numerator appropiately
		>>> f.makeDenom(25)
		>>> f
		<nums.Fraction.Fraction instance at 0x2249650>: 5.0/25'''
		ratio = self.dom / denom
		newNum = self.num / ratio
		self.change(newNum, denom)
		
	def makeNum(self, num):
		'''Makes the numerator to 'num' and scales the denominator appropiately
		>>> f.makeNum(25)
		>>> f
		<nums.Fraction.Fraction instance at 0x2249650>: 25/125.0'''
		ratio = self.num / num
		newDenom = self.dom / ratio
		self.change(num, newDenom)
		
	def changeDenom(self, denom):
		'''Same as makeDenom(self, denom)
		>>> f.makeDenom(25)
		>>> f
		<nums.Fraction.Fraction instance at 0x2249650>: 5.0/25'''
		self.makeDenom(denom)
		
	def changeNum(self, num):
		'''Same as makeNum(self, num)
		>>> f.makeNum(25)
		>>> f
		<nums.Fraction.Fraction instance at 0x2249650>: 25/125.0'''
		self.makeNum(num)
		
	def add(self, fraction):
		'''Adds two fractions'''
		if isinstance(fraction, types):
			fraction = self.makeFraction(fraction)
		if not isinstance(fraction, Fraction): raise NumericalError((getError('fraction')))
		f1 = self.simplify()
		f2 = fraction.simplify()
		new_f2 = Fraction(*f2)
		new_f2.makeDenom(f1[1])
		f = Fraction(f1[0] + new_f2.num, f1[1])
		return Fraction(*f.simplify())
		
	def subtract(self, fraction):
		'''Subtracts fraction from this fraction'''
		if isinstance(fraction, types):
			fraction = self.makeFraction(fraction)
		if not isinstance(fraction, Fraction): raise NumericalError((getError('fraction')))
		f1 = self.simplify()
		f2 = fraction.simplify()
		new_f2 = Fraction(*f2)
		new_f2.makeDenom(f1[1])
		f = Fraction(f1[0] - new_f2.num, f1[1])
		return Fraction(*f.simplify())
		
	def multiply(self, fraction):
		'''Multiplies two fractions'''
		if isinstance(fraction, types):
			return (self.num*fraction, self.dom)
		if not isinstance(fraction, Fraction): raise NumericalError((getError('fraction')))
		return Fraction(self.num*fraction.num, self.dom*fraction.dom)
		
	def divide(self, fraction):
		'''Divides this fraction by fraction'''
		r = fraction.reciprocal()
		return self.multiply(Fraction(*r))
		
	def __add__(self, other):
		'''Allows the usage of the '+' operator with fractions'''
		return self.add(other)
		
	def __sub__(self, other):
		'''Allows the usage of the '-' operator with fractions'''
		return self.subtract(other)
		
	def __mul__(self, other):
		'''Allows the usage of the '*' operator with fractions'''
		return self.multiply(other)
		
	def __div__(self, other):
		'''Allows the usage of the '/' operator with fractions'''
		return self.divide(other)
		
	def __truediv__(self, other):
		'''Allows the usage of the '/' operator with fractions'''
		return self.divide(other)
		
	def __lt__(self, other):
		'''Allows the usage of the '<' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num < other.num
		
	def __le__(self, other):
		'''Allows the usage of the '<=' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num <= other.num
		
	def __eq__(self, other):
		'''Allows the usage of the '==' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num == other.num
		
	def __ne__(self, other):
		'''Allows the usage of the '!=' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num != other.num
	
	def __gt__(self, other):
		'''Allows the usage of the '>' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num > other.num
		
	def __ge__(self, other):
		'''Allows the usage of the '>=' operator with fractions'''
		if self.dom != other.dom: other.makeSame(self)
		return self.num >= other.num
		
	def __getitem__(self, index):
		'''Allows the usage of the [ ] operators with fractions'''
		if index % 2 == 0: return self.num
		else: return self.dom
		
	def __nonzero__(self):
		'''Returns a boolean if it is or isn't zero'''
		if self.num == 0: return False
		else: return True
		
	__radd__ = lambda self, other: self.__add__(other)
	__rsub__ = lambda self, other: self.__sub__(other)
	__rmul__ = lambda self, other: self.__mul__(other)
	__rdiv__ = lambda self, other: self.__div__(other)
		
	def __repr__(self):
		'''Creates a representation of the Fraction instance'''
		return "<nums.Fraction.Fraction instance at {mem}>: {num}/{dom}".format(mem = hex(id(self)), num = self.num, dom = self.dom)
		
	def __float__(self):
		return self.decimal()
		
	def __int__(self):
		return int(self.decimal())
		
### Module-level functions to manipulate Fractions
		
def addFractions(f1, f2):
	"""Adds fractions f1 and f2"""
	if not isinstance(f1, Fraction) or not isinstance(f2, Fraction): raise NumericalError((getError('fraction')))
	return f1.add(f2)
	
def subtractFractions(f1, f2):
	"""Subtracts fractions f1 and f2"""
	if not isinstance(f1, Fraction) or not isinstance(f2, Fraction): raise NumericalError((getError('fraction')))
	return f1.subtract(f2)
		
def multiplyFractions(f1, f2):
	"""Multiplies fractions f1 and f2"""
	if not isinstance(f1, Fraction) or not isinstance(f2, Fraction): raise NumericalError((getError('fraction')))
	return f1.multiply(f2)
		
def divideFractions(f1, f2):
	"""Divides fractions f1 and f2"""
	if not isinstance(f1, Fraction) or not isinstance(f2, Fraction): raise NumericalError((getError('fraction')))
	return f1.divide(f2)
	
def makeFraction(n):
	'''Creates a fraction of "n/1" and simplifies it'''
	if not isinstance(n, types): raise NumericalError((getError('num')))
	x = 1
	if isinstance(n, FloatType):
		x = 10 ** (len(str(n).split('.')[1]))
	f = Fraction(n * x, x)
	return Fraction(*f.simplify())
	
def makeSimpleFraction(n):
	'''Creates a fraction of "n/1"'''
	if not isinstance(n, types): raise NumericalError((getError('num')))
	return Fraction(n, 1)
	
def continuedFraction(n):
	'''Creates a continued fraction of "n"'''
	pass
	
# from __future__ import division
# from nums.Fraction import *

# '''see http://en.wikipedia.org/wiki/Continued_fraction'''

# def continuedFraction(d, frac = []):
	# if d.num == 0 or d.dom == 0: return []
	# n = makeFraction(int(d.num/d.dom)) # gets stuck here
	# d = makeFraction(d.num/d.dom)
	# print d, n # testing purposes
	# frac.append(int(n.num))
	# d -= n
	# d = d.reciprocal()
	# print '\t', d, n, '\n' # testing purposes
	# return frac + (continuedFraction(d, frac))

# print continuedFraction(makeSimpleFraction(3.245))
	
### Examples to display the module's capabilities
		
def example():
	'''Show's module's capabilities'''
	a = Fraction(1, 2)
	b = Fraction(1, 2)
	print('a: {a}, b: {b}'.format(a = a, b = b))
	print('a + b = {result}'.format(result = a + b))
	print('a - b = {result}'.format(result = a - b))
	print('a * b = {result}'.format(result = a * b))
	print('a / b = {result}'.format(result = a / b))
		
if __name__ == '__main__':
	help('nums.Fraction')