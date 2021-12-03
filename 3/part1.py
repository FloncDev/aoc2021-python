with open("input.txt", "r") as f:
    data = f.readlines()

gamma = ""
epsilon = ""

# Get the gamma value
for i in range(len(data[0])-1):
    count_0 = 0
    count_1 = 0
    for line in data:
        try:
            if line[i] == "0": count_0 += 1
            if line[i] == "1": count_1 += 1
        except IndexError:
            pass

    if count_0 > count_1: gamma += "0"
    else: gamma += "1"


# Flip the gamma value to get the epsilon value
for i in range(len(gamma)):
    if gamma[i] == "0":
        epsilon += "1"
    else:
        epsilon += "0"

print(f"Gamma: {int(gamma, 2)}; Epsilon: {int(epsilon, 2)}; Power Consumption: {int(gamma, 2) * int(epsilon, 2)}")