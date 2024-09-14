# Log Analysis Tool using Pandas

## Overview
This project is a simple log analysis tool built using Python and pandas. It reads a CSV file containing system logs, allowing you to filter logs by time range, count the number of logs by severity level, and display selected logs. This tool can be useful for analyzing log files in an efficient and structured manner.

## Features
- **Count Logs by Level**: Get a count of logs based on their severity level (e.g., Information, Warning, Error).
- **Filter Logs by Time Range**: Specify a start and end time to retrieve logs within that period.
- **Display Logs**: Display the first `n` log entries for quick viewing.

### How to Use

1. **Prepare a CSV File**: 
   You will need a CSV file containing logs with the following columns:
   ```
   "Message", "Id", "Version", "Qualifiers", "Level", "Task", "Opcode", 
   "Keywords", "RecordId", "ProviderName", "ProviderId", "LogName", 
   "ProcessId", "ThreadId", "MachineName", "UserId", "TimeCreated", 
   "ActivityId", "RelatedActivityId", "ContainerLog", "MatchedQueryIds", 
   "Bookmark", "LevelDisplayName", "OpcodeDisplayName", "TaskDisplayName", 
   "KeywordsDisplayNames", "Properties"
   ```

   **Note**: You are responsible for providing the CSV file. The script does not include a sample file but is designed to work with log data structured as shown above.

2. **Run the Script**: Update the path to your CSV file in the script and execute it. The tool will:
   - Count the logs based on their severity level.
   - Filter logs within the time range specified in the code.
   - Display the first `n` logs for quick inspection.

## Requirements
- Python 3.x
- pandas
- datetime

Install the required dependencies using:

```bash
pip install pandas
