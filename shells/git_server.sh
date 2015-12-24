#!/bin/bash
nmap_res=$(nmap hyc171819.vicp.cc -p 22|grep ssh|awk '{print $2}')
git_status=${nmap_res:-down}
pid=$$
now=`TZ=":Asia/Chongqing" date +"%Y%m%d %0k:%M:%S %Z"`
now_int=`date +"%Y%m%d%0k%M%S"`
last_status=$(tail -n 1 gits.txt|awk '{print $2}')
echo $last_status
echo $git_status
if [ "$git_status" != "$last_status" ]
then
	nmap_res=$(nmap hyc171819.vicp.cc -p 22|grep ssh|awk '{print $2}')
	git_status=${nmap_res:-down}
	if [ "$git_status" != "$last_status" ]
	then
		echo "$now_int $git_status $pid" >> gits.txt
		echo -e "STATUS CHANGED!\nTime: $now.\nGit server hyc171819.vicp.cc was $git_status."|mail -s "git server status" -a gits.txt www@hubery-VirtualBox
		echo "$now_int $git_status $pid"
	fi
fi

