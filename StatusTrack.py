# StatusTrack.py
# First Draft
# Michael Rudden, 2016

print("What are you trying to accomplish?")
task = input("Task: ")

print("Enter the stages of your task. When finished, enter a \".\"")
stages = []
inputting_stages = True
i = 1
while inputting_stages:
    stage = input("Stage " + str(i) + ": ")
    if stage == ".":
        break
    else:
        stages.append(stage)
        i += 1

print("Enter the items to track. When finished, enter a \".\"")
items = []
inputting_items = True
i = 1
while inputting_items:
    item = input("Item " + str(i) + ": ")
    if item == ".":
        break
    else:
        items.append(item)
        i += 1

print(stages)
for item in items:
    print(item)
#This should look kind of like a spreadsheet later
