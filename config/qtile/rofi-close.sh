#!/bin/sh

DIALOG_RESULT=$(echo -e 'cancel\nexit qtile\nreboot\nshutdown\nhibernate\nsleep' | rofi -dmenu -i -p "   Computer  " -hide-scrollbar -tokenize -lines 4 -eh 1 -width 40 -location 8 -xoffset 170 -yoffset 70 -padding 30 -disable-history -font "JetBrainsMono Nerd Font 18")

#echo "This result is : $DIALOG_RESULT"
sleep 0.5;

if [ "$DIALOG_RESULT" = "exit qtile" ];
then
    exec qtile cmd-obj -o cmd -f shutdown
elif [ "$DIALOG_RESULT" = "reboot" ];
then
    exec reboot
elif [ "$DIALOG_RESULT" = "shutdown" ];
then
    exec shutdown -h now
elif [ "$DIALOG_RESULT" = "hibernate" ];
then
    exec systemctl hibernate
elif [ "$DIALOG_RESULT" = "sleep" ];
then
    exec systemctl suspend
fi