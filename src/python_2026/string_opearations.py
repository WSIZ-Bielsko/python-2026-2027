


if __name__ == '__main__':
    s = '***..***..***'
    n_stars = s.count('*')
    n_dots = s.count('.')

    print(n_stars, n_dots)  # --> wiemy ile jest gwiazdek i kropek

    g = s
    for i in range(100):
        g = g.replace('**', '*')
    star_groups = g.count('*')

    g = s
    for i in range(100):
        g = g.replace('..', '.')
    dot_groups = g.count('.')

    print(star_groups, dot_groups)
    expected_len_stars = n_stars // star_groups
    expected_len_dots = n_dots // dot_groups

    print('---')
    print(expected_len_stars, expected_len_dots)





