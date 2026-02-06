import subprocess
import json
import time

import os


def log_to_csv(date, time, isp, public_ip, local_ip, ping_ms, download_speed, upload_speed, server_location, jitter_ms):
    os.makedirs("logs", exist_ok=True)
    with open("logs/speedtest_log.csv", "a") as f:
        
        if os.path.getsize("logs/speedtest_log.csv") == 0:
            f.write("Date,Time,ISP,Public IP,Local IP,Ping (ms),Download (Mbps),Upload (Mbps),Server Location,Jitter (ms)\n")
        f.write(f'{date},{time},{isp},{public_ip},{local_ip},{ping_ms},{download_speed},{upload_speed},"{server_location}",{jitter_ms}\n')


def createNewTracker():
    pass