# nums.errors.py
# written by Rushy Panchal
# version 1.0

'''Errors library for the 'nums' package

'nums.errors.py' houses the NumericalError class, which is a custom Exception for the 'nums' package.
It does not serve much purpose outside of the package itself.
'''

### Change Log:

	# v1.0: Initial release, after splitting from 'nums.py' and being included in the 'nums' package

from types import *

s = set()
SetType = type(s)
del s

try: 
	types = (float, int, long) # for Python 2.x
except NameError: 
	types = (float, int) # handle Python 3.x, because 'long' was removed
	raw_input = input # also handles input in Python 3.3
	
class NumericalError(Exception):
	'''Custom class for Numerical Errors'''
	pass

def _type(extra = None):
	"""Creates a TypeError using 'extra' to be used in NumericalError:
	raise NumericalError(_type('int')) --> NumericalError: TypeError: 'int'"""
	return ("TypeError: " + extra) if not extra is None else "Incorrect Type"
	
def _value(extra = None):
	"""Creates a ValueError using 'extra' to be used in NumericalError:
	raise NumericalError(_value('3')) --> NumericalError: ValueError: '3'"""
	return ("ValueError: " + extra) if not extra is None else "Incorrect Value"

value_ = lambda extra: _value(extra)
type_ = lambda extra: _type(extra)
	
function = FunctionType

_errorTypes = {
'int': 'must be int', 'float': 'must be float', 'num': 'must be int or float', 'fraction': 'must be fraction',
'str': 'must be str', 'funct': 'must be function', 'bool': 'must be bool',
'list': 'must be list', 'set': 'must be set', 'tuple': 'must be tuple', 'iters': 'must be list, set, or tuple', 
'nonzero': 'cannot be zero', 'greaterthanzero': 'must be greater than zero', 'lessthanzero': 'must be less than zero'
}

getError = lambda error, default = '': _errorTypes.get(error, default)