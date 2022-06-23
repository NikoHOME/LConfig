#!/bin/sh

BEST_RESULT="$(nmcli --fields SSID device wifi list |head -2 | tail -1)";
CURRENT="$(nmcli --fields CONNECTION device status | head -2 | tail -1)";
BEST_RESULT="$(echo -e " \t$BEST_RESULT\t " | sed 's/^[ \t]//;s/[ \t]$//')";
CURRENT="$(echo -e " \t$CURRENT\t " | sed 's/^[ \t]//;s/[ \t]$//')";
echo $BEST_RESULT;
echo $CURRENT;
DIALOG_RESULT=$(nmcli --fields STATE device status | grep -w connected);
echo $DIALOG_RESULT;
if [ "$DIALOG_RESULT" = "" ];
then
    exec nmcli con up "$BEST_RESULT" 
else
    exec nmcli con down "$CURRENT" 
fi
