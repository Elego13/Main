#!/usr/bin/env bash
#evan Jurdan
curr=$(pwd)


echo "you are currently " $curr

if [[ "$curr" == *"/Desktop" ]];then
    y="y"
else
    cont=true
    while $cont
    do
        echo "you are not in the desktop do you want to continue?(y/n)"
        read ans
        if ["$ans" == "y"];then
            cont=false
        elif ["$ans" == "n"];then
            exit 1
        elif [ "$ans" == "quit" ]; then 
            echo "bye mate"
            exit 1
        else
            echo "not a valid answer"
        fi
    done

fi

 cont2=true
while $cont2
do

    echo -n "Please enter file path: "
    read pat

    if [ "$pat" == "quit" ]; then 
        echo "bye mate"
        exit 1
    elif [ -f "$pat" ]; then
        ln -s $pat $curr
        echo "link created in $curr"
        echo ''
        cout=$(find $curr -type l | wc -l)

        echo "found $cout symbolic link(s)"

        echo $(find $curr -type l)

        echo $(readlink $(find $curr -type l))
    else
        echo "$pat does not exist"
    fi
done
