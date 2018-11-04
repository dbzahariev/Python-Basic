grades = int(input())
vreme = input()

outfit = ""
shoes = ""
if 10 <= grades <= 18:
    if vreme == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if vreme == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    if vreme == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < grades <= 24:
    if vreme == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    if vreme == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    if vreme == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
else:
    if vreme == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    if vreme == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    if vreme == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {grades} degrees, get your {outfit} and {shoes}.")
