
from base_solution import BaseSolution
import os

class PaperRollGrid:
    def __init__(self, grid: list[str]) -> None:
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def point_is_valid(self, point):
        x, y = point
        return all([
            x >= 0,
            y >= 0,
            x < self.width,
            y < self.height
        ])

    def check_adjacent_points(self, x, y, limit):
        if (value := self.grid[y][x]) == '@':
            adjacent_points = [
                (x, y+1),
                (x, y-1),
                (x+1,y),
                (x-1,y),
                (x+1, y+1),
                (x+1, y-1),
                (x-1, y+1),
                (x-1, y-1)
            ]
            adjacent_points = list(filter(self.point_is_valid, adjacent_points))
            adjacent_points = [self.grid[y_][x_] for x_, y_ in adjacent_points]
            return "x" if adjacent_points.count('@') < limit else value
        return value
    
    def solve_grid(self, limit):
        result = []
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.check_adjacent_points(x, y, limit)
            result.append(line)
        self.grid = result
        return "\n".join(result)
    
    def remove_all_rolls(self, limit):
        previous_grid = self.grid
        self.solve_grid(limit)
        if self.grid != previous_grid:
            self.remove_all_rolls(limit)



class Solution(BaseSolution):
    def __init__(self, input):
        super().__init__(input)
        grid = [l.strip() for l in self.input.readlines()]
        self.grid = PaperRollGrid(grid)
        
    def solve_part1(self):
        return self.grid.solve_grid(4).count("x")
    
    def solve_part2(self):
        self.grid.remove_all_rolls(4)
        return "\n".join(self.grid.grid).count("x")

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")
    