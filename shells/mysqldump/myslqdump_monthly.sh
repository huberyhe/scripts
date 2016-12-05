#!/bin/bash

BKDIR='/home/hubery/dbBac/monthly'
USER='backup'
PASS='bbk855'
DBNAME='iksdb3'
MAXBK=12

# GRANT USAGE ON *.* TO 'backup'@'%' IDENTIFIED BY PASSWORD '*3EA2433A8A62A5AD014AA812DC097D3D2C5B1016'
# GRANT SELECT, LOCK TABLES, SHOW VIEW, TRIGGER ON `iksdb3`.* TO 'backup'@'%'

mysqldump -u$USER -p$PASS $DBNAME > $BKDIR/$DBNAME-`date +%y%m%d%H%M`.sql

bkCount=`ls -1t $BKDIR | wc -l`
echo "$bkCount files."

if [[ $bkCont -lt $MAXBK ]] ; then
    echo "too many, delete old one to storage space"
    oldOne=`ls -1t $BKDIR | tail -n 1`
    rm -f "$BKDIR/$oldOne"
fi

