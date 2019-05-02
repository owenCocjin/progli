## Author:	Owen Cocjin
## Version:	0.3
## Date:	30/04/19

import sys  #Required!
#--------User's imports--------#
import time, cursor
#              ^-- pip installed library
from importer import *
from common import *
from os import get_terminal_size

'''-------------------+
|        SETUP        |
+-------------------'''
#--------Variables--------#
flags=[]
assigned={}
args=[]

#--------Process sys.argv--------#
#Find flags in sys.argv and save them
sys.argv=sys.argv[1:]  #Remove first arg
for i, n in enumerate(sys.argv):
	#If current arg starts with '-', it's a flag
	if n[0]=='-':
		#If curreng arg starts with '--', its it's own flag
		if n[1]=='-':
			#Add the whole flag
			flags.append(n[2:])
		else:
			#Count each individual char as a flag
			for j in n[1:]:
				#Try assigning the next argument to this flag
				flags.append(j)
			try:
				assigned[j]=sys.argv[i+1]
			except:
				pass
	else:
		#counts as an argument
		args.append(n[0:9])

'''-----------------------+
|        VARIABLES        |
+-----------------------'''
programName=''
try:
	programName=args[0]
except:
	pass

'''-----------------------+
|        FUNCTIONS        |
+-----------------------'''
def add():
	print("Adding \"{}\"!".format(programName))
	with open(plPath, "a") as program_list:
		curProgram=Program(programName)
		description=str(input("Description (leave blank for none):\n"))
		command=str(input("Common command (leave blank for none):\n"))
		#Get notes
		allNotes=[]
		print("Notes (1 note/line. Leave blank for none):")
		while True:
			note=str(input("+ "))
			if note!='':
				allNotes.append(note)
			else:
				break

		#Write new Program to the program_list file
		program_list.write("-{}\n".format(curProgram.getName()))
		if description!='':
			program_list.write("({})\n".format(description))
		if command!='':
			program_list.write("{"+command+"}\n")
		if len(allNotes)!=0:
			for i in allNotes:
				program_list.write("+{}\n".format(i))
		program_list.write(";\n")
	exit(0)

def delete():
	if input("Are you sure?(yes/no): ").lower()=="yes":
		print(f"Deleting {programName}!")
		with open(plPath, "r+") as program_list:
			prev=program_list.readlines()
			#If nothing was found, program won't exit, throwing error below
			if '-'+programName+'\n' not in prev:
				print("\"{}\" not found! Nothing deleted.".format(programName))
				exit(0)

			program_list.seek(0)  #Reset to beginning of file
			for i, p in enumerate(prev):
				#Need try because if lines are deleted, length of prev shrinks,
				#but the for loop doesn't know this. If an IndexError is
				#raised (meaning we've reached the end of the list), leave
				if programName!=p[1:].strip():
					print(f"Writing: {p}")
					program_list.write(p)
				else:
					while prev[i].strip()!=';':
						print(prev[i].strip())
						del(prev[i])
					print("\"{}\" deleted!".format(programName))

			program_list.truncate()
			exit(0)

	else:
		print("Don't worry, I won't delete anything.")
	exit(0)

def edit():
	curProgram=''
	#loop through all Program names
	for i in Program.all_programs:
		if i.getName()==programName:
			curProgram=i
	if curProgram=='':
		print("Couldn't find \"{}\"".format(programName))
		exit(1)

	#Going to alternative buffer
	print("\033[?1049h")
	while True:
		#Prints everything
		cols, rows=get_terminal_size()
		print("\033[2J\033[2;H", end='')
		print(curProgram)
		print("\033[{};2H:".format(rows-1), end='')
		altBuff=input().split(':')
		try:
			#Quit
			if altBuff[0].lower() in ["q", "quit"]:
				print("\033[{};2H".format(rows-2), end='')
				print("Quit without saving?\033[J")
				print("\033[{};2H:".format(rows-1), end='')
				if input().lower() in ["y", "yes"]:
					print("\033[?1049l", end='')
					break
				else:
					continue
			#Save & quit
			elif altBuff[0].lower() in ["s", "save"]:
				print("\033[{};2H".format(rows-2), end='')
				print("Save and quit?\033[J")
				print("\033[{};2H:".format(rows-1), end='')

				if input().lower() in ["y", "yes"]:
					#Write new Program to file
					#Open the program_list and read and write everything
					with open(plPath, "r+") as program_list:
						prev=program_list.readlines()
						oldProgramIndex=prev.index('-'+programName+'\n')  #all lines end with '\n'

						#Deleting the old program
						while prev[oldProgramIndex][0]!=';':
							del(prev[oldProgramIndex])
						del(prev[oldProgramIndex])  #Delete the final ';'
						#Writing new program
						prev.insert(oldProgramIndex, "-"+curProgram.getName()+'\n')  #Insert name
						program_list.seek(0)  #Return to top of file

						#Loop through prev, writing each item
						for i in prev:
							#If we haven't found the name we inserted, just write
							if i!=("-"+curProgram.getName()+'\n'):
								program_list.write(i)
							else:
								program_list.write(i)  #Write name to file
								if curProgram.getDescription()!='':
									program_list.write("({})\n".format(curProgram.getDescription()))
								if curProgram.getCommand()!='':
									program_list.write("{"+curProgram.getCommand()+"}\n")
									oldProgramIndex+=1
								if len(curProgram.getNotes())!=0:
									for i in curProgram.getNotes():
										program_list.write('+'+i+'\n')
								program_list.write(';\n')
						program_list.truncate()

					#File is done saving!
					cursor.hide()
					print(f"\033[{rows-2};2H\033[JSaved!")
					input(" <Press enter to continue>")
					print("\033[?1049l\033[0m", end='')
					cursor.show()
					break
				else:
					print("Not saving...")

			#Edit name
			elif altBuff[0].lower() in ["n", "name"]:
				curProgram.setName(altBuff[1])
			#Edit description
			elif altBuff[0].lower() in ["d", "description"]:
				if altBuff[1]!=' ':
					curProgram.setDescription(altBuff[1])
			#Edit command
			elif altBuff[0].lower() in ["c", "command"]:
				if altBuff[1]!=' ':
					curProgram.setCommand(altBuff[1])
			#Handle notes
			elif altBuff[0].lower() in ["j", "notes", "note"]:
				noOfNotes=len(curProgram.getNotes())
				#Adds a note if position is longer than # of notes
				if int(altBuff[1])>=noOfNotes:
					curProgram.addNote(altBuff[2])
				#Removes a note at specific position
				elif 0<=int(altBuff[1])<noOfNotes:
					if altBuff[2]=='':
						curProgram.removeNote(int(altBuff[1]))
					else:
						curProgram.editNote(int(altBuff[1]), altBuff[2])
			else:
				continue
		except:
			pass
	exit(0)

#Luv u!
