#!/usr/bin/env bash

currentVolume=$(pactl list sinks | grep "Volume" | sed -n 1p | cut -d "/" -f2 | sed "s/%//")

if [ $currentVolume -lt 100 ]
then
    sh -c "pactl set-sink-volume 0 +5%"
fi
