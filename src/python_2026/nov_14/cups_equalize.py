


def equalize(cups: list[int]) -> list[int]:
    if len(cups) == 0:
        return []

    if sum(cups) % len(cups) != 0:
        raise ValueError("Cannot equalize cups with different total number of pearls")

    target_count = sum(cups) // len(cups)

    pearl_count_changes = []

    for cup in cups:
        pearl_count_changes.append(target_count - cup)

    return pearl_count_changes


def test_jeden_pusty_kubek():
    assert equalize([0]) == [0]


def test_jeden_kubek_z_kulkami():
    assert equalize([5]) == [0]


def test_dwa_juz_wyrownane_kubki():
    assert equalize([3, 3]) == [0, 0]


def test_trzy_puste_kubki():
    assert equalize([0, 0, 0]) == [0, 0, 0]


def test_cztery_juz_wyrownane_kubki():
    assert equalize([4, 4, 4, 4]) == [0, 0, 0, 0]


def test_dwa_kubki_mniej_w_pierwszym():
    assert equalize([1, 3]) == [1, -1]


def test_dwa_kubki_wiecej_w_pierwszym():
    assert equalize([3, 1]) == [-1, 1]


def test_dwa_kubki_jeden_pusty():
    assert equalize([0, 10]) == [5, -5]


def test_trzy_kubki_rozne_liczby_kulek():
    assert equalize([2, 7, 6]) == [3, -2, -1]


def test_trzy_kubki_srodkowy_juz_wyrownany():
    assert equalize([0, 3, 6]) == [3, 0, -3]


def test_trzy_kubki_odwrotna_kolejnosc():
    assert equalize([6, 3, 0]) == [-3, 0, 3]


def test_trzy_kubki_dwa_potrzebuja_kulek():
    assert equalize([1, 1, 7]) == [2, 2, -4]


def test_trzy_kubki_jeden_oddaje_kulki():
    assert equalize([8, 1, 3]) == [-4, 3, 1]


def test_cztery_kubki_dwa_puste():
    assert equalize([0, 0, 4, 4]) == [2, 2, -2, -2]


def test_cztery_kubki_jeden_juz_wyrownany():
    assert equalize([1, 2, 3, 6]) == [2, 1, 0, -3]


def test_piec_kubkow_cztery_puste():
    assert equalize([5, 0, 0, 0, 0]) == [-4, 1, 1, 1, 1]


def test_piec_kubkow_rosnaca_liczba_kulek():
    assert equalize([1, 2, 3, 4, 5]) == [2, 1, 0, -1, -2]


def test_piec_kubkow_naprzemiennie_puste():
    assert equalize([10, 0, 10, 0, 10]) == [-4, 6, -4, 6, -4]


def test_wieksze_liczby_kulek():
    assert equalize([100, 200, 300]) == [100, 0, -100]


def test_milion_kulek_w_jednym_kubku():
    assert equalize([1_000_000, 0]) == [-500_000, 500_000]
