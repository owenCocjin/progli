#!/bin/bash
#Set curUser & other vars
curUser=$( logname )
dirdotprogli="/home/${curUser}/.progli/"
#Checks for root
if [[ "$( whoami )" != 'root' ]]; then
	echo 'Run as root!'
	exit 1
fi

#remove pip installs
echo -en "\e[33mRemove 'cursor' module? Other python programs may require it (y/n): \e[0m"
read remover
echo -en "\t"  #Print the next line with a tab
if [[ "yes" == *"${remover,,}"* ]]; then
	echo 'y' | pip uninstall cursor &>/dev/null
	python -c "import cursor" &>/dev/null
	if [[ "$?" != '0' ]]; then  #If can't import cursor (isn't installed), an error is thrown
		echo "Removed 'cursor' using pip!"
	else
		echo "Something went wrong!"
	fi
else
	echo "Keeping 'cursor'"
fi

#Remove .progli directory
echo -e "\e[33mRemoving .progli & contents...\e[0m"
echo -en "\t"  #Print the next line with a tab
rm -rf $dirdotprogli
#Check if .progli was removed
if [[ -d "$dirdotprogli" ]]; then
	echo "Couldn't remove ${dirdotprogli} ! You can try manually removing it."
else
	echo "Removed .progli!"
fi

#Remove symlink
echo -e "\e[33mRemoving progli symlink...\e[0m"
echo -en "\t"
rm -rf /usr/local/bin/progli
if [[ -f /usr/local/bin/progli ]]; then
	echo "Couldn't remove /usr/local/bin/progli ! You can try manually removing it."
else
	echo "Removed progli symlink!"
fi
echo "================================="
echo "Thanks for trying out my program!"
echo "================================="

#To: This program,
#Luv u!
