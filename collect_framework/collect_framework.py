"""This Collection Framework module"""
from functools import lru_cache
import click


@lru_cache(typed=True, maxsize=1024)
def get_number_char(string: str) -> int:
    """The function returns the number of characters in a string that occur only once"""
    return sum(1 for ch in string if string.count(ch) == 1)


@click.command()
@click.option('--string', '-s', help='The string to process')
@click.option('--file', '-f', type=click.Path(exists=True), help='The path to the input text file')
def main(string: str, file: str) -> None:
    """This function implements the command line interface for the function get_number_char.
    In this case, the --file command will take precedence!"""
    if not string and not file:
        return click.secho('Either --string or --file must be provided!', bg='bright_white', fg='black')
    if file:
        with open(file, encoding='utf-8') as f:
            string = f.read()

    result = get_number_char(string=string)
    click.secho(f'THERE ARE {result} UNIQUE CHARACTERS IN THIS TEXT!', bg='bright_white', fg='black')


def get_collection_number(strings: list[str] | tuple[str]) -> list:
    """function returns the number of characters in st rings that occur only once"""
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
    main()
    assert do_collection_checks(("abbbccdf", "abbbccdfA", '12345')) == [3, 4, 5]
    assert do_collection_checks("wmmmmmmmwww") == [0]
