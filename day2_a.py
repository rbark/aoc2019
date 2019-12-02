program = []
instruction_pointer = 0

with open('day2_input.txt') as file:
    program = [int(i) for i in file.readline().split(",")]

program[1] = 12
program[2] = 2

while program[instruction_pointer] != 99:
    if program[instruction_pointer] == 1:
        program[program[instruction_pointer + 3]] = program[program[instruction_pointer + 1]] + program[program[instruction_pointer + 2]]
    elif program[instruction_pointer] == 2:
        program[program[instruction_pointer + 3]] = program[program[instruction_pointer + 1]] * program[program[instruction_pointer + 2]]
    else:
        print('No op')
    instruction_pointer += 4

print(program[0])
# 3562672



