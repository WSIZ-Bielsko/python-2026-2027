from random import randint, seed
seed(42)  # ustalenie pocztku dla liczb "pseudolosowych"


# function in python
def add(a,b) -> int:
    a += 1
    return a + b

def greater(a,b) -> bool:
    return a > b


# print(add(1,2))
# print(greater(11,2))


def check_licence_duplicates(n_elems: int, mi_val: int = 0, mx_val:int = 9999) -> bool:
    licences = []
    for i in range(n_elems):
        new_one = randint(mi_val,mx_val)
        if new_one in licences:
            return True
        licences.append(new_one)
    return False


def check_stats_on_experiment(n_exps = 1000) -> float:
    n_duplicates = 0
    for i in range(n_exps):
        if check_licence_duplicates(200, 0, 9999):
            n_duplicates += 1
    return n_duplicates / n_exps


if __name__ == '__main__':
    res = check_stats_on_experiment(n_exps=100_000)
    print(f'szansa duplikatu: {100 * res:.2f}%')
