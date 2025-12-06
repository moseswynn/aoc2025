from io import StringIO
import pytest
from day5.solution import Solution

@pytest.fixture
def data():
    return StringIO("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")

@pytest.fixture
def expected_ranges():
    return [(3,5),(10,14),(16,20),(12,18)]

@pytest.fixture
def expected_ids():
    return [1,5,8,11,17,32]

@pytest.fixture
def expected_consolidation():
    return [(3,5), (10, 20)]

def test_solution_init(data, expected_ranges, expected_ids):
    s = Solution(data)
    assert s.ranges == expected_ranges
    assert s.ids == expected_ids

def test_part1(data):
    s = Solution(data)
    assert s.solve_part1() == 3

def test_consolidation(data, expected_consolidation):
    s = Solution(data)
    assert s.consolidate_ranges() == expected_consolidation

def test_part2(data):
    s = Solution(data)
    assert s.solve_part2() == 14