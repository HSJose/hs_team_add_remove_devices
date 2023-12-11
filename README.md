# README.md for AddRemoveDevice Script

## Overview
This Python script is designed to manage the addition and removal of devices using the HeadSpin API. It features a class `AddRemoveDevice` with methods to add or remove devices from a team, as well as to process CSV files containing device details.

## Prerequisites
- Python 3.6 or higher
- `httpx`, `csv`, `rich`, and `python-dotenv` libraries
- An API key for HeadSpin API

## Installation
1. Clone the repository or download the script.
2. Install required packages:
   ```bash
   pip install httpx rich python-dotenv
   ```
s
## Set up the .env file with your HeadSpin API key:
    API_KEY=your_api_key_here

## Usage
Prepare your CSV files (sample_add_list.csv and sample_remove_list.csv) with device details.

Run the script:
    ```
    python add_remove_device.py
    ```

Follow the output on the terminal for the status of device addition or removal.

## CSV File Format
Device List CSV Files
- The script requires two CSV files: one for adding devices (sample_add_list.csv) and another for removing devices (sample_remove_list.csv). Each CSV file should follow this specific format:

- CSV Format
    Each CSV file should contain two columns:

    team_id: This column represents the unique identifier for the team to which the device belongs.
    device_address: This column contains the address of the device.
    Example
    Here is an example of how the CSV file should be structured:

Example:
```
team_id,device_address
ffdddba1-d22e-11ec-b15d-0243c669dd9b,address_1
ffdddba1-d22e-11ec-b15d-0243c669dd9b,address_2
...
```

## How It Works
- Environment Variables: The script loads API keys from a .env file.
- Main Function: The main function processes the CSV files and calls the add_devices and remove_devices methods for each device.
