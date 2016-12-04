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

function usage ()
{
	echo "Usage: bash $0 <up/down>"
}

if [[ $# -ne 1 ]]; then
	usage
	exit 1
fi

iniFile='list.ini'
commit="`date +%y%m%d` nightly"
if [[ $1 == 'up' ]]; then
	for line in `cat $iniFile`
	do
		echo "up->${line}"
		push $line
	done
elif [[ $1 == 'down' ]]; then
	for line in `cat $iniFile`
	do
		echo "down->${line}"
		pull $line
	done
else
	usage
fi
