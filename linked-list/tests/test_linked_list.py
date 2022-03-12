from linked_list.linked_list import LinkedList , Node

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_Node_created():
    assert 3 == Node(3).value
    assert None == Node(3).next

def test_insert_to_empty():
    val = 5
    linked_list = LinkedList()
    linked_list.insert(val)
    assert linked_list.head.value == 5

def test_head_to_the_first_el():
   linked_list = LinkedList()
   linked_list.insert('a')
   assert linked_list.head.value == 'a'
   linked_list.insert('b')
   assert linked_list.head.value == 'b'
   linked_list.insert('c')
   assert linked_list.head.value == 'c'
   linked_list.insert('d')
   assert linked_list.head.value == 'd'
   assert linked_list.head.next.next.value == 'b'

"""
 creating a Linked list to run the next tests with a node as an array object 
"""

linked_list = LinkedList()
new_nodes = ['a', 'b', 5, 'df', ['t', 'r', 4]]
for node in new_nodes:
    linked_list.insert(node)

def test_includes_true():
    """
    Will return true when finding a value within the linked list that exists
    """
    assert linked_list.includes('df') == True
    assert linked_list.includes(['t','r', 4]) == True
    assert linked_list.includes('a') == True

def test_includes_false():
    """
    This test will return false when searching for a value in the linked list that does not exist
    """
    assert linked_list.includes('d4f') == False
    assert linked_list.includes([]) == False
    assert linked_list.includes(4) == False

# def test__str__method():
#     assert linked_list.__str__() == "['t', 'r', 4], df, 5, b, a"



def test__str__method():
    """
    Can properly return a collection of all the values that exist in the linked list

    formatted as:"{ a } -> { b } -> { c } -> NULL"

    """
    linkesl1=LinkedList()
    linkesl1.insert(" c ")
    linkesl1.insert(" b ")
    linkesl1.insert(" a ")
    actual = linkesl1.__str__()
    expected="head -> { a } -> { b } -> { c } -> NULL"
    assert actual==expected