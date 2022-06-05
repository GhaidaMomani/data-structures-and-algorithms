import pytest
from tree_intersection.binary_tree import BinaryTree,Node
from tree_intersection.tree_intersection import tree_intersection

def test_tree_intersection(t1,t2):

    actual = tree_intersection(t1,t2)
    expected = {'0', '10', '2', '6'}
    assert actual == expected


def test_tree_intersection_fail():
    with pytest.raises(Exception):
        tree_intersection(BinaryTree(),BinaryTree())



def test_tree_intersection3(t3,t4):
    actual = tree_intersection(t3,t4)
    expected = {'6'}
    assert actual == expected





@pytest.fixture
def t1():
    bt1 = BinaryTree()
    bt1.root = Node(6)
    bt1.root.right = Node(9)
    bt1.root.left = Node(2)
    bt1.root.left.left = Node(0)
    bt1.root.right.left = Node(10)
    return bt1

@pytest.fixture    
def t2():

    bt2= BinaryTree()
    bt2.root = Node(6)
    bt2.root.right = Node(12)
    bt2.root.left = Node(2)
    bt2.root.left.left = Node(0)
    bt2.root.right.left = Node(10)

    return bt2
        

@pytest.fixture    
def t3():

    bt2 = BinaryTree()
    bt2.root = Node(6)

    return bt2


@pytest.fixture
def t4():
    bt1 = BinaryTree()
    bt1.root = Node(6)
    return bt1