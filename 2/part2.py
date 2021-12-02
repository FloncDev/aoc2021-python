x = 0
y = 0
aim = 0

with open("input.txt") as f:
    data = f.readlines()

for line in data:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])

    match direction:
        case "forward":
            x += distance
            y += distance * aim
        
        case "up":
            aim -= distance

        case "down":
            aim += distance

print(x*y)
print([x, y, x*y])