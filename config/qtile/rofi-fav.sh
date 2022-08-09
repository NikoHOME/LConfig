#!/bin/sh

DIALOG_RESULT=$(echo -e 'cancel\nfirefox\ncode\nthunar\ndiscord\nsteam' | rofi -dmenu -i -p "   Favourite " -hide-scrollbar -tokenize -lines 9 -eh 1 -width 40 -location 8 -xoffset 170 -yoffset 70 -padding 30 -disable-history -font "JetBrainsMono Nerd Font 18")

#echo "This result is : $DIALOG_RESULT"
sleep 0.5;

if [ "$DIALOG_RESULT" = "firefox" ];
then
    exec firefox

elif [ "$DIALOG_RESULT" = "code" ];
then
    exec code

elif [ "$DIALOG_RESULT" = "thunar" ];
then
    exec thunar

elif [ "$DIALOG_RESULT" = "discord" ];
then
    exec discord
elif [ "$DIALOG_RESULT" = "steam" ];
then
    exec steam-runtime
fi
