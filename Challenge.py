def convert_to_24_hour(hour, minute, period):
    # Adjust hour based on period
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the result as a four-digit string
    time_24_hour = "{:02d}{:02d}".format(hour, minute)
    
    return time_24_hour

# Example usage:
result1 = convert_to_24_hour(10, 30, "am")
result2 = convert_to_24_hour(8, 30, "pm")
result3 = convert_to_24_hour(12, 15, "am")
print(result1)  # Output: 1030
print(result2)  # Output: 2030
print(result3)  # Output: 0015