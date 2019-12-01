instruction_rows = []
sum = 0

def get_fuel(start_mass):
    calculated_mass = 0
    mass = start_mass
    while (mass//3)-2 > 0:
        mass = (int(mass) // 3) - 2
        calculated_mass += mass
    return calculated_mass


with open('day1_input.txt') as file:
    instruction_rows = file.readlines()

for line in instruction_rows:
    mass =get_fuel(int(line))
    sum = sum + mass

print(sum)

# 4943994