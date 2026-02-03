import time
import os 

from speedTest import *
from logger import *


def welcome():
    os.system("color B")
    os.system("title Speedtest - by Tony Akinniranye")
    
    # time.sleep(1.5)
    print("************************************************************")
    print("                     Network Speed Test\n")
    print("Developed by Tony Akinniranye ")
    print("************************************************************")
    # time.sleep(1.5)
    mainMenu()

    return
    
    
def mainMenu():
    print("\nWhat Would You Like To Do?\n")
    print("1. Begin Speed test")
    print("2. Begin automatic speed test tracker")
    print("3. View internet details")
    print("0. EXIT ")

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
    
    
    
    
    
    