#!/bin/bash

# default no(1)
function askNY ()
{
	ret=0
	timeout=5
	while
		echo -n "$1[y/N]"
	do
		read -t $timeout ans
		if [[ -z $ans ]]; then
			ret=1
			break
		elif [[ "$ans"x = "y"x || "$ans"x = "Y"x ]]; then
			ret=0
			break
		elif [[ "$ans"x = "n"x || "$ans"x = "N"x ]]; then
			ret=1
			break
		else
			continue
		fi
	done
	return $ret
}
# default yes(0)
function askYN ()
{
	ret=0
	timeout=5
	while
		echo -n "$1[Y/n]"
	do
		read -t $timeout ans
		if [[ -z $ans ]]; then
			ret=0
			break
		elif [[ "$ans"x = "y"x || "$ans"x = "Y"x ]]; then
			ret=0
			break
		elif [[ "$ans"x = "n"x || "$ans"x = "N"x ]]; then
			ret=1
			break
		else
			continue
		fi
	done
	return $ret
}

iptablesFile='/etc/iptables.rule'
if [[ -f $iptablesFile ]] && askYN "Already configured, restore(Y) or continue(N)?" ; then
	echo "Already configured, restore."
else
	echo "Start to configure and save rules."
fi