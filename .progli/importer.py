#!/bin/python3
## Author:	Owen Cocjin
## Version:	0.1
## Date:	09/04/19

from common import *

'''-----------------+
|		CLASSES		|
+-----------------'''
class Program():
	'''A class that holds all the info for a program'''
	all_programs=[]

	def __init__(self, name):
		'''
		A program MUST have a name.
		It MAY have a description, commonly used command, and multiple notes
		'''
		self.name=name
		self.description=""
		self.command=""
		self.notes=[]
		Program.all_programs.append(self)

	def __str__(self):
		'''Formatted print output. This should simplify the listing process'''
		toReturn="    \033[4m\033[1m\033[36m{}\033[0m".format(self.name) #Always return the name

		#Returns description if one exists
		if self.description!='':
			toReturn+="\n\t\033[0m{}\033[0m".format(self.description)

		#Returns common command if one exists
		if self.command!='':
			toReturn+="\n\t\033[2m{}\033[0m".format(self.command)

		#Returns notes, if any
		if len(self.notes)>0:
			for i in self.notes:
				toReturn+="\n\t\033[33m\t- {}\033[0m".format(i)

		return toReturn+'\n'

	def setName(self, new):
		self.name=new
	def getName(self):
		return self.name

	def setDescription(self, new):
		self.description=new
	def getDescription(self):
		return self.description

	def setCommand(self, new):
		self.command=new
	def getCommand(self):
		return self.command

	def addNote(self, new):
		self.notes.append(new)
	def removeNote(self, old):
		'''Removes a note. Takes the position of the note as an argument'''
		self.notes.remove(old)
	def getNotes(self):
		return self.notes
	def editNote(self, notePos, new):
		try:
			self.notes[notePos]=new
		except IndexError:
			error("importer.Program.editNote", "Invalid position given!")

'''-----------------+
|		MAIN		|
+-----------------'''
#Loop through the program_list file, "compiling" the programs and adding them
#to the list
global program_list
with open(plPath) as program_list:
	try:
		curLine=program_list.readline().strip()
		lineCounter=0
		while curLine!='':
			lineCounter+=1
			if curLine[0]==';':
				curProgram=''
				pass #If the current line is a semicolon, erase curProgram, then skip it

			#If the first character is a '-', we create a Program
			elif curLine[0]=='-':
				#Create a Program named whatever is on the line
				curProgram=Program(curLine[1:])

			#Add a definition
			elif curLine[0]=='(':
				if curLine.strip("()")!="":
					curProgram.setDescription(curLine.strip("()"))

			#Add a common command
			elif curLine[0]=='{':
				if curLine.strip("{}")!="":
					curProgram.setCommand(curLine.strip("{}"))

			#Add notes (if any)
			elif curLine[0]=="+":
				while curLine[0]=="+":
					curProgram.addNote(curLine[1:])
					curLine=program_list.readline().strip()
					lineCounter+=1

			#Any line that starts with any other character throws an error
			else:
				error("importer.main", "Invalid line in program_list (line {})".format(lineCounter))
			curLine=program_list.readline().strip()

	except NameError:
		error("importer.main", "Error found! Probably error in formatting of program_list")
