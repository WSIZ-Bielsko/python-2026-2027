import pytest


def count(elems: list[int], elem: int) -> int:
    # how many times elem is in elems
    # return elems.count(elem)
    cnt = 0
    for x in elems:
        if x == elem:
            cnt += 1
    return cnt


def give_change(coins: list[int], amount: int) -> list[int]:
    if amount in coins:
        return [amount]

    for coin in coins:
        if coin <= amount:
            still_needed = amount - coin
            if still_needed == coin and count(coins, coin) > 1:
                return [coin, coin]
            else:
                if still_needed in coins:
                    return [coin, still_needed]

    return [] # never happens


def _uses_available_coins(coins: list[int], result: list[int]) -> bool:
    pool = list(coins)
    for coin in result:
        if coin not in pool:
            return False
        pool.remove(coin)
    return True


def assert_valid(coins: list[int], amount: int, result: list[int]) -> None:
    assert isinstance(result, list)
    assert len(result) <= 2
    assert sum(result) == amount
    assert _uses_available_coins(coins, result)


@pytest.mark.parametrize(
    "coins, amount",
    [
        ([], 0),
        ([5], 0),
        ([7], 7),
        ([1, 4, 9], 4),
        ([3, 5], 8),
        ([10, 1, 2, 7], 9),
        ([5, 5], 10),
        ([5, 5, 5], 5),
        ([1, 2, 3], 3),  # [3] or [1, 2] both valid
        ([8, 1, 4, 3], 7),
        ([100, 50, 20], 70),
        ([2, 2, 2], 4),
    ],
)
def test_give_change_contract(coins, amount):
    assert_valid(coins, amount, give_change(coins, amount))


def test_does_not_mutate_input():
    coins = [1, 2, 3]
    snapshot = coins.copy()
    give_change(coins, 3)
    assert coins == snapshot


def test_each_coin_used_at_most_once():
    result = give_change([5, 5], 10)
    assert_valid([5, 5], 10, result)
    assert result == [5, 5]
