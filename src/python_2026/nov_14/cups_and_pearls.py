


def can_equalize(cups: list[int]) -> bool:
    if len(cups) == 0:
        return True
    n_cups = len(cups)
    n_pearls = sum(cups)
    return n_pearls % n_cups == 0



def test_example_not_divisible():
    assert can_equalize([2, 7, 4]) is False

def test_simple_divisible():
    assert can_equalize([1, 2, 3]) is True

def test_single_cup():
    assert can_equalize([5]) is True

def test_already_equal():
    assert can_equalize([3, 3, 3]) is True

def test_all_empty_cups():
    assert can_equalize([0, 0, 0]) is True

def test_all_balls_in_one_cup():
    assert can_equalize([0, 0, 9]) is True

def test_two_cups_odd_sum():
    assert can_equalize([1, 2]) is False

def test_one_ball_two_cups():
    assert can_equalize([0, 1]) is False

def test_large_numbers():
    assert can_equalize([10**9, 10**9 + 2]) is True

def test_many_cups_off_by_one():
    assert can_equalize([1] * 99 + [2]) is False  # 101 / 100

def test_no_cups():
    assert can_equalize([]) is True