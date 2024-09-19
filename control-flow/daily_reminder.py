# daily_reminder.py

# Prompt the user for task details
task = input("Please enter the task description: ")
priority = input("Please enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Process the task based on its priority
match priority:
    case 'high':
        reminder = f"The task '{task}' is a HIGH priority task."
    case 'medium':
        reminder = f"The task '{task}' is a MEDIUM priority task."
    case 'low':
        reminder = f"The task '{task}' is a LOW priority task."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-sensitive
if time_bound == 'yes':
    reminder += " This task requires immediate attention today!"
else:
    reminder += " This task can be completed at your convenience."

# Print the customized reminder
print("\nReminder:")
print(reminder)
