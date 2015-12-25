#!/bin/bash
Resettem=$(tput sgr0)
serverDomainName="hyc171819.vicp.cc"
echo "Checking $serverDomainName..."

nslookupIP=$(nslookup $serverDomainName 118.118.118.118 | grep Address | sed -n '2p' | awk '{print $2}')
echo "Got nslookup IP: $nslookupIP"
# publicIP=$(curl 178.62.234.75:16000/api/v1.0 | grep remote | awk '{print $2}' | sed 's/\"//g')
publicIP=$(curl -s http://www.dicovi.com/shows/git?ns=$nslookupIP | sed 's/.*"remote":"\([^",}]*\).*/\1/')
echo "Got public IP: $publicIP"
printf "\n"

if [[ $nslookupIP == $publicIP ]]; then
	#statements
	echo -e '\E[33m' "$serverDomainName is all right." $Resettem
else
	echo -e '\E[31m' "$serverDomainName is error. Right IP for GIT server is" $publicIP $Resettem
fi

echo "Check completed!"