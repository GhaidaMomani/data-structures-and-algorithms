from linked_list.linked_list import LinkedList, Node



def test_kth_from_end_happy_path():
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5, 6]
    for el in elements:
        ll.insert(el)
    actual = ll.kth_from_end(4)
    expected = 5
    assert actual == expected


def test_kth_from_end_edge_case():
    "if the index was 0 which is the last node in the linked list"
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5, 6]
    for el in elements:
        ll.insert(el)
    actual = ll.kth_from_end(0)
    expected = 1
    assert actual == expected


def test_kth_from_end_expected_failure_one():
    "k > the length of the list"
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5, 6]
    for el in elements:
        ll.insert(el)
    actual = ll.kth_from_end(7)
    expected = "Location is greater than the length of LinkedList"
    assert actual == expected


def test_kth_from_end_expected_failure_two():
    "k > the length of the list"
    ll = LinkedList()
    data = [1, 2, 3, 4, 5, 6]
    for el in data:
        ll.insert(el)
    actual = ll.kth_from_end("this is a string")
    expected = "the index should be a positive integer value"
    assert actual == expected
