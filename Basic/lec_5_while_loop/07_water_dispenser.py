ml = float(input())
taped = 0
buttons = {"Easy": 50, "Medium": 100, "Hard": 200}
while ml > 0:
    ml -= buttons[input()]
    taped += 1
if ml == 0:
    print(f"The dispenser has been tapped {taped} times.")
else:
    print(f"{abs(ml):.0f}ml has been spilled.")