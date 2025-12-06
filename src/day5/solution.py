
from base_solution import BaseSolution
import os
from functools import reduce

def consolidate_ranges(rng1, rng2):
    if rng2[0] <= rng1[1]:
        return rng1[0], rng2[1]

class Solution(BaseSolution):
    def __init__(self, input: str | bytes):
        try:
            super().__init__(input)
        except:
            self.input = input
        raw = self.input.read()
        ranges_raw, ids_raw = raw.split("\n\n")
        self.ranges = list([tuple(int(id) 
                                  for id in rng.strip().split("-")) 
                                  for rng in ranges_raw.splitlines()])
        self.ids = list([int(id.strip()) for id in ids_raw.splitlines()])

    def consolidate_ranges(self):
        self.ranges.sort(key=lambda x: x[0])
        new_ranges = []
        new_range = []
        total_ranges = len(self.ranges)
        current_idx = 0
        while current_idx < total_ranges:
            current_range = self.ranges[current_idx]
            if not new_range:
                new_range.extend(current_range)
            else:
                if current_range[0] <= new_range[1]:
                    new_range[1] = current_range[1]
                else:
                    new_ranges.append(tuple(new_range))
                    new_range = list(current_range)                
            current_idx += 1
        new_ranges.append(tuple(new_range))
        return new_ranges
        
    def solve_part1(self):
        counter = 0
        for id in self.ids:
            in_range = False
            for start, stop in self.ranges:
                if id in range(start, stop+1):
                    in_range = True
                    break
            if in_range:
                counter += 1
        return counter

    def solve_part2(self):
        self.ranges = self.consolidate_ranges()
        # return sum(map(lambda x: x[1]-x[0]+1, self.ranges)) #THIS PASSES TESTS, BUT DOES NOT PASS WITH REAL INPUT!?
        counter=0
        for start, stop in self.ranges:
            for _ in range(start,stop+1):
                counter += 1
                print(counter)
        return counter

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")
    