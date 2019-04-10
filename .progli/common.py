## Author:	Owen Cocjin
## Version:	0.1
## Date:	09/04/19

import os

'''---------------------+
|		VARIABLES		|
+---------------------'''
global plPath
plPath="{}/program_list".format(os.path.dirname(os.path.realpath(__file__)))

'''---------------------+
|		FUNCTIONS		|
+---------------------'''
def error(location, message="Unknown Error", code=1):
	print("\033[31m[\033[34m|\033[31mX]\033[0m({}): {}".format(location, message))
	exit(code)

#To: This program,
#Luv u!
