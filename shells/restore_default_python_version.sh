#!/bin/bash

if [[ $USER != 'root' ]];then
    echo "Must be run as root!"
    exit 1
fi

echo "restore to default version..."
mv /usr/bin/python /usr/bin/python.new
ln -s /usr/bin/python2 /usr/bin/python
echo "Done."

echo "restore to new version, continue with enter..."
read
mv /usr/bin/python.new /usr/bin/python
echo "Done."
