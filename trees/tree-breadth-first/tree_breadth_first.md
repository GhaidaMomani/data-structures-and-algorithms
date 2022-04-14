

# Challenge Summary

This challenge is about  a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encounter

## Whiteboard Process

![img](../../assets/tree_max_val.jpg)

## features 

1. [x] Can successfully instantiate an empty tree.
2. [x] Can successfully instantiate a tree with a single root node.
3. [x] Can successfully  add a left child and a right child to a single root node.
4. [x] Can successfully return a collection from a preorder traversal.
5. [x] Can successfully return a collection from an inorder traversal.
6. [x] Can successfully return a collection from a postorder traversal.

## Approach & Efficiency

All the functions within super class, pre, post, and in order functions are all utilzing recursion. This is not terrible as it will only invoke that function once per node. This gives us a O(n) efficiency. Space is a bit tricky we are creating lists for each method, O(1) and thats not counting the actually node or tree it self.

Breadth First, utilizes recursion as well as a queue. Adding and removing items with O(1) and the recursion is O(n).

## Solution

```python

    def breadth_first(self, tree):
        """Return values of breadth first search."""
        if self.root is None:
            return
        else:
            print(self.head),
            breadth_queue = Queue()
            breadth_queue(self.root)
        while breadth_queue is not None:
            current = breadth_queue.dequeue()
            if current.left:
                breadth_queue.queue.enqueue(current.left)
            if current.right:
                breadth_queue.queue.enqueue(current.right)
            print(current),
        return
  

```













<hr/>
<br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>
<p align="right">22, 13 April</p>