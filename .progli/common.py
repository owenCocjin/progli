## Author:	Owen Cocjin
## Version:	0.2
## Date:	30/04/19

import os

'''-----------------------+
|        VARIABLES        |
+-----------------------'''
plPath="{}/program_list".format(os.path.dirname(os.path.realpath(__file__)))
'''-----------------------+
|        FUNCTIONS        |
+-----------------------'''
def error(location, message="Unknown Error", code=1):
	print("\033[31m[\033[34m|\033[31mX]\033[0m({}): {}".format(location, message))
	exit(code)

def usage():
	print('''
\033[33mUsage:\033[0m progli [-adh] [PROGNAME]
\tOrganizer for installed programs, aliases, or just help with common commands.
\n\033[33mArguments:\033[0m
\t-a, --add\tAdds an entry to the list
\t-d, --delete\tRemoves an entry from the list
\t-e, --edit\tEdit specific Program
\t-h, --help\tPrints this screen
\t-l, --list\tLists all programs
\t-s,\t\tLists all programs alphabetically
\t-t,\t\tLists all programs in detail
\n\033[33mExamples:\033[0m
\tprogli
\tprogli -l
\t\t\033[2mJust prints the program names\033[0m\n
\tprogli -a newProgramName
\tprogli -d programToDelete
\tprogli -e programToFix
\t\t\033[2mCommands (Leave any text field empty to remove):
\t\t  n:newName
\t\t  d:newDefinition
\t\t  c:newCommand
\t\t  j:#:newNote <- # is note position.
\t\t\t\t 1st note @ pos 0.
\t\t\t\t #>number of notes to add new note\033[0m
	'''.format())
	exit(1)

#Luv u
