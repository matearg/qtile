#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

keybLayout=$(setxkbmap -v | awk -F "+" '/symbols/ {print $2}')

#starting utility applications at boot time
nitrogen --restore &
picom --config $HOME/.config/picom/picom.conf &
dunst -conf /home/mateo/.config/dunst/dunstrc &
lxsession &

#Optional
# numlockx on &
# run xfce4-power-manager &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#systray(optional)
# run volumeicon &
# run nm-applet &
# run pamac-tray &
# blueberry-tray &
