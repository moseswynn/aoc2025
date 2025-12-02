from collections import deque
from enum import Enum

class DialDirections(Enum):
    LEFT = -1
    RIGHT = 1

class Dial(deque):
    def __init__(self, initial_value: int):
        super().__init__(range(100))
        super().rotate(initial_value)
        

    @property
    def value(self):
        return self[0]
    
    def rotate(self, direction: DialDirections, steps: int):
        super().rotate(direction.value * steps)

def main():
    dial = Dial(50)
    with open('input.txt') as f:
        inputs = f.readlines()
    results = []
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
        results.append(dial.value)
    final = len(list(filter(lambda x: x == 0, results)))
    with open('output.txt','w+') as f:
        f.write(str(final))

if __name__ == "__main__":
    main()
    

