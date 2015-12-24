#!/bin/bash

nslookupIP=$(nslookup hyc171819.vicp.cc 118.118.118.118 | grep Address | sed -n '2p' | awk '{print $2}')
# publicIP=$(curl 178.62.234.75:16000/api/v1.0 | grep remote | awk '{print $2}' | sed 's/\"//g')
publicIP=$(curl -s http://www.dicovi.com/shows/git?ns=$nslookupIP | sed 's/.*"remote":"\([^",}]*\).*/\1/')

echo "nslookupIP = $nslookupIP"
echo "publicIP = $publicIP"