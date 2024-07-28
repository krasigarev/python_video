import sys

name = input()

best_name = ""
max_goal = - sys.maxsize
max_name = ""


while not name == "END":
    count_goal = int(input())
    best_name = name

    if count_goal > max_goal:
        max_goal = count_goal
        max_name = best_name

    if max_goal >= 10:
        break

    name = input()

print(f"{best_name} is the best players.")

if max_goal >= 3:
    print(f'He has scored {max_goal} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_name} goals.')





