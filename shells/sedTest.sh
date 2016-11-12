#!/usr/bin/env bash
hda1=$(df -h | grep "/$" | awk '{print $1}')
echo $hda1
hda1c=$(echo $hda1 | sed 's:\/:\\\/:g')
sed -i '/^command\[check_hda1\]/s/\/dev\/vda1/'$hda1c'/g' nrpe.cfg | grep 'check_hda1'
