#!/bin/bash
orayuser='hyc171819'
oraypass='hjhchf910215'
oraydomain='hyc171819.vicp.cc'
realip=`curl http://ddns.oray.com/checkip | cut -d' ' -f 6 | cut -d'<' -f 1`
currentip=`nslookup $oraydomain | tail -2 | head -1 | cut -d' ' -f 2`
theurl="http://$orayuser:$oraypass@ddns.oray.com/ph/update?hostname=$oraydomain&myip=$realip"
if [ "$realip" = "$currentip" ]; then
	exit 0
else
	curl "$theurl"
	echo
fi
