import random

random_list = random.sample(range(0, 30), 15)


def get_second_max_elem(elements):
    first_max, second_max = None, None

    for el in elements:
        if first_max is None:
            first_max = el
            continue
        if second_max is None:
            second_max = el

        if el > second_max:
            second_max = el

        if second_max > first_max:
            second_max, first_max = first_max, second_max

    return second_max
