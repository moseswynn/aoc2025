from ..base_solution import BaseSolution
from collections import deque
from enum import Enum
import os

class DialDirections(Enum):
    LEFT = -1
    RIGHT = 1

class Dial(deque):
    def __init__(self, initial_value: int = 0) -> None:
        super().__init__(range(100))
        if initial_value > 0:
            super().rotate(initial_value*-1)

        self.history = []
        self.zero_count = 0

    @property
    def value(self):
        return self[0]
    
    def rotate(self, direction: DialDirections, steps: int) -> None:
        for i in range(steps):
            super().rotate(direction.value)
            if self.value == 0:
                self.zero_count += 1
        self.history.append(self.value)

class Solution(BaseSolution):
    def __init__(self, input):
        super().__init__(input)
        turns = self.input.readlines()
        self.dial = Dial(50)
        for s in turns:
            direction = s[0]
            match direction.lower():
                case "r":
                    direction = DialDirections.RIGHT
                case "l":
                    direction = DialDirections.LEFT
                case _:
                    print("unmatched direction, skipping...")
                    continue
            steps = int(s[1:])
            self.dial.rotate(direction, steps)



    def solve_part1(self):
        return len(list(filter(lambda x: x == 0, self.dial.history)))

    def solve_part2(self):
        return self.dial.zero_count
    
def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 solution: {s.solve_part2()}")
    