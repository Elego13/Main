#!/bin/bash


tester(){
    wget --spider $1


    if [ $? -eq 0 ]; then
        echo "Online"
    else
        echo "Offline"
    fi
}

#def getit():
IP=$(/sbin/ip route | awk '/default/ { print $3 }')
remote=$(8.8.8.8)
echo $IP

tester $IP
tester $remote
