import datetime
from random import randint


def ts():
    return datetime.datetime.now().timestamp()



if __name__ == '__main__':
    food = [randint(1,10**18) for _ in range(10**7)]
    st = ts()
    food = set(food)
    en = ts()
    print(f'duration: {en-st:.2f}s')