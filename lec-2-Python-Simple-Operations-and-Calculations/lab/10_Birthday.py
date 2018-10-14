length = float(input())
width = float(input())
height = float(input())
percent = float(input())

print(float("{0:.3f}".format(((length * width * height) * 0.001) * (1 - (percent * 0.01)))))
