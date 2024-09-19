Task=input("Enter a task description: ").lower()
Priority=input("Enter task priority (high/medium/low): ").lower()
Time_bound=input("Is the task time bound? (yes/no): ").lower()

match Priority:
    case "high":
        if Time_bound:
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
        elif not Time_bound:
            print("Reminder:Schedule {Task} conveniently")
    case "medium":
        if Time_bound:
            print(f"Reminder:Perform {Task} before day ends")
        elif not Time_bound:
            print("Reminder:Schedule {Task} conveniently")
    case "low" :
        if Time_bound:
            print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
        elif not Time_bound:
            print(f"Reminder:Schedule {Task} conveniently")