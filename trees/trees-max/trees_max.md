# Challenge Summary

Find the maximum value stored in the tree. with assumption  that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![img](../../assets/tree_max_val.jpg)

## Approach & Efficiency
define an algorithm find_maximum() raise an exception if the tree is empty return the root value if the tree only have one node (the root) define (maximum) that holds the value of the root value define a recursive loop by a function that will traverse through the tree in each recursion, check if the current value is bigger than the current max and modify it accordingly return the maximum

Big-O is o(n) for time because the recursive internal function, and o(1) for space.

## Solution

```python

  def BT_max_val(self):
 
        if self.root == None:
            raise ValueError("fill the tree and try again")

        self.max = 0

        def move(root):
            if not root:
                return
            if root.value > self.max:
                self.max = root.value

            move(root.left)
            move(root.right)

        move(self.root)
        return self.max

```





<hr/>
<br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>
<p align="right">22, 13 April</p>