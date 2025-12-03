class BaseSolution:
    def __init__(self, input: str) -> None:
        self.input = open(input)

    def solve_part1(self):
        raise NotImplementedError("Implement this method in your solution.")
    
    def solve_part2(self):
        raise NotImplementedError("Implement this method in your solution.")