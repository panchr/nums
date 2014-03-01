# nums.bases.py
# written by Rushy Panchal
# Version 1.0

'''Simple number-manipulation and number-theory library

nums.bases.py contains various classes and base structures to be used in the nums package.

These are meant to be used internally, but can be used directly if needed.'''

import inspect
import types
import math
import re

### Main functions

def math_eval(*args, **kwargs):
	'''Tries to evaluate the function but returns 0 if there is an error'''
	try:
		return eval(*args, **kwargs)
	except (ValueError, ZeroDivisionError):
		return 0

### Main classes

class Function(object):
	'''Creates a parsable representation of a function'''
	def __init__(self, function):
		self.funct_str = False
		self.variables = {}
		if isinstance(function, str):
			self.funct_str = self.parse(function)
			self.function = lambda **variables: eval(function, {"__builtins__": math}, variables)
		elif isinstance(function, (types.FunctionType, types.LambdaType)):
			self.function = function
		else:
			raise TypeError("function can only be a string or callable")
			
	def __call__(self, **variables):
		'''Calls the function'''
		return self.evaluate(**variables)
			
	def __str__(self):
		'''Returns a string representation of the function'''
		return self.funct_str
		
	def parse(self, string):
		'''Parses the string and returns a formatted function'''
		function = ''.join(string.split(' ')).replace('^', '**')
		pattern = re.compile("([0-9]+|[a-z])(?=[a-z\(])", re.IGNORECASE)
		pattern2 = re.compile("([\)])([0-9]+|[a-z])", re.IGNORECASE)
		function = pattern2.sub('\\1*\\2', pattern.sub('\\1*', function))
		return function
			
	def createVariable(self, *names):
		'''Creates the variable(s)'''
		for name in names:
			self.setVariable(name, 0)
	
	def detectVariables(self):
		'''Tries to find any variables'''
		variable_pattern = re.compile('([a-z]+)(?!{})'.format('|'.join(math.__dict__.keys())))
		variables = variable_pattern.findall(self.funct_str)
		return variables
	
	def setVariable(self, name, value = 0):
		'''Sets the variable to the value'''
		self.variables[name] = value
		
	def delVariable(self, *names):
		'''Deletes the variable(s)'''
		for name in names:
			del self.variables[name]
			
	def evaluate(self, **variables):
		'''Evaluates the function by plugging the variables'''
		if "variable" in variables.keys():
			def_value = variables["variable"]
			all_variables = self.detectVariables() if self.funct_str else inspect.getargspec(self.function)
			for v in all_variables:
				if v not in variables.keys(): 
					variables[v] = def_value
			del variables["variable"]
		if not variables:
			variables = self.variables.copy()
		else:
			self.variables = variables.copy()
		return self.function(**variables)