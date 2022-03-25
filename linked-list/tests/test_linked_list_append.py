import pytest
from linked_list.linked_list_append import LinkedList, Node

linked_list = LinkedList()
values = ['a', 'b', 4, 'd']
for el in values:
    linked_list.insert(el)


# def test_append():
#     assert "head -> { d } -> { 4 } -> { b } -> { a } -> { 5 } -> NULL" == linked_list.append('5')

# def test_append_to_empty():
#     linked_list = LinkedList()
#     assert "head -> { 5 } -> NULL" == linked_list.append('5')

# def test_insert_before_value_in_list():

#     assert "head -> { d } -> { 4 } -> { b } -> { 3 } -> { a } -> { 7 } -> { 5 } -> NULL" == linked_list.insert_before('a', 3)

# def test_insert_before_value_not_in_list():

#     assert 'Value is not in the list' == linked_list.insert_before('e', 3)



# def test_insert_after_value_in_list():

#     assert "head -> { d } -> { 4 } -> { b } -> { 3 } -> { a } -> { 7 } -> { 5 } -> NULL"== linked_list.insert_after('a',7 )

# def test_insert_after_value_not_in_list():

#     assert 'Value is not in the list' == linked_list.insert_after('e', 3)



@pytest.fixture
def node():
    return Node(42)


@pytest.fixture
def ll():
    return LinkedList()


@pytest.fixture
def filled_ll():
    ll = LinkedList()
    ll.insert(42)
    ll.insert(14)
    ll.insert('October')
    return ll


def test_exists():
    assert LinkedList
    assert Node


def test_node_next(node):
    assert node.next == None


def test_node_value(node):
    assert node.value == 42


def test_ll_head(ll):
    assert ll.head == None


def test_ll_insert_one(ll):
    ll.insert(42)
    assert ll.head.value == 42


def test_ll_insert_two(ll):
    ll.insert(42)
    ll.insert(14)
    assert ll.head.value == 14
    assert ll.head.next.value == 42


def test_ll_insert_three(ll):
    ll.insert(42)
    ll.insert(14)
    ll.insert('October')
    assert ll.head.value == 'October'
    assert ll.head.next.value == 14
    assert ll.head.next.next.value == 42


def test_ll_includes(filled_ll):
    assert filled_ll.includes('October') == True
    assert filled_ll.includes(2001) == False
    # Edge Case: Checking an empty linked list
    assert LinkedList().includes('Towel') == False


def test_ll_append(ll, filled_ll):
    # Append Once
    ll.append(2)
    assert ll.head.value == 2

    # Append Multiple
    ll.append(4)
    assert ll.head.next.value == 4

    filled_ll.append(2)
    assert filled_ll.head.next.next.next.value == 2


def test_ll_insert_before(ll, filled_ll):
    # Empty List
    ll.insert_before(2, 6)
    assert ll.head == None

    # Single Item List
    ll.append(2)
    assert ll.head.value == 2
    ll.insert_before(2, 1)
    assert ll.head.value == 1

    #TEST CHANGED (before was ll.insert_before(1, 3))
    # NEED CLARIFICATION
    # Target Not Present
    ll.insert_before(9, 3)
    assert ll.head.value == 1

    ll.insert_before(1, 3)
    assert ll.head.value == 3

    ll.append(8)
    assert ll.head.value == 3
    assert ll.head.next.value == 1
  



    # Filled List
    filled_ll.insert_before(14, 'dell')
    assert filled_ll.head.next.value == 'dell'


def test_ll_insert_after(ll, filled_ll):
    # Empty List
    ll.insert_after(2, 6)
    assert ll.head == None

    # Single Item List
    ll.append(2)
    ll.insert_after(2, 1)
    assert ll.head.next.value == 1

    # Target Not Present
    ll.insert_after(3, 4)
    assert ll.head.value == 2
    assert ll.head.next.value == 1
    assert ll.head.next.next == None

    # Filled List
    filled_ll.insert_after(42, 'dell')
    assert filled_ll.head.next.next.next.value == 'dell'
