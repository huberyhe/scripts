#!/bin/bash
set -x

function push ()
{
	if [[ ! -d $1 ]]; then
		red 'dir not exist.'
		return
	fi
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
	if [[ ! -d $1 ]]; then
		red 'dir not exist.'
		return
	fi
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
		red 'dir not exist.'
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
		red 'dir not exist.'
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
	echo "Usage: bash $0 <open/up/down/add/delete> [dirname]"
	echo "Help to sync git repo every day and night."
	echo "	open				open all work directorys"
	echo "	up				automatically push all git repo after dayly work"
	echo "	down				automatically pull all git repo before dayly work"
	echo "	add [dirname]			add a git repo, current directory in default"
	echo "	delete [dirname]		delete a git repo, current directory in default"
}


function red() {
    str_len=${#1}
    echo -e "\033[31m$1\033[0m"
}

function green() {
    str_len=${#1}
    echo -e "\033[32m$1\033[0m"
}

function yellow() {
    str_len=${#1}
    echo -e "\033[33m$1\033[0m"
}

function blue() {
    str_len=${#1}
    echo -e "\033[34m$1\033[0m"
}

if [[ $# -lt 1 ]]; then
	usage
	exit 1
fi

scriptPath=$(dirname $0)
scriptPath=${scriptPath/\./$(pwd)}
iniFile="$scriptPath/list.ini"
commit="`date +%y%m%d` - nightly"


# WID=$(xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"| awk '{print $5}')
# xdotool windowfocus $WID
# xdotool key ctrl+shift+t
# wmctrl -i -a $WID
# sleep 1;
# xdotool type --delay 1 --clearmodifiers "cd";
# xdotool key Return;
###### http://stackoverflow.com/questions/1188959/open-a-new-tab-in-gnome-terminal-using-command-line
###### http://blog.csdn.net/swust_long/article/details/7285147
###### http://blog.csdn.net/namelcx/article/details/49453911

if [[ $1 == 'open' ]]; then
	openCMD=''
	while read line; do
		if [[ ${line:0:1} == '#' ]]; then
			continue
		fi
		dirName=$line
		cd -P $dirName
		dirFullName=$(pwd)
		cd -P - >/dev/null
		yellow "open -> ${dirFullName}"
		if [[ ! -d $dirFullName ]]; then
			red 'dir not exist.'
			continue
		fi
		openCMD=${openCMD}"--tab -e 'bash -c \"cd ${dirFullName}; exec bash\"' "
	done < $iniFile
	bash -c "gnome-terminal $openCMD--maximize"
	xdotool key ctrl+alt+s

elif [[ $1 == 'up' ]]; then
	cat $iniFile | while read line; do
		if [[ ${line:0:1} == '#' ]]; then
			continue
		fi
		yellow "up -> ${line}"
		push $line
	done
elif [[ $1 == 'down' ]]; then
	cat $iniFile | while read line; do
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

# exit 0
