import enum
import dataclasses

import data.day12_data as d


class Direction(enum.Enum):
    North = "N"
    South = "S"
    East = "E"
    West = "W"
    Left = "L"
    Right = "R"
    Forward = "F"


class Axis(enum.Enum):
    No_axis = -1
    Latitude = 0
    Longitude = 1


@dataclasses.dataclass
class Order:
    direction: Direction
    value: int


positive_rotation = [
    Direction.East,
    Direction.North,
    Direction.West,
    Direction.South,
]

negative_rotation = [
    Direction.East,
    Direction.South,
    Direction.West,
    Direction.North,
]


def analyse_direction(direction: Direction):
    if direction in [Direction.North, Direction.South]:
        positive = 1 if direction == Direction.North else -1
        return Axis.Latitude, positive

    if direction in [Direction.East, Direction.West]:
        positive = 1 if direction == Direction.East else -1
        return Axis.Longitude, positive

    positive = 1 if direction == Direction.Left else -1
    return Axis.No_axis, positive


def identify_direction(facing: Direction, value: int, is_positive: bool) -> Direction:
    rotation = positive_rotation if is_positive else negative_rotation
    start = rotation.index(facing)
    offset = value // 90
    return rotation[(start + offset) % len(rotation)]


class Boat:
    def __init__(self):
        self.facing = Direction.East
        # North/East -> positive
        self.latitude = 0
        self.longitude = 0

        self.waypoint_latitude = 1
        self.waypoint_longitude = 10

    def move(self, order: Order):
        axis, positive = analyse_direction(
            self.facing if order.direction == Direction.Forward else order.direction
        )

        if axis == Axis.Latitude:
            self.latitude += positive * order.value

        if axis == Axis.Longitude:
            self.longitude += positive * order.value

        if axis == Axis.No_axis:
            self.facing = identify_direction(self.facing, order.value, positive > 0)

    def advanced_move(self, order: Order):
        axis, positive = analyse_direction(order.direction)

        if axis == Axis.Latitude:
            self.waypoint_latitude += positive * order.value

        if axis == Axis.Longitude:
            self.waypoint_longitude += positive * order.value

        if axis == Axis.No_axis:
            if order.direction == Direction.Forward:
                self.latitude  += order.value * self.waypoint_latitude
                self.longitude += order.value * self.waypoint_longitude
            else:
                new_latitude_direction = identify_direction(
                    Direction.North if self.waypoint_latitude >= 0 else Direction.South,
                    order.value,
                    positive > 0,
                )

                new_longitude_direction = identify_direction(
                    Direction.East if self.waypoint_longitude >= 0 else Direction.West,
                    order.value,
                    positive > 0,
                )

                old_latitude = self.waypoint_latitude
                old_longitude = self.waypoint_longitude

                if new_latitude_direction == Direction.North: self.waypoint_latitude =      abs(old_latitude)
                if new_latitude_direction == Direction.South: self.waypoint_latitude = -1 * abs(old_latitude)
                if new_latitude_direction == Direction.East: self.waypoint_longitude =      abs(old_latitude)
                if new_latitude_direction == Direction.West: self.waypoint_longitude = -1 * abs(old_latitude)

                if new_longitude_direction == Direction.North: self.waypoint_latitude =      abs(old_longitude)
                if new_longitude_direction == Direction.South: self.waypoint_latitude = -1 * abs(old_longitude)
                if new_longitude_direction == Direction.East: self.waypoint_longitude =      abs(old_longitude)
                if new_longitude_direction == Direction.West: self.waypoint_longitude = -1 * abs(old_longitude)

    @property
    def manhattan_distance(self) -> int:
        return abs(self.latitude) + abs(self.longitude)


def solve_day12():
    output = "Day 12 "

    boat = Boat()
    advanced_boat = Boat()

    for line in d.data:
        order = Order(Direction(line[0]), int(line[1:]))
        boat.move(order)
        advanced_boat.advanced_move(order)

    output += str(boat.manhattan_distance)
    output += " " + str(advanced_boat.manhattan_distance)

    print(output, end=" ")
