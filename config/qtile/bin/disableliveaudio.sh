filename='pactl-devices.txt'
while read p; do 
    pactl unload-module "$p"
done < "$filename"
: > pactl-devices.txt