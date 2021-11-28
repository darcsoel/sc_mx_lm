import random

from main import get_second_max_elem


def test1():
    for _ in range(100):
        random_list = random.sample(range(0, 30), 15)
        print(random_list)
        assert get_second_max_elem(random_list) == list(reversed(sorted(random_list)))[1]


def test2():
    elems = [1, 29, 28, 24, 11, 8, 15, 10, 26, 13, 23, 20, 17, 0, 21]
    assert get_second_max_elem(elems) == 28
