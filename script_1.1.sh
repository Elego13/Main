#!/bin/bash


tester(){
    echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

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
