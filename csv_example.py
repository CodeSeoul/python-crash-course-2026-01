import csv


data = []
with open("sample.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
        data.append(row)

# print(data)

# How many hours did Bob work?
hours = 0
for record in data:
    if record["employee"] == "Bob":
        hours += int(record["hours"])
print("Bob's hours:", hours)

# Which task has the most hours?
task_hours = {}
for record in data:
    task = record["task"]
    if record["task"] not in task_hours:
        task_hours[task] = 0
    
    hours = int(record["hours"])
    task_hours[task] += hours

longest_task = None
max_hours = 0
for task, hours in task_hours.items():
    if hours > max_hours:
        longest_task = task
        max_hours = hours
print("Longest task is", longest_task, "with", max_hours, "hours")
