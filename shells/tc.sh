#!/bin/bash
if [[ `whoami` != 'root' ]]; then
	echo "Permission Denied."
	exit 1
fi
modprobe sch_netem
modprobe sch_htb
tc qdisc del dev eth0 root
tc qdisc add dev eth0 root handle 1: htb
tc class add dev eth0 parent 1: classid 1:1 htb rate 20mbit
tc filter add dev eth0 protocol ip parent 1:0 prio 1 handle 10 fw flowid 1:1
iptables -t mangle -A POSTROUTING -o eth0 -j MARK --set-mark 10