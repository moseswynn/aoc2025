from collections import deque
from enum import Enum

class DialDirections(Enum):
    LEFT = -1
    RIGHT = 1

class Dial(deque):
    def __init__(self, initial_value: int):
        super().__init__(range(100))
        super().rotate(initial_value)

        self.zero_count = 0
        

    @property
    def value(self):
        return self[0]
    
    def rotate(self, direction: DialDirections, steps: int):
        for i in range(steps):
            super().rotate(direction.value)
            if self.value == 0:
                self.zero_count += 1


def main():
    dial = Dial(50)
    with open('input.txt') as f:
        inputs = f.readlines()
    for s in inputs:
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
        dial.rotate(direction, steps)
    with open('output.txt','w+') as f:
        f.write(str(dial.zero_count))

if __name__ == "__main__":
    main()
    

