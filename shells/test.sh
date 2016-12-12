#!/bin/bash
var='1234'
if [ -n "$(echo $var| sed -n "/^[0-9]\+$/p")" ]; then
	echo 'ts'
fi

arrayTest=(
'111'
'222'
'333'
'444'
'555'
'666'
'777'
'888'
'999'
'000'
)

for i in ${arrayTest[@]} ; do
    echo $i
done
