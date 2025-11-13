#!/usr/bin/env bash
# sysinfo.sh - afișează periodic informații despre sistem
# intervalul se poate seta prin variabila de mediu INTERVAL (secunde)
INTERVAL=${INTERVAL:-5}

# buclă infinită
while true; do
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="
  # informații OS
  if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "Distro: $NAME $VERSION"
  else
    uname -a
  fi

  # CPU summary
  if command -v lscpu >/dev/null 2>&1; then
    lscpu | awk -F: '/Model name|Socket|CPU\(s\)/{print $1": "$2}'
  fi

  # memorie
  echo "Mem:"
  free -h 2>/dev/null || vm_stat 2>/dev/null || true

  # disk usage (root)
  echo "Disk (/:)"
  df -h / | sed -n '1,2p'

  # rețea - IP public/local
  echo "Network interfaces:"
  ip -4 addr show 2>/dev/null | awk '/inet /{print $2 " -> " $NF}' || ifconfig 2>/dev/null || true

  echo ""
  sleep "$INTERVAL"
done
