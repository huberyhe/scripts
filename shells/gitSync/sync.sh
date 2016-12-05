#!/bin/bash

function push ()
{
	cd $1
	hasModified=`git status -s | wc -l`
	if [[ $hasModified -ne 0 ]]; then
		echo 'hasModified'
		git add -A
		git commit -m "$commit"
		git push origin master
	fi
}

function pull ()
{
	cd $1
	hasUpdated=`git fetch origin master:tmp && git diff --summary tmp | wc -l`
	if [[ $hasUpdated -ne 0 ]]; then
		echo 'hasUpdated'
		git merge tmp
	fi
}

function add ()
{
	if [[ ! -d $1 ]]; then
		echo 'dir not exist.'
		return
	fi
	dirName=$1
	cd -P $dirName
	dirFullName=$(pwd)
	cd -P - >/dev/null
	yellow "add -> $dirFullName"
	dirFullNameParse=${dirFullName//\//\\/}
	hasLine=`sed -n "/^${dirFullNameParse}[/]*$/p" $iniFile | wc -l`
	if [[ $hasLine -ne 0 ]]; then
		echo 'alreay in list, ignore.'
		return
	fi
	echo $dirFullName >> $iniFile
	echo 'done.'
}

function delete ()
{
	if [[ ! -d $1 ]]; then
		echo 'dir not exist.'
		return
	fi
	dirName=$1
	cd -P $dirName
	dirFullName=$(pwd)
	cd -P - >/dev/null
	yellow "delete -> $dirFullName"
	dirFullNameParse=${dirFullName//\//\\/}
	hasLine=`sed -n "/^${dirFullNameParse}[/]*$/p" $iniFile | wc -l`
	if [[ $hasLine -eq 0 ]]; then
		echo 'not in list, ignore.'
		return
	fi
	sed -i "/^${dirFullNameParse}[/]*$/d" $iniFile
	echo 'done.'
}

function usage ()
{
	echo "Usage: bash $0 <up/down/add/delete> [dirname]"
	echo "Help to sync git repo every day and night."
	echo "	bash $0 up					automatically push all git repo after dayly work"
	echo "	bash $0 down				automatically pull all git repo before dayly work"
	echo "	bash $0 add [dirname]			add a git repo, "
	echo "	bash $0 delete [dirname]			delete a git repo"
}

function yellow() {
    str_len=${#1}
    echo -e "\033[33m$1\033[0m"
}

if [[ $# -lt 1 ]]; then
	usage
	exit 1
fi

scriptPath=$(dirname $0)
scriptPath=${scriptPath/\./$(pwd)}
iniFile="$scriptPath/list.ini"
commit="`date +%y%m%d` - nightly"
if [[ $1 == 'up' ]]; then
	cat list.ini | while read line; do
		if [[ ${line:0:1} == '#' ]]; then
			continue
		fi
		yellow "up -> ${line}"
		push $line
	done

elif [[ $1 == 'down' ]]; then
	cat list.ini | while read line; do
		if [[ ${line:0:1} == '#' ]]; then
			continue
		fi
		yellow "down -> ${line}"
		pull $line
	done
elif [[ $1 == 'add' ]]; then
	if [[ $2 == '' ]]; then
		targetDir=`pwd`
	else
		targetDir=$2
	fi
	add $targetDir
elif [[ $1 == 'delete' ]]; then
	if [[ $2 == '' ]]; then
		targetDir=`pwd`
	else
		targetDir=$2
	fi
	delete $targetDir
else
	usage
fi