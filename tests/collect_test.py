"""--Pytest for module collect_framework--"""
import pytest
from collect_framework import collect_framework


def test_get_number_char():
    assert collect_framework.get_number_char("abbbccdf") == 3
    assert collect_framework.get_number_char("wmmmmmmmwww") == 0


def test_get_collection_number():
    assert collect_framework.get_collection_number(("abbbccdf", "abbbccdfA", '12345')) == [3, 4, 5]
    assert collect_framework.get_collection_number(["abbbccdf", " "]) == [3, 1]


def test_do_collection_checks():
    assert collect_framework.do_collection_checks("Write an application that takes a string") == [7]
    assert collect_framework.do_collection_checks(["abbbccdf", '#####!##################']) == [3, 1]
    assert collect_framework.do_collection_checks(("abv", '0423-50', 'hdhdh73322', 'True')) == [3, 5, 1, 4]


def test_empty_string():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks("")
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_empty_tuple():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(tuple())
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_empty_list():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks([])
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_empty_string_in_collection():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(["abv", '0423-50', 'hdhdh73322', 'True', ""])
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_type_none():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(None)
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_type_digit():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(33.99)
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_collection_set():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks({'wdsd', 'dsdfssd'})
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_type_bool_coll():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(('None', 'False', True))
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


def test_type_coll_in_coll():
    with pytest.raises(TypeError) as error:
        collect_framework.do_collection_checks(('None', ['1', '2', '3'], 'True'))
    assert '--only not empty strings and collections of strings are expected--' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
