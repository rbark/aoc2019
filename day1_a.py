instruction_rows = []
sum = 0


with open('day1_input.txt') as file:
    instruction_rows = file.readlines()

for line in instruction_rows:
    mass = (int(line) // 3) - 2
    sum = sum + mass

print(sum)
# 3297909