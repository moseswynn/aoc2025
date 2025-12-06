
from base_solution import BaseSolution
import os
import re
from functools import reduce

class Solution(BaseSolution):
    def __init__(self, input):
        try:
            super().__init__(input)
        except:
            self.input = input

        lines = [normalized_line.split(" ") 
                 for normalized_line in [re.sub(r"\s+", " ", stripped_line) 
                           for stripped_line in [line.strip() 
                                     for line in self.input.readlines()]]]
        self.total_number_lines = len(lines)-1
        numbers = [[int(val) for val in line if val] for line in lines[:self.total_number_lines]]
        operands = lines[self.total_number_lines]
        self.problems = []
        for idx, operand in enumerate(operands):
            current_problem = []
            for line in numbers:
                current_problem.append(line[idx])
            current_problem.append(operand)
            self.problems.append(tuple(current_problem))

    def solve_problems(self):
        for problem in self.problems:
            operand = problem[self.total_number_lines]
            numbers = problem[:self.total_number_lines]
            if operand == "+":
                yield sum(numbers)
            if operand == "*":
                yield reduce(lambda x, y: x * y, numbers)

    def parse_part_2(self):
        self.input.seek(0)
        lines = self.input.readlines()

        operands = re.sub(r"([\*\+]\s+)(\s)",r"\1,", lines[-1]).split(",")[:-1]
        print(operands)



    def solve_part1(self):
        return sum(self.solve_problems())
    
    def solve_part2(self):
        self.parse_part_2()
        pass

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")
    