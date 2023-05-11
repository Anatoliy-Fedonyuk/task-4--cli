"""This Collection Framework module"""
import click
from functools import lru_cache


@click.command()
@click.option('--string', help='The string to process', required=False)
@click.option('--file', type=click.Path(exists=True), help='The path to the input text file', required=False)
@lru_cache(typed=True, maxsize=1024)
def get_number_char(string: str, file: str) -> int:
    """The function returns the number of characters in a string that occur only once.
    The function also has a command line interface that allows you to enter as input text not only the line --string,
    but also the text file --file.  In this case, the --file command will take precedence!"""
    if file:
        with open(file, 'r') as f:
            string = f.read()
    if not string:
        raise ValueError("Either --string or --file must be provided.")
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
    print(get_number_char())

    # assert do_collection_checks("abbbccdf") == [3]
    # assert do_collection_checks(("abv", '0423-50', 'hdhdh73322', 'True', 'None')) == [3, 5, 1, 4, 4]
