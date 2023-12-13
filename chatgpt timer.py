def add_time(hours1, minutes1, hours2, minutes2):
    total_minutes = (hours1 * 60 + minutes1) + (hours2 * 60 + minutes2)
    total_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    return total_hours, remaining_minutes

# Example hours and minutes
hours_1 = 0
minutes_1 = 0
hours_2 = 0
minutes_2 = 1

# Calculate the total time by adding hours and minutes
total_hours, remaining_minutes = add_time(hours_1, minutes_1, hours_2, minutes_2)

# Normalize the time to have a single hour and a single minute
normalized_hours = total_hours % 24  # Ensure the hour is within a day (24 hours)
normalized_minutes = remaining_minutes

print(f"Total Time: {normalized_hours} hour(s) and {normalized_minutes} minute(s)")
