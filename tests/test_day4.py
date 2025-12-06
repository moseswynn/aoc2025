from src.day4.solution import PaperRollGrid

def test_check_grid():
    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    test_input = [l.strip() for l in test_input.split("\n") if l]
    expected_output = """..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x."""
    grid = PaperRollGrid(grid=test_input)
    result = grid.solve_grid(4)
    result_count = result.count("x")
    expected_count = expected_output.count("x")
    assert result_count == expected_count