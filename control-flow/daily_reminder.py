task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level. Please use high, medium, or low."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound != "no":
    reminder = "Invalid input for time-bound. Please use yes or no."

print(f"Reminder: {reminder}")
