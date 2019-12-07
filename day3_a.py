with open('day3_input_1.txt') as file:
    cable1_path = file.readline().split(",")

with open('day3_input_2.txt') as file:
    cable2_path = file.readline().split(",")

cable1_y_coord = set()
cable2_y_coord = set()
cable1_coords = {0: set()}
cable2_coords = {0: set()}

cable1_pos = [0, 0]
cable2_pos = [0, 0]

cable1_coords.get(0).add(0)
cable2_coords.get(0).add(0)


def register_up(steps, position, the_map):
    for i in range(position[1], position[1] + steps):
        the_map.get(position[0]).add(position[1] + 1)
        position[1] = position[1] + 1


def register_down(steps, position, the_map):
    for i in range(position[1], position[1] + steps):
        the_map.get(position[0]).add(position[1] - 1)
        position[1] = position[1] - 1


def register_right(steps, position, the_map):
    for i in range(position[0], position[0] + steps):
        if the_map.get(position[0] + 1) is None:
            the_map[position[0] + 1] = set()
        the_map.get(position[0] + 1).add(position[1])
        position[0] = position[0] + 1;


def register_left(steps, position, the_map):
    for i in range(position[0], position[0] + steps):
        if the_map.get(position[0] - 1) is None:
            the_map[position[0] - 1] = set()
        the_map.get(position[0] - 1).add(position[1])
        position[0] = position[0] - 1;

def insert_pos(cable, the_map, pos):
    for instruction in cable:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == 'U':
            register_up(steps, pos, the_map)
        if direction == 'D':
            register_down(steps, pos, the_map)
        if direction == 'L':
            register_left(steps, pos, the_map)
        if direction == 'R':
            register_right(steps, pos, the_map)


insert_pos(cable1_path, cable1_coords, cable1_pos)
insert_pos(cable2_path, cable2_coords, cable2_pos)

cross_coords = set();

def get_crossing():
    for key in cable1_coords:
        cable_1y_coords = cable1_coords.get(key)

        cable_2_y_coords = cable2_coords.get(key)
        if cable_2_y_coords is None:
            continue
        else:
            for y in cable_1y_coords:
                cross_coord = y in cable_2_y_coords
                if cross_coord:
                    cross_tuple = (key, y)
                    cross_coords.add(cross_tuple)


get_crossing()
shortest_dist = 0
for co in cross_coords:
    if co != (0, 0):
        dist = (abs(co[0]) + abs(co[1]))
        if shortest_dist == 0:
            shortest_dist = dist
        elif dist < shortest_dist:
            shortest_dist = dist

print('shortest dist:' , shortest_dist)




