org_program = []

with open('day2_input.txt') as file:
    org_program = [int(i) for i in file.readline().split(",")]

def get_program():
    return org_program.copy()


def runProgram(prog, noun, verb):
    instruction_pointer = 0
    prog[1] = noun
    prog[2] = verb
    while prog[instruction_pointer] != 99:
        if prog[instruction_pointer] == 1:
            prog[prog[instruction_pointer + 3]] = prog[prog[instruction_pointer + 1]] + prog[prog[instruction_pointer + 2]]
        elif prog[instruction_pointer] == 2:
            prog[prog[instruction_pointer + 3]] = prog[prog[instruction_pointer + 1]] * prog[prog[instruction_pointer + 2]]
        else:
            print('No op')
        instruction_pointer += 4
    return prog[0]


for noun in range(100):
    for verb in range(100):
        program = get_program()
        if runProgram(program, noun, verb) == 19690720:
          print(str(100*noun+verb))
          exit(0)
# 8250



