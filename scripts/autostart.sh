#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

keybLayout=$(setxkbmap -v | awk -F "+" '/symbols/ {print $2}')

#starting utility applications at boot time
# nitrogen --restore &
~/.fehbg &

picom --config $HOME/.config/picom/picom.conf &
# picom --config $HOME/.config/picom/picom-pijulius.conf &
# picom --config $HOME/.config/picom/picom-jonaburg.conf &

dunst -conf /home/mateo/.config/dunst/dunstrc.nord &
# dunst -conf /home/mateo/.config/dunst/dunstrc.catppuccin &
# dunst -conf /home/mateo/.config/dunst/dunstrc.monokai &
# dunst -conf /home/mateo/.config/dunst/dunstrc.rosepine &

lxsession &

#Optional
# numlockx on &
run xfce4-power-manager &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#systray(optional)
# run volumeicon &
run nm-applet &
# run pamac-tray &
blueberry-tray &

