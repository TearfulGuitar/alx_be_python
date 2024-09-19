task=input("Enter a task description: ")
priority=input("Enter task priority (high/medium/low): ")
time_bound=input("Is the task time bound? (yes/no): ")

match priority:
    case "high":
        if time_bound:
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif not time_bound:
            print("Reminder:Schedule {task} conveniently")
    case "medium":
        if time_bound:
            print(f"Reminder:Perform {task} before day ends")
        elif not time_bound:
            print("Reminder:Schedule {task} conveniently")
    case "low" :
        if time_bound:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        elif not time_bound:
            print(f"Reminder:Schedule {task} conveniently")