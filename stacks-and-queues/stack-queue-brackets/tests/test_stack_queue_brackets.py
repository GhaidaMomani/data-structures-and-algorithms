import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_mbv_exists():
    assert validate_brackets('test')

def test_mbv_one():
    string = '{}'
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_mbv_two():
    string = '{}(){}'
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_mbv_three():
    string = '()[[Extra Characters]]'
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_mbv_four():
    string = '(){}[[]]'
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_mbv_five():
    string = '{}{Code}[Fellows](())'
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_mbv_six():
    string = '[({}]'
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_mbv_seven():
    string = '(]('
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_mbv_eight():
    string = '{(})'
    actual = validate_brackets(string)
    expected = False
    assert actual == expected