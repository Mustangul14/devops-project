#!/usr/bin/env python3
"""
sysinfo.py
Afișează periodic informații despre sistem: OS, CPU, memorie, disc și rețea.
"""

import platform
import psutil
import time
from datetime import datetime
import shutil
import socket

# Intervalul (secunde) — poate fi schimbat prin variabila de mediu INTERVAL
import os
INTERVAL = int(os.getenv("INTERVAL", "5"))

def get_ip():
    """Returnează adresa IP locală (non-loopback)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "N/A"

def show_info():
    print("=== ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), " ===")
    print("OS:", platform.system(), platform.release())
    print("CPU cores:", psutil.cpu_count(logical=True))
    print(f"CPU usage: {psutil.cpu_percent()}%")
    mem = psutil.virtual_memory()
    print(f"Memory usage: {mem.percent}% ({mem.used/1e9:.1f} GB / {mem.total/1e9:.1f} GB)")
    disk = psutil.disk_usage("/")
    print(f"Disk usage: {disk.percent}% ({disk.used/1e9:.1f} GB / {disk.total/1e9:.1f} GB)")
    print("Local IP:", get_ip())
    print()

if __name__ == "__main__":
    while True:
        show_info()
        time.sleep(INTERVAL)


