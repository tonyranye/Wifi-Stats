# Automatic monitoring using APScheduler

import time
import os

from apscheduler .schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from speedTest import speedTest
from datetime import datetime

def start_auto_tracker(interval_hours=2):
    schedular = BackgroundScheduler()
    
    schedular.add_job(
        speedTest,
        'interval',
        hours=interval_hours,
        next_run_time=datetime.now(), # run immediately on start
        args=[True]
    )
    
    schedular.start()
    
    print(f"\nAuto tracker started --- running every {interval_hours} hours")
    print("Press Ctrl + C to stop \n")
    
    try:
        while True:
            time.sleep(60)
            
    except (KeyboardInterrupt, SystemExit):
        schedular.shutdown()
        print("\nAuto tracker stopped.")
    
    
def prompt_interval():
    print("\nHow often would you like to run the speed test?")
    print("1. Every 1 hour")
    print("2. Every 2 hours")
    print("3. Every 6 hours")
    print("4. Custom interval")
    
    choice = int(input("\nENTER CHOICE HERE: "))
    
    if choice == 1:
        start_auto_tracker(1)
    elif choice == 2:
        start_auto_tracker(2)
    elif choice == 3:
        start_auto_tracker(6)
    elif choice == 4:
        hours = float(input("Enter interval in hours: "))
        start_auto_tracker(hours)
    else:
        print("Invalid choice, defaulting to 2 hours")
        start_auto_tracker(2)