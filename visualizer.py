# Matplotlib charts from the csv log

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

LOG_PATH = "logs/speedtest_log.csv"


# loads the csv data into a numpy dataframe
def load_logs():
    if not os.path.exists(LOG_PATH):
        print("No log file found. Run a speed test first.")
        
    df = pd.read_csv(LOG_PATH)
    
    if df.empty:
        print("\nNo Data found in log file")
        return None
    
    # Need to convert string coulmns "Date" and "Time" into a single proper datetime object
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df.sort_values('Datetime')
    return df
    

def show_summary(df):
    print("\n ---------------- SPEED TEST SUMMARY ----------------")
    print(f"Total tests loged:          {len(df)}")
    print(f"Avg Download Speed:         {df['Download (Mbps)'].mean():.2f} Mbps ")
    print(f"Avg Upload Speed:           {df['Upload (Mbps)'].mean():.2f} Mbps")
    print(f"Avg Ping:                   {df['Ping (ms)'].mean():.2f} ms")
    print(f"Best Download               {df['Download (Mbps)'].max():.2f} Mbps")
    print(f"Worst Download              {df['Download (Mbps)'].min():.2f} Mbps")
    print(f"Best Ping                   {df['Ping (ms)'].max():.2f} ms")
    print(f"Worst Ping                  {df['Ping (ms)'].min():.2f} ms")
    print("------------------------------------------------------")



def plot_speeds(df):
    fig, axes = plt.subplots(3, 1, figsize=(12,10))
    plt.subplots_adjust(hspace=0.6)
    fig.suptitle('Network Performance over time', fontsize=16, fontweight='bold')
    
    # Download speed 
    axes[0].plot(df['Datetime'], df['Download (Mbps)'], color= '#2196F3', linewidth=2, marker='o', markersize=4)
    axes[0].fill_between(df['Datetime'], df['Download (Mbps)'], alpha=0.1, color='#2196F3')
    axes[0].set_title('Download Speed')
    axes[0].set_ylabel('Mbps')
    axes[0].grid(True, alpha=0.3)
    
    # Upload speed
    axes[1].plot(df['Datetime'], df['Upload (Mbps)'], color='#5DCA03', linewidth=2, marker='o', markersize=4)
    axes[1].fill_between(df['Datetime'], df['Upload (Mbps)'], alpha=0.1, color='#5DCA03')
    axes[1].set_title('Upload Speed')
    axes[1].set_ylabel('Mbps')
    axes[1].grid(True,alpha=0.3)
    
    # Ping
    axes[2].plot(df['Datetime'], df['Ping (ms)'], color='#FF5722', linewidth=2, marker='o', markersize=4)
    axes[2].fill_between(df['Datetime'], df['Ping (ms)'], alpha=0.1, color='#FF5722')
    axes[2].set_title('Ping (ms)')
    axes[2].set_ylabel('ms')
    axes[2].grid(True, alpha=0.3)
    
    
    # format x-axis dates on all subplots
    for ax in axes:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %H:%M'))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()


def visualize():
    df = load_logs()
    if df is None:
        return
    
    show_summary(df)
    
    print("\nWould you like to view the charts? (Y/n): ", end="")
    choice = input().strip().lower()
    if choice == 'y' or choice == '':
        plot_speeds(df)



