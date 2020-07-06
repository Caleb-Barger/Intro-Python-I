"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# check if another arg was passed
if len(sys.argv) > 1:
    print(f'First Arg: {sys.argv[1]}') # prints first arg passed
else:
    print('First Arg: None') 


# Print out the OS platform you're using:
# YOUR CODE HERE
if sys.platform == 'win32':
    print('Platform: windows scrub')

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f'Running version: {sys.version[0]}')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f'Process ID: {os.getpid()}')

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'Dir: {os.getcwd()}')


# Print out your machine's login name
# YOUR CODE HERE
print(f'Login: {os.getlogin()}')

