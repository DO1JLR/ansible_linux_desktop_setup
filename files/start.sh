#!/bin/sh
i3s=$(i3-msg -t get_workspaces)

if [ '[]' == "$i3s" ];  then
  echo "i3 not running"
else
  if [ ! -f /tmp/autostart ]; then
    tmux new-session -s i3-pannel -n etc -d 'sleep 5; /usr/bin/nm-applet --no-agent'
    tmux new-window  -t i3-pannel:1 -n nextcloud  'sleep 30; /usr/bin/nextcloud'
    touch /tmp/autostart
  else
    ddate
  fi
fi

