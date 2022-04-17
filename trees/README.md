# Data Structures and Algorithms

## Code 401 - Advanced Software Development
<!-- This is the reading notes repository where I keep my favorite articles with their sources.
       
       Hope you'll benefit from my reads, Enjoy!
-->




By [Ghaida Al Momani] (https://github.com/GhaidaMomani).

>>>>>Welcome to Code 401.
<br/>
<hr/>
<br/>


# [PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/13)


 # Binary Tree and BST Implementation.






## Approach & Efficiency
* for method .pre_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .in_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .post_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .add() time big O(h) -height of the tree, space O(1)
* for contains .add() time big O(h) -height of the tree, space O(1)
* for breadth_first() method Time and space Big O(n)

## API
* _Node - Private class to create a nodes for the tree and also nodes for the Queue
* Queue - class to create a queue

* BinaryTree - Class to create a binary tree
* ----.pre_order() - BinaryTree method to return an array of trre values in "pre-order" order
* ----.in_order() - BinaryTree method to return an array of tree values "in-order"
* ----.post_order() - BinaryTree method to return an array of tree values "post-order
* ----.breadth_first - a BinaryTree static method which takes a Binary Tree as its unique input, traversing the input tree using a Breadth-first approach, and returns a list of the values in the tree in the order they were encountered.

* BinarySearchTree - Class to create a Binary Search Tree, inherits its properties from BinaryTree class
* ----.add(value) - BinarySearchTree method that accepts a value, and adds a new node with that value in the correct location in the binary search tree
* ----.contains(value) - BinarySearchTree method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.



# Features and tasks 

- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [x] For a Binary Search Tree, can successfully add a - [x] left child and right child properly to a node
- [x] Can successfully return a collection from a preorder traversal
- [x] Can successfully return a collection from an inorder traversal
- [x] Can successfully return a collection from a postorder traversal



<hr/>
<br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>
<p align="right">22, 10 April