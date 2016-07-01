#!/bin/bash
var='1234'
if [ -n "$(echo $var| sed -n "/^[0-9]\+$/p")" ]; then
	echo 'ts'
fi
