
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine reminder based on priority using Match Case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an undefined priority"

# Adjust message if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    message += ". Consider completing it when you have free time."
elif time_bound == "no" and priority in ["high", "medium"]:
    message += ". Try to complete it as soon as possible."

# Print the final reminder
print("\n" + message)
