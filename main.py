import time
import os 

import subprocess
import json



# Speed test

def speedTest():
    try:
        print("FINDING BEST SERVER...")
        print("BEGINnING SPEED TEST...")
        
        result = subprocess.run(
           ['speedtest', '--format=json', '--accept-license', '--accept-gdpr'],
           capture_output=True,
           text=True,
           timeout=60
        )
    
        ping_ms = st.results.ping
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        
        # results
        
        print("\n--------------------------     SPEED TEST RESULTS     --------------------------")
        print(f"PING: {ping_ms} MS")
        print(f"DOWNLOAD SPEED: {download_speed:.2f}")
        print(f"UPLOAD SPEED: {upload_speed:.2f}")
        

def welcome():
    os.system("color B")
    os.system("title Speedtest - by Tony Akinniranye")
    
    # time.sleep(1.5)
    print("\n**********************************************************************")
    print("                     Network Speed Test\n")
    print("Developed by Tony Akinniranye ")
    print("**********************************************************************")
    # time.sleep(1.5)
    mainMenu()
    
    
def mainMenu():
    print("\n\n\nWould you like to perform a speed test now or setup a automatic speed tester?")
    print("1. Start speed test now.")
    print("2. Start automatic speed tester")
    # time.sleep(1.0)
    menuChoice = int(input("\n ENTER CHOICE HERE: "))
    if menuChoice == 1:
        speedTest()
        

if __name__ == "__main__":
    welcome()
    
    