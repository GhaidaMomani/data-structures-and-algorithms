import pytest
from trees.trees import (
    Node,
    BinaryTree,
    BinarySearchTree
)

def test_BST_exists():
    assert BinaryTree()


def test_BST_single_root():
    bt = BinarySearchTree()
    bt.add(200)
    actual = bt.root.value
    expected = 200
    assert actual == expected

def test_BST_left_and_right():
    bt = BinarySearchTree()
    bt.add(10)
    bt.add(5)
    bt.add(15)
    right = bt.root.right.value
    expected_right = 15
    left = bt.root.left.value
    expected_left = 5
    assert right == expected_right
    assert left == expected_left

def test_BST_pre_order():
    bt = BinarySearchTree()
    [bt.add(i) for i in [5,10,15,20,25]]
    actual = bt.pre_order()
    expected = [5, 10, 15, 20, 25]
    assert actual == expected


def test_BST_in_order():
    bt = BinarySearchTree()
    [bt.add(i) for i in [0,5,10,15,20,25,30,35,40,45,50]]
    actual = bt.in_order()
    expected = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert actual == expected


def test_BST_post_order():
    bt = BinarySearchTree()
    [bt.add(i) for i in [0,5,10,15,20,25,30,35,40,45,50]]
    actual = bt.post_order()
    expected = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
    assert actual == expected

def test_BST_post_order_2():
    bt = BinarySearchTree()

    [bt.add(i) for i in [50,60,55,40,45]]
    actual = bt.post_order()
    expected = [45, 40, 55, 60, 50]
    assert actual == expected

def test_BST_contains_True():
    bt = BinarySearchTree()

    [bt.add(i) for i in [10,20,30,40,50]]
    actual = bt.contains(30)
    expected = True
    assert actual == expected

def test_BST_contains_False():
    bt = BinarySearchTree()
    [bt.add(i) for i in [10,20,30,40,50]]

    actual = bt.contains(200)
    expected = False
    assert actual == expected


def test_BST_find_max():
    bt = BinarySearchTree()
    [bt.add(i) for i in [10,20,30,40,50]]

    actual = bt.BST_max_val()
    expected =50
    assert actual == expected 
    
 

def test_BST_find_max_empty():
    bt = BinarySearchTree()
   # [bt.add(i) for i in [10,20,30,40,50]]

    actual = bt.BST_max_val()
    expected = "add some nodes to the tree :) "
    assert actual == expected 

#############################################################3

def test_find_max_value(binay_tree):
        assert binay_tree.BT_max_val() == 300

def test_find_max_value_on_empty_tree():
    with pytest.raises(Exception):
        BinaryTree().BT_max_val()


@pytest.fixture
def binay_tree():
    node1 = Node(100)
    node2 = Node(100)
    node3 = Node(100)
    node4 = Node(100)
    node5 = Node(100)
    node6 = Node(300)
    node7 = Node(200)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.right= node7
        
    tree = BinaryTree() 
    tree.root = node1
    return tree