# Wifi-Stats - Network Speed Performance Scanner

A Windows system tray application that monitors your network performance, performs speed tests, and visualizes your internet quality over time.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)



## Screenshots
<img width="525" height="361" alt="image" src="https://github.com/user-attachments/assets/14fae398-6c43-4e10-b75f-7986c868a296" />
<br> <br>
<img width="761" height="446" alt="image" src="https://github.com/user-attachments/assets/4e10bc6b-fff1-420c-bf31-72a80de5a04e" />
<br><br>
<img width="399" height="207" alt="image" src="https://github.com/user-attachments/assets/c30561f3-c317-4185-a06a-70d69a8d9253" />
<br><br>
<img width="1189" height="883" alt="image" src="https://github.com/user-attachments/assets/ebc521f2-c37c-48c3-a39a-bf5c889a44be" />






## Features

### 🚀 Current Features (v0.1)
- **On-Demand Speed Testing**: Run network speed tests instantly from the command line
- **Automated Data Logging**: All test results saved to CSV with timestamps
- **ISP Tracking**: Records your Internet Service Provider information
- **Automatic Periodic Scanning**: Schedule speed tests at custom intervals
- **Detailed Metrics**: Captures ping, download speed, upload speed, and public IP
- **Data Visualization**: Interactive charts showing network performance over time
- **Historical Analysis**: Track trends and identify peak/low performance periods


### 🔮 Planned Features (System Tray Version)
- **Windows System Tray Integration**: Run silently in the background
- **Multi-Location Support**: Compare performance across different service providers
- **Performance Alerts**: Notifications when speeds drop below thresholds

## Installation

### Prerequisites
- Python 3.8 or higher
- Windows OS
- Ookla Speedtest CLI (included in repository)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/tonyranye/Wifi-Stats.git
   cd Wifi-Stats
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage

### Current Console Version

Run the program and select from the menu:
```
1. Begin Speed test - Runs a single speed test and logs results
2. Begin automatic speed test tracker - (Coming soon)
3. View internet details - (Coming soon)
0. EXIT - Close the application
```

### Data Storage

All speed test results are automatically saved to:
```
logs/speedtest_log.csv
```

CSV format:
```
Date,Time,ISP,Public IP,Local IP,Ping (ms),Download (Mbps),Upload (Mbps),Server Location,Jitter (ms)
2024-02-03,14:35:22,123.45.67.89,15.23,250.45,35.67
```

## Roadmap to System Tray Application

### Phase 1: GUI Framework ✨ (Next)
- [ ] Implement PyQt5 system tray icon
- [ ] Create context menu (Run Test, View Stats, Settings, Exit)
- [ ] Add tray notifications for test completion

### Phase 2: Automated Scanning 🔄
- [ ] Background thread for periodic scanning
- [ ] Configurable scan intervals (hourly, daily, custom)
- [ ] Start/Stop controls from tray menu

### Phase 3: Data Visualization 📊
- [ ] Speed over time line charts
- [ ] ISP comparison bar charts
- [ ] Peak/average/minimum statistics
- [ ] Exportable reports

### Phase 4: Advanced Features 🎯
- [ ] Performance threshold alerts
- [ ] Multiple location tracking
- [ ] Network quality scoring
- [ ] Historical trend analysis

### Phase 5: Distribution 📦
- [ ] Package as standalone .exe (PyInstaller)
- [ ] Windows startup integration
- [ ] Auto-update functionality
- [ ] Installer creation

## Project Structure

```
Wifi-Stats/
├── main.py                          # Entry point (console version)
├── speedTest.py                     # Speed test logic using Ookla CLI
├── logger.py                        # CSV logging functionality
├── ookla-speedtest-1.2.0-win64/    # Speedtest CLI executable
│   └── speedtest.exe
├── logs/                            # Generated speed test logs
│   └── speedtest_log.csv
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

### Future Structure (System Tray Version)
```
Wifi-Stats/
├── main.py                          # Tray app entry point
├── speedTest.py                     # Core speed test logic
├── logger.py                        # Enhanced logging + auto-scan
├── gui/
│   ├── tray_app.py                 # System tray implementation
│   ├── visualization.py            # Data charts and graphs
│   └── settings_dialog.py          # Configuration window
├── ookla-speedtest-1.2.0-win64/
├── logs/
├── assets/
│   └── icon.ico                    # Tray icon
└── requirements.txt
```

## Technical Details

### Dependencies
- **Ookla Speedtest CLI**: Official CLI tool for accurate speed measurements
- **Python Standard Library**: subprocess, json, datetime, os
- **Planned**: PyQt5 (GUI), matplotlib (visualization), pandas (data analysis)

### How It Works

1. **Speed Test Execution**: Calls Ookla Speedtest CLI with JSON output format
2. **Data Parsing**: Extracts metrics from JSON response
3. **Logging**: Appends results to CSV with timestamp
4. **Display**: Shows formatted results in console

### Speed Test Metrics

- **Ping (Latency)**: Response time in milliseconds
- **Download Speed**: Mbps (converted from bandwidth in bps)
- **Upload Speed**: Mbps (converted from bandwidth in bps)
- **Public IP**: Your current external IP address
- **ISP**: Internet Service Provider name

## Contributing

Contributions are welcome! This project is currently in active development.

### Development Priorities
1. System tray implementation (PyQt5)
2. Automated scanning with threading
3. Data visualization (matplotlib/plotly)
4. Packaging for distribution

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Ookla Speedtest**: For providing the CLI tool for accurate speed measurements
- Developed by **Tony Akinniranye**

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Current Version**: 0.1-alpha (Console Version)  
**Next Milestone**: System Tray Integration (v0.2)
