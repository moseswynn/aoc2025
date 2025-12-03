from base_solution import BaseSolution
import os
from functools import reduce
from itertools import batched

class Solution(BaseSolution):
    def __init__(self, input):
        super().__init__(input)
        self.ranges = [tuple(int(v) for v in range.split("-")) 
                  for range in self.input.read().split(",")]
        
    def solve_part1(self):
        bad_values = []
        for start, stop in self.ranges:
            for i in range(start, stop+1):
                if (length := len(str(i))) % 2 == 0:
                    stop_idx = int(length/2)
                    if str(i)[:stop_idx] == str(i)[stop_idx:]:
                        bad_values.append(i)
        return sum(bad_values)
    
    def solve_part2(self):
        bad_values = []
        for start, stop in self.ranges:
            for i in range(start, stop+1):
                length = len(str(i))
                factors = list(set(reduce(
                    list.__add__,
                    ([j, length//j] for j in range(1, int(length**0.5) + 1) if length % j == 0)
                )))
                factors.sort()
                for factor in factors:
                    if factor == length:
                        continue
                    batches = list(batched(str(i), factor))
                    if batches.count(batches[0]) == len(batches):
                        bad_values.append(i)
                        break
        return sum(bad_values)

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")