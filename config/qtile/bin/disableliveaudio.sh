<<<<<<< Updated upstream
filename='pactl-devices.txt'
while read p; do 
    pactl unload-module "$p"
done < "$filename"
: > pactl-devices.txt
=======
filename='/home/linus/.config/qtile/bin/pactl-devices.txt'
while read p; do 
    pactl unload-module "$p"
done < "$filename"
: > $filename
>>>>>>> Stashed changes
