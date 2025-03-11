
"""Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). 
(Hint: You can use python intervals module)"""
from datetime import datetime,timedelta

def remove_night_intervals(start_time, end_time):
    total_time = end_time - start_time
    current_time = start_time

    night_duration = timedelta()
    while current_time < end_time:

        night_start = current_time.replace(hour=0, minute=0, second=0)
        night_end = current_time.replace(hour=6, minute=0, second=0)
            
        if current_time.hour >= night_end.hour:
                night_start += timedelta(days=1)
                night_end += timedelta(days=1)

        if night_start < end_time and night_end > start_time:
                overlap_start = max(night_start, start_time)
                overlap_end = min(night_end, end_time)
                night_duration = (overlap_end - overlap_start)

        current_time += timedelta(days=1)

    return total_time - night_duration
def get_input():
    start_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
    end_str = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")

    start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

    if start_time >= end_time:
        print("Error: Start time must be earlier than end time.")
        return

    total_time = remove_night_intervals(start_time, end_time)

    print(f"Total time excluding night intervals (12 AM - 6 AM): {total_time}")

get_input()
