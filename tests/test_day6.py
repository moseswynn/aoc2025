from io import StringIO
import pytest
from day6.solution import Solution

@pytest.fixture
def data():
    return StringIO("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """)

@pytest.fixture
def expected_problems():
    return [
        (123, 45, 6, "*"),
        (328, 64, 98, "+"),
        (51, 387, 215,"*"),
        (64, 23, 314, "+")
    ]

@pytest.fixture
def solution(data):
    return Solution(data)

def test_init_solution(solution, expected_problems):
    assert solution.problems == expected_problems

def test_solve_problems(solution):
    assert tuple(solution.solve_problems()) == (33210, 490, 4243455, 401)

def test_part_1(solution):
    assert solution.solve_part1() == 4277556