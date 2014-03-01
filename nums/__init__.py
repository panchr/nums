# nums.__init__.py
# written by Rushy Panchal
# Version 1.0

'''Library for number manipulation, sequences, and number theory applications.

'nums' contains various modules with classes and functions found in mathematics (of various levels). 
These functions can be applied in number-theory and complex calculations. There are also sequence-generators.
Examples of the usage of various functions are in their respective modules.

INSTALLATION: 
	Save 'nums' in a location that Python can see:
	If Python is installed at 'C:\Python27', place 'nums' in 'C:\Python27\Lib\site-packages'.
	This can also be placed in any folder in your PYTHONPATH environment variable.

PLATFORMS:
	'nums' will work on any platform where standard Python libraries are available.
	No external libraries are used, but some functions and modules rely on each other, so installing the whole package is recommended.
	Download Python and/or the standard libraries here: 
		http://python.org/download/
	In addition, 'nums' supports both Python 2.7 and Python 3.3 (the current standard releases). However, 3.3 users may need to port the code.
	To open 'python.org', run 'nums.__init__platforms()'.
	
LICENSE:
	'nums' is packaged and published as open-software and does not come with any warranties. It is packaged under the General Public License (GPL):
		http://www.gnu.org/licenses/gpl.html
	To open the license, run 'nums.__init__.license()'.
'''
import webbrowser

### Change Log:

	# v1.0: Initial release: 'nums.py' is split into a package
	
'''
To do:
* A random module? using primes as the basis in a complex equation that involves current memory usage and the current time
* Trigonometry module? (with a Pi class, sin, cos, tan functions, etc)
* Add descriptions to each file, and examples for each function/class/method
'''

### All functions, classes, and modules

modules = ['number_theory.py', 'sequences.py', 'bases.py', 'Fraction.py', 'errors.py']

from nums.number_theory import *
from nums.sequences import *
from nums.Fraction import *
from nums.errors import *
from nums.bases import *

### Package information
	
_license = """
'nums' is packaged and published as open-software and does not come with any warranties. It is packaged under the General Public License (GPL):\n
\thttp://www.gnu.org/licenses/gpl.html"""
	
_platforms = """
'nums' will work on any platform where standard Python libraries are available.\n
No external libraries are used, but some functions rely on each other, so installing the whole package is recommended.\n
Download Python and/or the standard libraries here: \n
\thttp://python.org/download/\n
In addition, 'nums' supports both Python 2.7 and Python 3.3 (the current standard releases)."""
	
_author = """
Written by Rushy Panchal:
\t panchr@d-e.org"""

__author__ = "Rushy Panchal"

__version__ = 1.0
	
def information():
	'''Gives main information about nums'''
	print("""
	AUTHOR:
		{author}
	INSTALLATION: 
		Save 'number_theory.py' in a location that Python can see:
		If Python is installed at 'C:\Python', place 'nums' in 'C:\Python27\Lib\site-packages'.
		For faster importation time, run 'nums.compilePackage.py'
		This can also be placed in any folder in your PYTHONPATH environment variable.
	\nPLATFORMS:
		{platform_info}
	\nLICENSE:
		{license_info}
	""".format(platform_info = _platforms, license_info = _license, author = _author))
	
def license():
	'''Displays license of nums'''
	print(_license)
	raw_input('\nPress enter to open GNU/GPL')
	webbrowser.open_new_tab('http://www.gnu.org/licenses/gpl.html')
	
def platforms():
	'''Displays the platforms that 'nums' supports'''
	print(_platforms)
	raw_input('\nPress enter to open python.org')
	webbrowser.open_new_tab('http://python.org/download/')
