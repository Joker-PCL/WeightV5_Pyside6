#!/bin/bash

while true
do
    echo -ne "\n"
    echo -ne "<<< Weight 10s' >>>\n"
    for(i=20; i>=0; i--)
    do
        echo -ne "Start in $i seconds \r"
        sleep 1
    done

    echo -ne "\n"
    
    cd /home/weight/Desktop/polipharm
    source env/bin/activate
    python3 main.py
done