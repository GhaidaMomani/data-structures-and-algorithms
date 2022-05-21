import pytest
from hashtable.hashtable   import HashTable


def test_hash_a_key():
    myHash = HashTable(10)
    actual = myHash.hash('a')
    expected = 3
    assert actual == expected

def test_add_to_hashtable():
    myHash = HashTable(3)
    myHash.add('one item', 1)
    actual = myHash.contains('one item')
    expected = True
    assert actual == expected

def test_add_to_hashtable_multiple_items():
    myHash = HashTable(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual1 = myHash.contains('something')
    actual2 = myHash.contains('code')
    actual3 = myHash.contains('random')
    actual4 = myHash.contains('No in map!')
    expected = [True, True, True, False]
    assert [actual1, actual2, actual3, actual4] == expected

def test_get_key():
    myHash = HashTable(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual = myHash.get('random')
    expected = 42
    assert actual == expected

def test_get_key_2():
    myHash = HashTable(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual = myHash.get('code')
    expected = 99
    assert actual == expected

def test_get_key_invalid():
    myHash = HashTable(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual = myHash.get('FooBar!')
    expected = None
    assert actual == expected

def test_retrieve_from_bucket():
    myHash = HashTable(100)
    myHash.add('random', 10)
    myHash.add('rnadom', 42)
    actual1 = myHash.get('random')
    actual2 = myHash.get('rnadom')
    expected = [10, 42]
    assert [actual1, actual2] == expected
