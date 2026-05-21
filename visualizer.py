# Matplotlib charts from the csv log

import pandas as pd
import matplotlib as plt
import matplotlib.dates as mdates
import os
from main import *

LOG_PATH = "logs/speedtest_log.csv"

def load_logs():
    if not os.path.exists(LOG_PATH):
        print("No log file found. Run a speed test first.")
        
    df = pd.read_csv(LOG_PATH)
    
    if df.empty:
        print("\nNo Data found in log file")
        return None
    
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df.sort_values('Datetime')
    
    
    return df
    




def plot_speeds():
    pass

def show_summary(df):
    pass

def visualize():
    load_logs()



