#!/bin/bash

#Monitoring the free fs space disk

FU=$(df -h | egrep -v "Filesystem|tmpfs" | grep sda1 | awk '{print $5}' | tr -d %)

TO="_name@gmail.com"

if [[ $FU -ge 80 ]]
then
        echo "Warning, disk space is running low - $FU %" | mail -s "Disk Space Alert !" $TO

else
        echo "Working fine"
fi
