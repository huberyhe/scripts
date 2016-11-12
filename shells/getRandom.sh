#!/bin/bash

function getRandom ()
{
	retArray=();
	count=$1;
	have=0;
	while (($have<$count)); do
		ret=$(($RANDOM%14));
		if [[ "${retArray[@]/$ret/}" != "${retArray[@]}" ]]; then
			continue;
		else
			retArray[$have]=$ret;
			have=$(($have+1));
			echo $ret;
		fi
	done

	# return retArray;

}

getRandom 4