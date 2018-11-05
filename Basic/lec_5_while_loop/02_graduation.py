name = input()

grade = float(input())
counter = 1
result = 0
year = 1
while year < 12:
    if grade > 4:
        year += 1
    result += grade
    counter += 1
    kk = input()
    grade = float(kk)

average = result / year
print(f"{name} graduated. Average grade: {average:.2f}")
