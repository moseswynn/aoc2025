from src.day3.solution import BatteryBank
import pytest

@pytest.fixture
def batterybanks():
    return [
        BatteryBank("987654321111111"),
        BatteryBank("811111111111119"),
        BatteryBank("234234234234278"),
        BatteryBank("818181911112111"),
    ]
    
def test_max_voltage(batterybanks):
    p1_joltages = [
        98,
        89,
        78,
        92
    ]
    p1_total = 357
    p2_joltages = [
        987654321111,
        811111111119,
        434234234278,
        888911112111
    ]
    p2_total = 3121910778619
    p1_results = list([bank.max_joltage(2) for bank in batterybanks])
    p2_results = list([bank.max_joltage(12) for bank in batterybanks])
    assert p1_results == p1_joltages
    assert sum(p1_results) == p1_total
    assert p2_results == p2_joltages
    assert sum(p2_results) == p2_total