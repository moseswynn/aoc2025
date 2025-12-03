from src.day1.solution import Dial, DialDirections

def test_dial():
    dial = Dial(initial_value=5)
    assert dial.value == 5

def test_dial_rotate():
    dial = Dial()
    assert dial.value == 0
    dial.rotate(direction=DialDirections.LEFT,steps=5)
    assert dial.value == 5
    dial.rotate(direction=DialDirections.RIGHT, steps=5)
    assert dial.value == 0
    assert dial.history == [5,0]
    dial.rotate(DialDirections.RIGHT, 201)
    assert dial.zero_count == 3