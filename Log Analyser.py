import pandas as pd 
from datetime import datetime 
# Define the path to the CSV file 
csv_path = "path" 
# Define the column headers 
columns = [ 
"Message", "Id", "Version", "Qualifiers", "Level", "Task", "Opcode", "Keywords",  
"RecordId", "ProviderName", "ProviderId", "LogName", "ProcessId", "ThreadId",  
"MachineName", "UserId", "TimeCreated", "ActivityId", "RelatedActivityId",  
"ContainerLog", "MatchedQueryIds", "Bookmark", "LevelDisplayName",  
"OpcodeDisplayName", "TaskDisplayName", "KeywordsDisplayNames", 
"Properties" 
] 
# Read the CSV file into a DataFrame with specified columns, skipping the first two 
rows 
df = pd.read_csv(csv_path, names=columns, skiprows=2) 
# Convert the 'TimeCreated' column to datetime 
df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], errors='coerce') 
# Function to count logs by level 
5 
6 
 
def count_logs_by_level(df): 
    return df['LevelDisplayName'].value_counts() 
 
# Function to filter logs by time range 
def filter_logs_by_time(df, start_time, end_time): 
    mask = (df['TimeCreated'] >= start_time) & (df['TimeCreated'] <= end_time) 
    return df.loc[mask] 
 
# Function to display the first n logs 
def display_logs(df, n=10): 
    print(df.head(n)) 
 
# Example analysis 
if __name__ == "__main__": 
    # Count logs by level 
    log_counts = count_logs_by_level(df) 
    print("Log counts by level:") 
    print(log_counts) 
 
    # Define a time range 
    start_time = datetime(2023, 1, 1) 
    end_time = datetime(2024, 1, 1) 
 
    # Filter logs by time range 
filtered_logs = filter_logs_by_time(df, start_time, end_time) 
print(f"\nLogs between {start_time} and {end_time}:") 
display_logs(filtered_logs, n=10)