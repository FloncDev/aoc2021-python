x = 0
y = 0

with open("input.txt") as f:
    data = f.readlines()

for line in data:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])

    match direction:
        case "forward":
            x += distance
        
        case "up":
            y -= distance

        case "down":
            y += distance

print(x*y)      
            