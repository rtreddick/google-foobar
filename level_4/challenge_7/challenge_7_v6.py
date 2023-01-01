import copy
import math


class ImpossibleTriangleError(Exception):
    def __init__(self, beam_distance):
        self.beam_distance = beam_distance


class DistanceExceededError(Exception): pass


class Wall:
    def __init__(self, wall, dimensions, my_position, trainer_position, room):
        self.wall = wall
        self.axis = wall % 2
        self.length = dimensions[self.axis]
        self.span = dimensions[not self.axis]
        self.distance_to_me = dimensions[not self.axis] - my_position[not self.axis] if wall < 2 else my_position[not self.axis]
        self.distance_to_trainer = dimensions[not self.axis] - trainer_position[not self.axis] if wall < 2 else trainer_position[not self.axis]
        self.room = room

    def turn(self, direction):
        return self.room.walls[(self.wall + direction) % 4]

    def reflect(self):
        return self.room.walls[(self.wall + 2) % 4]


class Room:
    def __init__(self, walls, dimensions, my_position, trainer_position):
        self.walls = [Wall(wall, dimensions, my_position, trainer_position, self) for wall in walls]
        self.my_position = my_position
        self.trainer_position = trainer_position


class Path:
    def __init__(self, first_wall, direction, room):
        self.walls = [first_wall]
        self.direction = direction
        self.room = room
        self.axis = None
        self.turned = False
        self.opposite_axis = first_wall.wall % 2
        self.opposite = first_wall.turn(self.direction).distance_to_me
        self.adjacent = first_wall.distance_to_me
        

    def turn(self):
        path = copy.deepcopy(self)
        if not path.turned: path.turned = True
        wall = self.walls[-1].turn(self.direction)
        path.opposite += wall.length if wall.axis == self.opposite_axis else 0
        path.adjacent += wall.length if wall.axis != self.opposite_axis else 0
        path.walls.append(wall)
        return path
        
    def reflect(self):
        path = copy.deepcopy(self)
        wall = self.walls[-1].reflect()
        if not path.axis: path.axis = wall.axis
        path.direction = -path.direction
        path.opposite += wall.span if wall.axis != path.opposite_axis else 0
        path.adjacent += wall.span if wall.axis == path.opposite_axis else 0
        path.walls.append(wall)
        return path

    def extend(self):
        if self.axis is None or self.walls[-1].axis == self.axis: return (self.reflect(), self.turn())
        else: return (self.turn(),)

    def beam_distance(self, distance):
        wall = self.walls[-1]

        if self.adjacent > distance or self.opposite > distance:
            raise DistanceExceededError

        if wall.axis == self.opposite_axis:
            last_adjacent = wall.distance_to_trainer
            last_opposite = -wall.turn(self.direction).distance_to_trainer
        else:
            last_adjacent = -wall.turn(self.direction).distance_to_trainer
            last_opposite = wall.distance_to_trainer

        total_adjacent = self.adjacent + last_adjacent
        total_opposite = self.opposite + last_opposite

        if total_adjacent <= 0 or total_opposite <= 0:
            beam_distance = total_adjacent + total_opposite
            raise ImpossibleTriangleError(beam_distance)

        first_adjacent = float(self.walls[0].distance_to_me)
        first_opposite = first_adjacent * total_opposite / total_adjacent
        first_hypotenuse = math.sqrt(first_adjacent ** 2 + first_opposite ** 2)
        beam_distance = first_hypotenuse * total_opposite / first_opposite

        if first_opposite > self.walls[0].turn(self.direction).distance_to_me:
            raise ImpossibleTriangleError(beam_distance)

        if not self.turned and wall.turn(self.direction).distance_to_trainer > wall.turn(self.direction).distance_to_me:
            raise ImpossibleTriangleError(beam_distance)

        return beam_distance


def solution(dimensions, my_position, trainer_position, distance):

    if math.sqrt((trainer_position[0] - my_position[0]) ** 2 + (trainer_position[1] - my_position[1]) ** 2) <= distance: result = 1
    else: return 0

    walls = [0,1,2,3]
    directions = [-1,1]
    room = Room(walls, dimensions, my_position, trainer_position)
    stack = [Path(room.walls[wall], direction, room) for wall in walls for direction in directions]

    while stack:
        path = stack.pop()
        try:
            if path.beam_distance(distance) <= distance:
                result += 1
                stack.extend(path.extend())
        except ImpossibleTriangleError as e:
            if e.beam_distance < distance:
                stack.extend(path.extend())
        except DistanceExceededError:
            continue

    return result


print(solution([300,275], [150,150], [185,100], 500))