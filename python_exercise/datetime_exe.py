from datetime import datetime, timedelta

def remove_night_intervals(start_time, end_time):
    # Calculate the total interval between start and end times
    total_time = end_time - start_time

    # Define the night period from 12 AM to 6 AM for the start date
    night_start = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    night_end = start_time.replace(hour=6, minute=0, second=0, microsecond=0)
    
    # Check if the start and end times overlap with the night period
    night_duration = timedelta()  # timedelta() Initialize the night duration to zero

    # If the night period is within the start and end times
    if night_start < end_time and night_end > start_time:
        overlap_start = max(night_start, start_time)
        overlap_end = min(night_end, end_time)
        night_duration = overlap_end - overlap_start

    # Subtract the night duration from the total time
    total_time -= night_duration

    return total_time

def get_input():
    # Take start time and end time as input from the user
    start_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
    end_str = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
    
    # Convert string inputs to datetime objects
    start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    
    # Get the total time excluding the night intervals
    total_time = remove_night_intervals(start_time, end_time)
    
    # Print the result
    print(f"Total time excluding night intervals (12 AM - 6 AM): {total_time}")

# Example usage
get_input()


