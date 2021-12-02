with open("input.txt", "r") as file:
    data = file.readlines()

increase_count = 0

for index, current in enumerate(data):
    try:
        if int(current) > int(data[index-1]):
            increase_count += 1

    except IndexError:
        continue

print(increase_count)