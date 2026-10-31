

from random import randint, seed

seed(111)

n_close_pairs = 0

for i in range(10):
    x = randint(0,10) # 0 i 10 mogą się pojawić
    y = randint(0,10)
    d = (x**2 + y**2)**0.5
    if d < 10:
        n_close_pairs += 1
        print(f'{x=:2}, {y=:2}, {d=:.2f}')

print(f'n_close_pairs = {n_close_pairs}')