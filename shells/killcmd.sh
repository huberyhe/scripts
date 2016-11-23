#!/bin/bash
script=$0
debug=0

function usage()
{
	if [[ $debug -eq 0 ]]; then
		echo 'pwd'
	else
		echo "usage: bash $script <port>"
		# echo "    type: l/s (l for ikstcplogin, s for ikstcpserver)"
		# echo "    port: login or server port"
	fi

}

if [[ "$#" -ne "1" ]]; then
	usage
	exit 1
fi

port=$1
service_type=0
service_ver=0
if [[ $port =~ ^1[1-9]{2}00$ ]]; then
	service_type='l'
	service_ver=4
elif [[ $port =~ ^1[1-9]{2}12$ ]]; then
	service_type='s'
	service_ver=4
elif [[ $port =~  ^[1-9]{2}00$ ]]; then
	service_type='l'
	service_ver=3
elif [[ $port =~ ^[1-9]{2}12$ ]]; then
	service_type='s'
	service_ver=3
else
	usage
	exit 1
fi

if [[ $service_type == 'l' ]]; then
	echo "ps ax | grep IKSTCP[L]ogin${service_ver} | grep -v respawnandlog.sh | grep ' $port -d ' | awk '{print \$1}' | tee /dev/stderr | xargs sudo kill"
elif [[ $service_type == 's' ]]; then
	echo "ps ax | grep IKSTCP[s]erver${service_ver} | grep -v respawnandlog.sh | grep ' $port ' | awk '{print \$1}' | tee /dev/stderr | xargs sudo kill"
else
	usage
	exit 1
fi

