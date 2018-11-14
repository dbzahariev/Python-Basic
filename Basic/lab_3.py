# import datetime
#
# today_s = datetime.time(10, 30)
# today_e = datetime.time(11, 30)
# today_d = datetime.time()
# today_d = today_d.replace(hour=today_s.hour - today_e.hour)
#
# today = today.minute = 3;
# print(today)
# print(today_d.minute)
# print("Today's date is {:%H, %M}".format(today))

# name = input()
#
#
# year = 0.0
# result = 0.0
# count_grades = 0.0
# while year < 12:
#     grade = float(input())
#     count_grades += 1
#     if grade > 4:
#         year += 1
#     result += grade
#
#
# average = result / count_grades
# print(f"{name} graduated. Average grade: {average:.2f}")

# name = input()
# grades = 1.0
# sum_all_grades = 0.0
# while grades <= 12:
#     grade = float(input())
#     if grade >= 4.00:
#         sum_all_grades += grade
#         grades += 1
#
# average = sum_all_grades / 12
# print(f"{name} graduated. Average grade: {average:.2f}")

# name = input()
# grades = 1.0
# sums = 0.0
# expel_counter = 0
#
# while grades <= 12:
#     grade = float(input())
#
#     if grade < 4.00:
#         expel_counter += 1
#
#     if expel_counter == 2:
#         break
#
#     if grade >= 4.00:
#         sums += grade
#         grades += 1
#     average = sums / 12
#
# if expel_counter == 2:
#     print(f'{name} has been excluded at {round(grades)} grade')
# else:
#     print(f'{name} graduated. Average grade: {average:.2f}')


# steps = input()
# counter_steps = 0
# goal = 10000
#
# while True:
#     steps = input()
#
#     if steps == "Going home":
#         steps = int(input())
#         counter_steps += steps
#         if counter_steps >= goal:
#             print("Goal reached! Good job!")
#         else:
#             diff = goal - counter_steps
#             print(f"{diff} more steps to reach goal.")
#         break
#
#     counter_steps += int(steps)
#
#     if counter_steps >= goal:
#         print("Goal reached! Good job!")
#         break
