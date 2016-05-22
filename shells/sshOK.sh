#!/bin/bash
$(ssh www@218.66.216.118)
until [ $? == '0' ]
do
	echo "ssh done"
	$(ssh www@218.66.216.118)
done
echo `date +"%Y%m%d%0k%M%S"` > sshOK.log