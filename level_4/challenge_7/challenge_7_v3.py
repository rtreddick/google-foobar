import math

class ImpossibleTriangleException(Exception): pass

class Wall:
    def __init__(self, name, on_x_axis, coordinate, length, distance_to_opposite, distance_to_me, distance_to_trainer):
        self.name = name
        self.on_x_axis = on_x_axis
        self.coordinate = coordinate
        self.length = length
        self.distance_to_opposite = distance_to_opposite
        self.distance_to_me = distance_to_me
        self.distance_to_trainer = distance_to_trainer

class Run:
    def __init__(self, walls, on_opposite_axis = False):
        self.walls = walls
        self.first_wall = self.walls[0]
        self.on_opposite_axis = on_opposite_axis
        self.on_x_axis = self.first_wall.on_x_axis
        self.span_between_walls = self.first_wall.distance_to_opposite
        self.length_of_walls = self.first_wall.length

    def current_wall(self):
        return self.walls[-1]

class Path:
    def __init__(self, runs):
        self.runs = runs
        self.first_run = runs[0]
        self.first_wall = self.first_run.first_wall

    def copy(self):
        return Path([Run(run.walls[:]) for run in self.runs])

    def current_run(self):
        return self.runs[-1]

    def current_wall(self):
        return self.current_run().current_wall()

    def extend_run(self, wall):
        self.current_run().walls.append(wall)

    def add_new_run(self, wall):
        on_opposite_axis = not self.current_run().on_opposite_axis
        self.runs.append(Run([wall], on_opposite_axis))

    def extended(self, wall):
        path = self.copy()
        if path.current_wall().on_x_axis == wall.on_x_axis: path.extend_run(wall)
        else: path.add_new_run(wall)
        return path

    def calc_beam_distance(self, fighters_x, fighters_y):
        adjacent_distance = 0
        opposite_distance = 0
        max_first_opposite_distance = self.first_run.length_of_walls

        if len(self.runs) == 1:
            adjacent_distance = self.first_wall.distance_to_me + self.current_wall().distance_to_trainer + self.current_run().span_between_walls * (len(self.current_run().walls) - 1)
            opposite_distance = fighters_x if self.current_run().on_x_axis else fighters_y

        else:
            for num, run in enumerate(self.runs, 1):

                if num == 1:
                    adjacent_distance += run.first_wall.distance_to_me

                if num == 2:
                    max_first_opposite_distance = run.first_wall.distance_to_me
                    opposite_distance -= run.first_wall.distance_to_opposite - max_first_opposite_distance

                if run.on_opposite_axis:
                    if num == len(run.walls) - 1: adjacent_distance -= run.current_wall().distance_to_opposite - run.current_wall().distance_to_trainer
                    if num == len(run.walls): adjacent_distance += run.current_wall().distance_to_trainer
                    adjacent_distance += run.span_between_walls * (len(run.walls) - 1)
                    opposite_distance += run.length_of_walls

                else:
                    if num == len(run.walls) - 1: opposite_distance -= run.current_wall().distance_to_opposite - run.current_wall().distance_to_trainer
                    if num == len(run.walls): opposite_distance += run.current_wall().distance_to_trainer
                    adjacent_distance += run.span_between_walls
                    opposite_distance += run.length_of_walls * (len(run.walls) - 1)
                    
        first_adjacent_distance = self.first_wall.distance_to_me
        first_opposite_distance = float(opposite_distance) / adjacent_distance * first_adjacent_distance

        condition_1 = (first_opposite_distance > max_first_opposite_distance)
        condition_2 = any([adjacent_distance == 0, opposite_distance == 0])

        if any([condition_1, condition_2]):
            raise ImpossibleTriangleException

        first_hypotenuse_distance = math.sqrt(first_adjacent_distance ** 2 + first_opposite_distance ** 2)
        beam_distance = opposite_distance / first_opposite_distance * first_hypotenuse_distance

        return beam_distance

def solution(dimensions, my_position, trainer_position, max_distance):

    x = dimensions[0]
    y = dimensions[1]
    my_x = my_position[0]
    my_y = my_position[1]
    trainer_x = trainer_position[0]
    trainer_y = trainer_position[1]
    fighters_x = abs(trainer_x - my_x)
    fighters_y = abs(trainer_y - my_y)

    WALLS = [
        Wall('NORTH', True, y, x, y, y - my_y, y - trainer_y),
        Wall('SOUTH', True, 0, x, y, my_y, trainer_y),
        Wall('EAST', False, x, y, x, x - my_x, x - trainer_x),
        Wall('WEST', False, 0, y, x, my_x, trainer_x)
    ]
    
    direct_distance = math.sqrt((trainer_x - my_x) ** 2 + (trainer_y - my_y) ** 2)
    if direct_distance > max_distance:
        return 0

    result = 1
    stack = [Path([Run([wall], True)]) for wall in WALLS]

    while stack:
        path = stack.pop(0)
        try:
            if path.calc_beam_distance(fighters_x, fighters_y) <= max_distance:
                result += 1
                stack.extend([path.extended(wall) for wall in WALLS if path.current_wall() != wall])
        except ImpossibleTriangleException:
            continue

    return result

print(solution([1250,1250], [25,25], [100,100], 1000))