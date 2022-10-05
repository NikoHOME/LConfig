#!/bin/bash

MICROPHONE="alsa_input.pci-0000_04_00.6.HiFi__hw_acp__source"
SPEAKERS="alsa_output.pci-0000_04_00.6.HiFi__hw_Generic_1__sink"
<<<<<<< Updated upstream
: > pactl-devices.txt
# Create the null sinks
# virtual1 gets your audio source (mplayer ...) only
# virtual2 gets virtual1 + micro
pactl load-module module-null-sink sink_name=VirtualOutput sink_properties=device.description="VirtualOutput" >> pactl-devices.txt
pactl load-module module-null-sink sink_name=VirtualOutputInput sink_properties=device.description="VirtualOutputInput" >> pactl-devices.txt

# Now create the loopback devices, all arguments are optional and can be configured with pavucontrol
pactl load-module module-loopback source=VirtualOutput.monitor sink=$SPEAKERS >> pactl-devices.txt
pactl load-module module-loopback source=VirtualOutput.monitor sink=VirtualOutputInput >> pactl-devices.txt
pactl load-module module-loopback source=$MICROPHONE sink=VirtualOutputInput >> pactl-devices.txt
=======
OUTPATH="/home/linus/.config/qtile/bin/pactl-devices.txt"
: > $OUTPATH
# Create the null sinks
# virtual1 gets your audio source (mplayer ...) only
# virtual2 gets virtual1 + micro
pactl load-module module-null-sink sink_name=VirtualOutput sink_properties=device.description="VirtualOutput" >> $OUTPATH
pactl load-module module-null-sink sink_name=VirtualOutputInput sink_properties=device.description="VirtualOutputInput" >> $OUTPATH

# Now create the loopback devices, all arguments are optional and can be configured with pavucontrol
pactl load-module module-loopback source=VirtualOutput.monitor sink=$SPEAKERS >> $OUTPATH
pactl load-module module-loopback source=VirtualOutput.monitor sink=VirtualOutputInput >> $OUTPATH
pactl load-module module-loopback source=$MICROPHONE sink=VirtualOutputInput >> $OUTPATH
>>>>>>> Stashed changes
