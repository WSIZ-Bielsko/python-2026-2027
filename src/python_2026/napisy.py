def has_5_or_more(pad: str) -> bool:
    # return true if 5 or more stars are present in the pad
    # can assume only `.` and `*` are in the pad; length is >=1
    # return '*****' in pad
    # return '*****' in pad
    if '*****' in pad:
        return True

    stars_at_front = 0
    for x in pad:
        if x == '*':
            stars_at_front += 1
        else:
            break

    stars_at_back = 0
    for x in reversed(pad):
        if x == '*':
            stars_at_back += 1
        else:
            break

    if len(pad) >= 5 and (stars_at_front + stars_at_back >= 5):
        return True
    return False


import pytest


def test_exactly_5_consecutive():
    assert has_5_or_more("*****") is True


def test_4_consecutive():
    assert has_5_or_more("****.") is False


def test_all_dots():
    assert has_5_or_more(".....") is False


def test_all_stars_long():
    assert has_5_or_more("**********") is True


def test_single_dot():
    assert has_5_or_more(".") is False


def test_wrap_around_simple():
    assert has_5_or_more("**....***") is True


def test_wrap_around_exact():
    assert has_5_or_more("***..**") is True


def test_no_wrap_needed():
    assert has_5_or_more(".....*****....") is True


def test_split_not_enough():
    assert has_5_or_more("**...**") is False


def test_6_consecutive():
    assert has_5_or_more("......******......") is True


def test_scattered_stars():
    assert has_5_or_more("*.*.*.*.*.*.*") is False


def test_wrap_5_stars():
    assert has_5_or_more("***.......**") is True


def test_wrap_4_stars():
    assert has_5_or_more("**........**") is False


def test_all_stars_short():
    assert has_5_or_more("*****") is True


def test_long_mixed_true():
    assert has_5_or_more("..*.**.*****...") is True


def test_long_mixed_false():
    assert has_5_or_more("..*.**.****...") is False


def test_wrap_many_stars():
    assert has_5_or_more("****..........*") is True


def test_edge_single_stars_wrap():
    assert has_5_or_more("*...*") is False


def test_entire_wrap_split():
    assert has_5_or_more("*.****") is True


if __name__ == '__main__':
    s = '..*..**k***'
    print(type(s))
    print(s[-1])
    print(s.upper())

    # print('bra' in s)
    # s.startswith('kad')
    # s.endswith('bra')
