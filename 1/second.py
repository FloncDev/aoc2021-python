with open("input.txt", "r") as file:
    data = file.readlines()

increase_count = 0

for index, current in enumerate(data):
    try:
        current_window = int(current)
        for i in range(1, 3):
            try: current_window += int(data[index - i])
            except: continue

        last_window = int(data[index - 1])
        for i in range(2, 4):
            try: last_window += int(data[index - i])
            except: continue

        if current_window > last_window:
            increase_count += 1

    except IndexError:
        continue

print(increase_count)