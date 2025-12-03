
from base_solution import BaseSolution
import os

class BatteryBank:
    def __init__(self, batteries: str) -> None:
        self.batteries = batteries

    def max_joltage(self, total_batteries: int) -> int:
        bank = self.batteries
        joltage = ""
        for i in range(total_batteries, 1, -1):
            if i == len(bank):
                joltage += bank
                break
            joltage += max(bank[:-i+1])
            position = bank.index(joltage[-1])
            bank = bank[position+1:]
        else:
            joltage += max(bank)
        return int(joltage)
    

class Solution(BaseSolution):
    def __init__(self, input):
        super().__init__(input)
        self.banks = [BatteryBank(bank.strip()) for bank in self.input.readlines()]
        
    def solve_part1(self):
        return sum([bank.max_joltage(2) for bank in self.banks])
    
    def solve_part2(self):
        return sum([bank.max_joltage(12) for bank in self.banks])

def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input.txt'))
    s = Solution(input_path)
    print(f"Part 1 Solution: {s.solve_part1()}")
    print(f"Part 2 Solution: {s.solve_part2()}")
    