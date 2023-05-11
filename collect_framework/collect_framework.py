"""This Collection Framework module"""
# from time import time
from functools import lru_cache


@lru_cache(typed=True, maxsize=1024)
def get_number_char(string: str) -> int:
    """function returns the number of characters in the string occurring only once"""
    return sum(1 for ch in string if string.count(ch) == 1)


def get_collection_number(strings: list[str] | tuple[str]) -> list:
    """function returns the number of characters in strings that occur only once"""
    return list(map(get_number_char, strings))


def do_collection_checks(collection: list | tuple | str) -> list:
    """function returns the numbers of characters in the collection"""
    match collection:
        case str(col) if col:
            return [get_number_char(col)]
        case list(col) | tuple(col) if col:
            if all(isinstance(item, str) and item for item in col):
                return get_collection_number(col)
    raise TypeError('--only not empty strings and collections of strings are expected--')


if __name__ == '__main__':
    # start = time()
    assert do_collection_checks("abbbccdf") == [3]
    # assert do_collection_checks('0') == [1]
    # assert do_collection_checks("wmmmmmmmwww") == [0]
    # assert do_collection_checks("Write an application that takes a string") == [7]
    # assert do_collection_checks(("abbbccdf", "abbbccdfA", '12345')) == [3, 4, 5]
    # assert do_collection_checks(["abbbccdf", "abbbccdfA", "Write an application that takes a string"]) == [3, 4, 7]
    # assert do_collection_checks(("abv", '0423-50', 'hdhdh73322', 'True', 'None')) == [3, 5, 1, 4, 4]
    #
    # end = time()
    # print(f'test time: {end - start} s.')
    # print(get_number_char.cache_info())
