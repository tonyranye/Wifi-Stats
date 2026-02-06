import time
import os 

from speedTest import *
from logger import *


def welcome():
    os.system("color B")
    os.system("title Speedtest - by Tony Akinniranye")
    
    print("""
          
 __    __  ____  _____  ____        _____ ______   ____  ______  _____
|  |__|  ||    ||     ||    |      / ___/|      | /    ||      |/ ___/
|  |  |  | |  | |   __| |  | _____(   \_ |      ||  o  ||      (   \_ 
|  |  |  | |  | |  |_   |  ||     |\__  ||_|  |_||     ||_|  |_|\__  |
|  `  '  | |  | |   _]  |  ||_____|/  \ |  |  |  |  _  |  |  |  /  \ |
 \      /  |  | |  |    |  |       \    |  |  |  |  |  |  |  |  \    |
  \_/\_/  |____||__|   |____|       \___|  |__|  |__|__|  |__|   \___|
                                                                      
    """)
    time.sleep(1)
    print("Network Performance Scanner & Analyzer")
    time.sleep(0.2)
    print("Version 0.1 - Alpha")
    time.sleep(0.2)
    print("Developed by tonyranye")
    time.sleep(0.4)
    mainMenu()
    return
    
    
def mainMenu():
    print("\nWhat Would You Like To Do?\n")
    print("1. Begin Speed test")
    # print("2. Begin automatic speed test tracker")
    # print("3. View internet details")
    print("*. EXIT ")

    menuChoice = int(input("\nENTER CHOICE HERE: "))
    
    if menuChoice == 1:
        speedTest()
        
    if menuChoice == 2:
        # createNewTracker()
        pass
    if menuChoice == 0:
        print("EXITING...")
        
        
    

if __name__ == "__main__":
   welcome()
    
    
    
    
    
    