import enum
import dataclasses


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
            rotation = positive_rotation if positive > 0 else negative_rotation
            start = rotation.index(self.facing)
            offset = order.value // 90
            self.facing = rotation[(start + offset) % len(rotation)]

    def advanced_move(self, order: Order):
        axis, positive = analyse_direction(order.direction)

        if axis.Latitude:
            self.waypoint_latitude += positive * order.value

        if axis.Longitude:
            self.waypoint_longitude += positive * order.value

        if axis == Axis.No_axis:
            if order.direction == Direction.Forward:
                self.latitude += order.value * self.waypoint_latitude
                self.longitude += order.value * self.waypoint_longitude
            else:
                # TODO Fix -> make a truth table
                rotation = positive_rotation if positive > 0 else negative_rotation
                start = rotation.index(
                    Direction.North if self.waypoint_latitude >= 0 else Direction.South
                )
                offset = order.value // 90
                new_direction = rotation[(start + offset) % len(rotation)]
                new_axis, new_positive = analyse_direction(new_direction)
                if (
                    new_axis == Axis.Latitude
                    and self.waypoint_latitude * new_positive < 0
                ):
                    self.waypoint_latitude *= -1
                    self.waypoint_longitude *= -1
                if new_axis == Axis.Longitude:
                    self.waypoint_longitude, self.waypoint_latitude = (
                        positive * -1 * self.waypoint_latitude,
                        positive * self.waypoint_longitude,
                    )

    @property
    def manhattan_distance(self) -> int:
        return abs(self.latitude) + abs(self.longitude)


import data.day12_data as d


def solve_day12():
    output = "Day 12 "

    boat = Boat()
    advanced_boat = Boat()

    for line in d.sample_data:
        order = Order(Direction(line[0]), int(line[1:]))
        boat.move(order)
        advanced_boat.advanced_move(order)

    output += str(boat.manhattan_distance)
    output += " " + str(advanced_boat.manhattan_distance)

    print(output, end=" ")
