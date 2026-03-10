"""
Ogechukwu Okereke
CSMC 111
Spring 2026
week6 Capstone Milestone
"""
tasks = ["Study Python", "Complete networking homework", "Work on GitHub"]
print("Today's Tasks:")
for task in tasks:
    print(f"- {task}")
tasks.append("Review dictionaries")
print("\nUpdated Task List:")
for task in tasks:
    print(f"- {task}")
print(f"\nTotal tasks: {len(tasks)}")