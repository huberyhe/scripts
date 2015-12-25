#!/bin/bash
Resettem=$(tput sgr0)
nslookupIP=$(nslookup hyc171819.vicp.cc 118.118.118.118 | grep Address | sed -n '2p' | awk '{print $2}')
# publicIP=$(curl 178.62.234.75:16000/api/v1.0 | grep remote | awk '{print $2}' | sed 's/\"//g')
publicIP=$(curl -s http://www.dicovi.com/shows/git?ns=$nslookupIP | sed 's/.*"remote":"\([^",}]*\).*/\1/')

echo "nslookupIP = $nslookupIP"
echo "publicIP = $publicIP"

if [[ $nslookupIP -eq $publicIP ]]; then
	#statements
	echo -e '\E[33m' "hyc171819.vicp.cc is all right." $Resettem "Check completed!"
else
	echo -e '\E[33m' "hyc171819.vicp.cc is error. Right IP for git server is " $publicIP $Resettem "Check completed!"
fi