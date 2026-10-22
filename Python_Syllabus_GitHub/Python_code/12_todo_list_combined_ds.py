"""Practical: 3.12 Combined Data Structures: To-do List"""

tasks = []  # list preserves task order; each task uses a set for unique tags

def add_task():
    task_name = input("Enter task: ").strip()
    tags = set(input("Enter tags separated by commas: ").lower().split(","))
    tags = {tag.strip() for tag in tags if tag.strip()}
    tasks.append({"task": task_name, "tags": tags})
    print("Task added.")

def display_all():
    if not tasks:
        print("No tasks yet.")
    for index, item in enumerate(tasks, 1):
        print(f"{index}. {item['task']} | Tags: {', '.join(sorted(item['tags'])) or 'None'}")

def find_by_tag():
    tag = input("Enter tag to search: ").strip().lower()
    matches = [item for item in tasks if tag in item["tags"]]
    if matches:
        for item in matches:
            print(item["task"], "| Tags:", ", ".join(sorted(item["tags"])))
    else:
        print("No tasks found with that tag.")

while True:
    print("\n1.Add task 2.Display all 3.Find by tag 4.Exit")
    choice = input("Choose: ")
    if choice == "1": add_task()
    elif choice == "2": display_all()
    elif choice == "3": find_by_tag()
    elif choice == "4": break
    else: print("Invalid choice.")
