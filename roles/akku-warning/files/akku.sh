#!/bin/bash

power="$((`cat /sys/class/power_supply/BAT0/energy_now` * 100 / `cat /sys/class/power_supply/BAT0/energy_full_design`))"

if (( $power < 25 && $power > 15 )); then
    zenity --warning --title="Low Power" --text="$power percent remaining.\n\nPlease recharge soon!" --display=:0.0
elif (( $power < 15 && $power > 9 )); then
    zenity --warning --title="Low Power" --text="$power percent remaining.\n\nPlease recharge soon!" --display=:0.0
    mpv /opt/low_battery.mkv -fs --volume 130 --start 00:00:18
elif (( $power < 9 && $power > 5 )); then
    zenity --warning --title="Critical Power" --text="$power percent remaining.\n\nPlease recharge NOW!" --display=:0.0
elif (( $power < 5 )); then
    zenity --warning --title="Critical Power" --text="$power percent remaining.\n\nRECHARGE!\nNOW!" --display=:0.0
fi
