#!/bin/bash
#Set curUser
curUser=$( logname )
#Checks for root
if [[ "$( whoami )" != 'root' ]]; then
	echo 'Run as root!'
	exit 1
fi

#Check pip installs
python -c "import cursor" 2>/dev/null
if [[ "$?" != '0' ]]; then
	read -p "'cursor' module is not installed! Install now? (y/n): " installer
	if [[ "yes" == *"${installer,,}"* ]]; then
		pip install cursor
	fi
else
	echo -e "'cursor' -> \e[32mGood!\e[0m"
fi

#Check for ~/.progli directory
if [[ ! -d "/home/${curUser}/.progli" ]]; then
	echo "Creating .progli!"
	mkdir /home/${curUser}/.progli/
else
	read -p ".progli directory exists! Wipe and re-install? (y/n): " installer
	if [[ "yes" == *"${installer,,}"* ]]; then
		rm -rf /home/${curUser}/.progli/*
	else
		echo "I'll try not to clean it..."
	fi
fi

#Copies files over if .progli is empty
if [[ -z $( ls /home/$curUser/.progli ) ]]; then
	echo "Copying files into .progli"
	for i in ./.progli/*; do
		cp $i /home/$curUser/.progli/
	done
fi

#Create symlink in /usr/local/bin
if [[ ! -f "/usr/local/bin/progli" ]]; then
	echo "Creating symlink"
	ln -s /home/${curUser}/.progli/progli /usr/local/bin/progli
else
	echo "Symlink already exists!"
fi

#To: This program,
#Luv u!
