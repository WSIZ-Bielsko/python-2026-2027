from random import randint, seed

seed(42)

def get_random_rods(n_elems) -> list[int]:
    res = []
    for _ in range(n_elems):
        res.append(randint(1,100))
    return res



if __name__ == '__main__':
    # zadanie - sprawdzic czy z wylosowanej listy mozna stworzyc pret dlugosic 50
    ...