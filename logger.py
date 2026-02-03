import subprocess
import json
import time

import os


def log_to_csv(date, time, public_ip, ping_ms, download_speed, upload_speed):
    os.makedirs("logs", exist_ok=True)
    with open("logs/speedtest_log.csv", "a") as f:
        
        if os.path.getsize("logs/speedtest_log.csv") == 0:
            f.write("Date,Time,Public IP,Ping (ms),Download (Mbps),Upload (Mbps)\n")
        f.write(f"{date},{time},{public_ip},{ping_ms},{download_speed},{upload_speed}\n")


def createNewTracker():
    pass