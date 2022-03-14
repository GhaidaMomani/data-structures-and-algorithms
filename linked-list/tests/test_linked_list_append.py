import pytest
from linked_list.linked_list import LinkedList, Node

linked_list = LinkedList()
values = ["a", "b", 4, "d"]
for el in values:
    linked_list.insert(el)


def test_insert_after():
    ll = LinkedList()
    data = [1, 2, 3, 4, 5, 6]
    for el in data:
        ll.insert(el)
    ll.insert_after(5, 10)
    actual = ll.printList()
    expected = [1, 2, 3, 4, 5, 10, 6]
    assert actual == expected
    ll.insert_after(6, 7)
    actual = ll.printList()
    expected = [1, 2, 3, 4, 5, 10, 6, 7]
    assert actual == expected


def test_insert_before():
    ll = LinkedList()
    data = [1, 2, 3, 4, 5, 6]
    for el in data:
        ll.insert(el)
    ll.insert_before_another(5, 10)
    actual = ll.printList()
    expected = [1, 2, 3, 4, 10, 5, 6]
    assert actual == expected
    ll.insert_before_another(6, 7)
    actual = ll.printList()
    expected = [1, 2, 3, 4, 10, 5, 7, 6]
    assert actual == expected


def test_append():
    ll = LinkedList()
    data = [1, 2, 3, 4, 5, 6]
    for el in data:
        ll.insert(el)
    ll.append(10)
    actual = ll.printList()
    expected = [1, 2, 3, 4, 5, 6, 10]
    assert actual == expected
