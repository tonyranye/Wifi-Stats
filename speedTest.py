import time

import subprocess
import json


from logger import log_to_csv
from datetime import datetime

def speedTest():
    
    print("\nBEGINING SPEED TEST...")
    
    
    result = subprocess.run(
       ['ookla-speedtest-1.2.0-win64\speedtest.exe', '--format=json', '--accept-license', '--accept-gdpr'],
       capture_output=True,
       text=True
    )

    data = json.loads(result.stdout)
    
    now = datetime.now()
    date = now.strftime("%Y-%m-%d") # ex 2024-02-03
    time_hr = now.strftime("%H:%M:%S") # ex 14:35:22
    isp = data['isp']
    public_ip = data['interface']['externalIp']
    
    server_location = data['server']['location']
    
    
    
    jitter_ms = data['ping']['jitter']
        
    import socket
    local_ip = socket.gethostbyname(socket.gethostname())
   
    ping_ms = data['ping']['latency']
    download_speed = data['download']['bandwidth'] * 8 / 1_000_000  # Convert to Mbps
    upload_speed = data['upload']['bandwidth'] * 8 / 1_000_000

    # results
    
    print("\n -------------------------     SPEED TEST RESULTS     --------------------------")
    print(f'| PUBLIC IP: {public_ip}')
    print(f'| LOCAL IP: ***********')
    print(f"| SERVER LOCATION: {server_location}")
    print(f'| DATE {date}')
    print(f"| TIME {time_hr}\n|")
    
    print("| ")
    print(f"| PING: {ping_ms:.2f} MS")
    print(f"| JITTER: {jitter_ms:.2f} MS")
    print(f"| DOWNLOAD SPEED: {download_speed:.2f} Mbp/s")
    print(f"| UPLOAD SPEED: {upload_speed:.2f} Mbp/s")
    
    print(f"| Internet Service Provider: {isp}\n|")
    print("| saved to log/speedtest_logs.csv")
    print(" -------------------------------------------------------------------------------")

    
    log_to_csv(date, time_hr, isp, public_ip, local_ip, ping_ms, download_speed, upload_speed, server_location, jitter_ms)
    
    
    loop = True
    while loop:
      end = (input("\nPerform Another test? (Y/n): ")) 
      if end == "y" or end == "Y":
         speedTest()
         loop = False
         
      elif end == "n" or end == "N":
         print("exiting...")
         loop = False
         return
      else:
         print("invalid entry, try again")
         time.sleep(0.8)
         continue