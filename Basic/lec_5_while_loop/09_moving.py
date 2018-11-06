free_cubic_meters = float(input()) * float(input()) * float(input())  # width * length * height
count_transported_box = 0
boxs = input()
diff = free_cubic_meters
while not boxs == "Done":
    count_transported_box += float(boxs)
    diff = count_transported_box - free_cubic_meters
    if count_transported_box >= free_cubic_meters:
        break
    boxs = input()

if diff >= 0:
    print(f"No more free space! You need {(count_transported_box - free_cubic_meters):.0f} Cubic meters more.")
else:
    print(f"{abs(diff):.0f} Cubic meters left.")
