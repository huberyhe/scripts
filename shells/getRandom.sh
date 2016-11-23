#!/bin/bash

function getRandom ()
{
	retArray=();
	count=$1;
    out=$2
	have=0;
	while (($have<$out)); do
		ret=$(($RANDOM%$count));
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

getRandom 14 2
