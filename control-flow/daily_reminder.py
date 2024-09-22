# daily_reminder.py

# Prompt the user for task details
task= input("Enter task : ")
priority=input("Priority (high, medium, low): ").lower()
time_bound=input("Is the task time-bound? (yes or no): ").lower()



match priority:
    case 'high':
        if time_bound == 'yes':
            message = "that requires immediate attention today!"

        elif time_bound == 'no':
            message = "Consider completing it when you have free time."
        print (f"Reminder: {task} is a high prority task {message}")
    
    case 'medium':
        if time_bound == 'yes':
            message = "that requires immediate attention today!"
        

        elif time_bound == 'no':
            message = "Consider completing it when you have free time."
        print (f"Reminder: {task} is a medium prority task {message}")
    
    case 'low':
        if time_bound == 'yes':
            message = "that requires immediate attention today!"

        elif time_bound == 'no':
            message = "Consider completing it when you have free time."
        print (f"Reminder: {task} is a low prority task {message}")
                   
    case _:
        print = f"{task} has an UNKNOWN priority."
