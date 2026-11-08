


def get_number_of_packages(package_size: int, total_size_needed: int) -> int:
    if total_size_needed % package_size == 0:
        return total_size_needed // package_size
    else:
        return total_size_needed // package_size + 1



def sol_2d(package_x, package_y, total_x, total_y):
    return min(get_number_of_packages(package_x, total_x) * get_number_of_packages(package_y, total_y),
               get_number_of_packages(package_x, total_y) * get_number_of_packages(package_y, total_x))


if __name__ == '__main__':
    print(get_number_of_packages(10, 99))
