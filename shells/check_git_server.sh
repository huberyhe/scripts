#!/bin/bash

parse_json(){

echo $1 | sed 's/.*'$2':\ \([^,}]*\).*/\1/'

}

nslookupIP=$(nslookup hyc171819.vicp.cc 118.118.118.118 | grep Address | sed -n '2p' | awk '{print $2}')
publicIP=$(curl 178.62.234.75:16000/api/v1.0 | grep remote | awk '{print $2}' | sed 's/\"//g')

echo "nslookupIP = $nslookupIP"
echo "publicIP = $publicIP"