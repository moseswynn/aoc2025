import os
import tomlkit

def main():
    solution_text = """
from ..base_solution import BaseSolution
import os

class Solution(BaseSolution):
    def __init__(self, input):
        super().__init__(input)
        
    def solve_part1(self):
        pass
    
    def solve_part2(self):
        pass

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")
    """
    current_dir = os.path.dirname(__file__)
    days = [int(n[-1]) for n in os.listdir(current_dir) if n.startswith("day")]
    next_day = f"day{max(days)+1}"
    next_day_path = os.path.abspath(os.path.join(current_dir, next_day))
    os.mkdir(next_day_path)
    solution_path = os.path.abspath(os.path.join(next_day_path, "solution.py"))
    with open(solution_path, "w+") as f:
        f.write(solution_text)
    with open("pyproject.toml") as f:
        doc = tomlkit.parse(f.read())
    
    doc["project"]["scripts"][next_day] = f"{next_day}.solution:main"
    with open("pyproject.toml", "w+") as f:
        f.write(tomlkit.dumps(doc))
