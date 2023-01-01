import math

class ImpossibleTriangleException(Exception): pass

class Wall:
    def __init__(self, name, on_x_axis, coordinate, length, distance_to_parallel, distance_to_me, distance_to_trainer):
        self.name = name
        self.on_x_axis = on_x_axis
        self.coordinate = coordinate
        self.length = length
        self.distance_to_parallel = distance_to_parallel
        self.distance_to_me = distance_to_me
        self.distance_to_trainer = distance_to_trainer

class Path:
    def __init__(self, current_wall, my_position, trainer_position, on_opposite_axis=True, first_adjacent_distance=None, opposite_distance=None, adjacent_distance=None, num_runs=1, prior_turn_wall=None, first_turn_wall=None, max_first_opposite_distance=None):
        self.current_wall = current_wall
        self.my_position = my_position
        self.trainer_position = trainer_position
        self.on_opposite_axis = on_opposite_axis
        self.first_adjacent_distance = first_adjacent_distance or self.current_wall.distance_to_me
        self.opposite_distance = opposite_distance or self.current_wall.length
        self.adjacent_distance = adjacent_distance or self.first_adjacent_distance
        self.num_runs = num_runs
        self.prior_turn_wall = prior_turn_wall
        self.first_turn_wall = first_turn_wall
        self.max_first_opposite_distance = max_first_opposite_distance or current_wall.length

    def copy(self):
        return Path(
            self.current_wall,
            self.my_position,
            self.trainer_position,
            self.on_opposite_axis,
            self.first_adjacent_distance,
            self.opposite_distance,
            self.adjacent_distance,
            self.num_runs,
            self.prior_turn_wall,
            self.first_turn_wall,
            self.max_first_opposite_distance
        )
        
    def extend_run(self, wall):
        self.current_wall = wall
        if self.on_opposite_axis: self.adjacent_distance += wall.distance_to_parallel
        else: self.opposite_distance += wall.distance_to_parallel

    def add_new_run(self, wall):
        self.num_runs += 1
        self.prior_turn_wall = self.current_wall
        self.current_wall = wall
        self.on_opposite_axis = not self.on_opposite_axis
        if self.num_runs == 2: self.first_turn_wall = wall
        if self.on_opposite_axis: self.opposite_distance += wall.length
        else: self.adjacent_distance += wall.length

    def extended(self, wall):
        path = self.copy()
        if path.current_wall.on_x_axis == wall.on_x_axis: path.extend_run(wall)
        else: path.add_new_run(wall)
        return path

    def calc_beam_distance(self):

        if self.num_runs == 1:
            x = abs(self.trainer_position[0] - self.my_position[0])
            y = abs(self.trainer_position[1] - self.my_position[1])
            self.opposite_distance = x if self.current_wall.on_x_axis else y
            self.adjacent_distance += self.current_wall.distance_to_trainer

        else:
            assert self.first_turn_wall is not None
            assert self.prior_turn_wall is not None

            self.max_first_opposite_distance = self.first_turn_wall.distance_to_parallel - self.first_turn_wall.distance_to_me
            self.opposite_distance -= self.max_first_opposite_distance

            if self.on_opposite_axis:
                self.adjacent_distance += self.current_wall.distance_to_trainer
                
            else:
                self.opposite_distance += self.current_wall.distance_to_trainer
                self.adjacent_distance -= self.prior_turn_wall.distance_to_parallel - self.prior_turn_wall.distance_to_trainer

        first_opposite_distance = float(self.opposite_distance) / self.adjacent_distance * self.first_adjacent_distance

        condition_1 = (first_opposite_distance > self.max_first_opposite_distance)
        condition_2 = any([self.adjacent_distance == 0, self.opposite_distance == 0])

        if any([condition_1, condition_2]):
            raise ImpossibleTriangleException

        first_hypotenuse_distance = math.sqrt(self.first_adjacent_distance ** 2 + first_opposite_distance ** 2)
        beam_distance = self.opposite_distance / first_opposite_distance * first_hypotenuse_distance

        return beam_distance

        
def solution(dimensions, my_position, trainer_position, max_distance):

    WALLS = [
        Wall('NORTH', True, dimensions[1], dimensions[0], dimensions[1], dimensions[1] - my_position[1], dimensions[1] - trainer_position[1]),
        Wall('SOUTH', True, 0, dimensions[0], dimensions[1], my_position[1], trainer_position[1]),
        Wall('EAST', False, dimensions[0], dimensions[1], dimensions[0], dimensions[0] - my_position[0], dimensions[0] - trainer_position[0]),
        Wall('WEST', False, 0, dimensions[1], dimensions[0], my_position[0], trainer_position[0])
    ]
    
    direct_distance = math.sqrt((trainer_position[0] - my_position[0]) ** 2 + (trainer_position[1] - my_position[1]) ** 2)
    if direct_distance > max_distance: return 0
    result = 1
    stack = [Path(wall, my_position, trainer_position) for wall in WALLS]

    while stack:
        path = stack.pop(0)
        try:
            if path.calc_beam_distance() <= max_distance:
                result += 1
                stack.extend([path.extended(wall) for wall in WALLS if path.current_wall != wall])
        except ImpossibleTriangleException:
            continue

    return result


# Input:
# solution.solution([300,275], [150,150], [185,100], 500)
# Output:
#     9

# result = solution([300,275], [150,150], [185,100], 500)

# print(result)

print('x' * 3)