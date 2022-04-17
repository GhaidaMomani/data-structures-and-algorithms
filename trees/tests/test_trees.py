
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