#!/bin/bash

START_DATE=170101
END_DATE=170110

for (( DATE=$START_DATE ; $DATE <= $END_DATE ; DATE=`date -j -v+1d -f %y%m%d $DATE +%y%m%d` )) ; do
   echo $DATE
   scrapy crawl boj -a date=$DATE
done
