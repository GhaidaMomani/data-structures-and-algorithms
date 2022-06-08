class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None
class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.is_empty():
            self.front, self.back = value, value
        else:
            self.back.pointer = value
            self.back = value

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue ")
        if self.front.value == self.back.value:
            value = self.front.value
            self.front, self.back = None, None
            return value

        temp = self.front
        self.front = self.front.pointer
        temp.pointer = None
        return temp.value 

    def is_empty(self):
        return self.front is None and self.back is None
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Input: None
        doing: traverse a tree (pre-order --> root-left-right)
        output: print values of the nodes of the tree
        """
        
        output = []
        def move(node):
            nonlocal output 
            output.append(node.value)

            if node.left:
                move(node.left)

            if node.right:
                move(node.right)

        move(self.root)
                
        return output
        
        
    def in_order(self):
        """
        Input: None
        doing: traverse a tree (in-order --> left-root-right)
        output: print values of the nodes of the tree
        """
        
        output = []
        def move(node):
            nonlocal output 

            if node.left:
                move(node.left)

            output.append(node.value)

            if node.right:
                move(node.right)
            
        move(self.root) 
        
        return list(output)
        
    
    def post_order(self):
        """
        Input: None
        doing: traverse a tree (post-order --> left-right-root)
        output: print values of the nodes of the tree
        """
        
        output = []
        def move(node):
            nonlocal output 

            if node.left:
                move(node.left)

            if node.right:
                move(node.right)
                
            output.append(node.value)
            
        move(self.root)
        
        return list(output)


    def find_max(self):
        """
        input: none
        doing: return the maximum value from the binary tree
        output: number 
        """
        
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        if not self.root.left and not self.root.right:
            return self.root.value

        max = self.root.value
                
        def move(node):
            nonlocal max 

            if node.value > max:
                max = node.value
            
            if node.left:
                move(node.left)

            if node.right:
                move(node.right)
                
        move(self.root)
        
        return max
    
                
class BinarySearchTree(BinaryTree):
    """
    a binary tree where each left node is less than its root, and each 
    right node is greater than its root 
    """
    
    def add(self, value):
        """
        input: value
        doing: add the value correctly to the tree
        output: None
        """
         
        current = self.root
        
        while True:
            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right                
            else:
                if value < current.value:
                    current.left = TNode(value)
                else:
                    current.right = TNode(value)
                break         
                
        
    def contains(self, value):
        """        
        input: value
        doing: check if the value is in the tree at least once
        output: boolean 
        """
        
        current = self.root
        
        while True:
            if current.value == value:
                return True
            
            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right                
            else:
                break
        
        return False
    
    
def breadth_first(tree):
    """
    input: tree
    doing: traverse the tree in a breadth-first manner
    output: list of values
    """
    
    if not tree.root:
        raise(Exception("Tree is empty !"))
    
    output = []
    q = Queue()
    q.enqueue(tree.root)

    while not q.is_empty():
        front = q.dequeue()
        output.append(front.value)
    
        if front.left:
            q.enqueue(front.left)

        if front.right:
            q.enqueue(front.right)
    
    return output

    
def fizz_buzz_tree(tree):
    """
    traversing through the tree and create a new one.
    Set the values of nodes according to the FizzBuzz game
    """
    
    if not tree.root:
        raise(Exception("Tree is empty !"))

    newTree = BinarySearchTree()
    newTree.root = tree.root 
        
    def move(node):
        
        if node.left:
            move(node.left)

        if node.right:
            move(node.right)
            
        if not str(node.value).isdigit(): 
            raise Exception("All values must be integers !")
        
        if node.value%3==0 and node.value%5==0:
            node.value = "FizzBuzz"
        elif node.value%5==0:
            node.value = "Buzz"
        elif node.value%3==0:
            node.value = "Fizz"
        else:
            node.value = str(node.value)

    move(newTree.root)
            
    return newTree
     
 
def odd_sum_tree(tree):
    """
    input: binary search tree
    doing: sum all odd numbers
    output: summation of odd numbers in the tree
    """
    
    if not tree.root:
        raise(Exception("Tree is empty !"))
    
    summation = 0
            
    def move(node):
        nonlocal summation 

        if node.value%2 != 0:
            summation += node.value
        
        if node.left:
            move(node.left)

        if node.right:
            move(node.right)
            
    move(tree.root)
    
    return summation


if __name__ == "__main__": 
    # pass
    tree = BinarySearchTree()
    tree.root = TNode(23) 
    [tree.add(i) for i in [8,4,16,15,22,42,27,85,105]]
    print(tree.pre_order()) 
    print(odd_sum_tree(tree))  
    
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())

    # nodeA = TNode("A")
    # nodeB = TNode("B")
    # nodeC = TNode("C")
    # nodeD = TNode("D")
    # nodeE = TNode("E")
    # nodeF = TNode("F")
    
    # nodeA.left = nodeB
    # nodeA.right = nodeC
    # nodeB.left = nodeD
    # nodeB.right = nodeE
    # nodeC.left = nodeF
        
    # tree = BinaryTree() 
    # tree.root = nodeA
    
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    
    
    
    