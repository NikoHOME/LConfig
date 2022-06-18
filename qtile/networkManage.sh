#!/bin/sh

DIALOG_RESULT=$(nmcli device status | grep PLAY);
if [ "$DIALOG_RESULT" = "" ];
then
    exec nmcli con up PLAY
else
    exec nmcli con down PLAY  
fi