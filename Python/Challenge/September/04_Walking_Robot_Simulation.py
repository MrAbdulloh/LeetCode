# https://leetcode.com/problems/walking-robot-simulation/description/
from typing import List


def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0

    x, y = 0, 0

    obstacle_set = set(map(tuple, obstacles))

    max_distance_squared = 0

    for command in commands:
        if command == -1:
            direction_index = (direction_index + 1) % 4
        elif command == -2:
            direction_index = (direction_index - 1) % 4
        else:
            dx, dy = directions[direction_index]
            for _ in range(command):
                if (x + dx, y + dy) not in obstacle_set:
                    x += dx
                    y += dy
                    max_distance_squared = max(max_distance_squared, x ** 2 + y ** 2)
                else:
                    break

    return max_distance_squared


commands = [4, -1, 3]
obstacles = []
print(robotSim(commands, obstacles))
