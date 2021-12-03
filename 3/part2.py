# Sorry for this pile of garbage code. I nearly cried while trying to figure this out.

with open("input.txt", "r") as f:
    data = f.readlines()

O2_generator = ""
CO2_scrubber = ""

# Finds the most common bits in the data
def get_common_bits(input_data: list):
    common_bits = ""
    for i in range(len(input_data[0])-1):
        count_0 = 0
        count_1 = 0
        for line in input_data:
            try:
                if line[i] == "0": count_0 += 1
                if line[i] == "1": count_1 += 1
            except IndexError:
                pass

        if count_0 > count_1: common_bits += "0"
        else: common_bits += "1"
    return common_bits

# O2 generator
O2_list = data.copy()
for i in range(len(data[0])-1):
    common_bits = get_common_bits(O2_list)
    passed = []
    for index, line in enumerate(O2_list):
        if line[i] == common_bits[i]:
            passed.append(line)

    O2_list = passed

    if len(O2_list) == 1:
        O2_generator = O2_list[0]
        break

# CO2 scrubber
CO2_list = data.copy()
for i in range(len(data[0])-1):
    common_bits = get_common_bits(CO2_list)
    passed = []
    for index, line in enumerate(CO2_list):
        if line[i] != common_bits[i]:
            passed.append(line)

    CO2_list = passed

    if len(CO2_list) == 1:
        CO2_scrubber = CO2_list[0]
        break

print(f"O2 generator: {int(O2_generator, 2)}; CO2 scrubber: {int(CO2_scrubber, 2)}; Life Support Rating: {int(O2_generator, 2) * int(CO2_scrubber, 2)}")