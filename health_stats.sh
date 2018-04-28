

#!/bin/bash

#gives the cpu load average
echo "CPU Load Average: " `uptime`
#logging the cpu Usage
#| sed -n 1'p'
#while true; do uptime >>uptime.csv; awk -F, '{OFS=",";print $1,$4,$5,$6}' uptime.csvs> outfile.csv ; sleep 10; done
T=1
htresh=0.03
vhtresh=0.06
count=0
while [ true ]
do
  uptime >>uptime.csv
  awk -F, '{OFS=",";print $1,$4,$5,$6}' uptime.csv> outfile.csv

  usage=$( tail -n1 outfile.csv | cut -d' ' -f9 )
  usage2=${usage%?}
  #usage2=0.2
  timestamp=$( tail -n1 outfile.csv | cut -d',' -f1 )
  #echo "Usage: " "$usage2"
  #if (( $(awk 'BEGIN {print ("'$usage'" >= "'$htresh'")}') ));
  #if (( $(echo "$usage > $htresh" | bc -l) ));
  if [ $(echo "$usage2 > $htresh" | bc) -ne 0 ]
  then
    echo "HIGH CPU Usage"
    msg="HIGH CPU Usage"
    echo "$timestamp, $msg, $usage2" >> logfile.csv

  else
    echo "Normal CPU Usage"
    #msg="Normal CPU Usage"
    #echo "$timestamp, $msg, $usage2" >> logfile.csv
  fi
  highusage=$( tail -n1 outfile.csv | cut -d',' -f3 )
  #echo "VH Usage: "  "$highusage"
  #if (( $(echo "$highusage > $vhtresh" | bc -l) ));
  if [ $(echo "$highusage > $vhtresh" | bc) -ne 0 ]
  then
    echo "VERY HIGH CPU Usage"
    msg2="VERY HIGH CPU Usage"
    echo "$timestamp, $msg1, $highusage" >> logfile.csv
  fi
  sleep $T
  #x=$(( $x + 1 ))
done
