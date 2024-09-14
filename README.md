# Log Analysis Tool using Pandas

## Overview
This project is a simple log analysis tool built using Python and pandas. It reads a CSV file containing system logs, allowing you to filter logs by time range, count the number of logs by severity level, and display selected logs. This tool can be useful for analyzing log files in an efficient and structured manner.

## Features
- **Count Logs by Level**: Get a count of logs based on their severity level (e.g., Information, Warning, Error).
- **Filter Logs by Time Range**: Specify a start and end time to retrieve logs within that period.
- **Display Logs**: Display the first `n` log entries for quick viewing.

### How to Use

You don’t need to provide a CSV file with the project. Simply ensure that you have your own CSV file with the required columns, and the script will work with your log data.

## Requirements
- Python 3.x
- pandas
- datetime

Install the required dependencies using:

```bash
pip install pandas
