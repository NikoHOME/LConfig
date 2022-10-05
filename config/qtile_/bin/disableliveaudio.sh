filename='/home/linus/.config/qtile/bin/pactl-devices.txt'
while read p; do 
    pactl unload-module "$p"
done < "$filename"
: > $filename