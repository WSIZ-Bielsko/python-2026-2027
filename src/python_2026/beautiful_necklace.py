def is_good(my_table_of_stars) -> bool:
    expected = len(my_table_of_stars[0])
    for pad in my_table_of_stars:
        if len(pad) > 0 and len(pad) != expected:
            return False
    return True


def is_beautiful(necklace: str) -> bool:
    necklace = necklace.strip('.')
    if len(necklace) ==0:
        return False
    pearls_good = is_good(necklace.split('.'))
    # change roles of '*' and '.'
    f = necklace.replace('*', '#')
    f = f.replace('.', '*')
    f = f.replace('#', '.')
    f = f.strip('.')
    dots_good = is_good(f.split('.'))
    print(f'{pearls_good=}, {dots_good=}')
    return pearls_good and dots_good


if __name__ == '__main__':
    # s = '**.***.******.***' # False
    s = '***.***.***.***' # True
    # s = '**.**..**'  # False

    print(is_beautiful(s))
