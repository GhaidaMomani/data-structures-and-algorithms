class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        self.storage.appendleft(value)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        return self.storage.pop()

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        return self.storage[-1]

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return len(self.storage) == 0

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Pre-order: root >> left >> right
        This is a Depth First traversal method. 
        It prioritizes printing the `root` first, 
        then looks to print `left` if left is not `None`, and lastly looks `right`.
        """
        collection = []

        def move(root):
            if not root:
                return

            
            collection.append(root.value)

            # <<< left
            move(root.left)

            # right >>>
            move(root.right)

        # end
        move(self.root)

        return collection


    def in_order(self):
        """
        In-order: left >> root >> right
        This is a Depth First traversal method. 
        It prioritizes printing the `left` first, then prints the `root`, 
        and lastly looks to print `right`.
        """
        collection = []

        def move(root):
            if not root:
                return

          
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                move(root.left)

            
            collection.append(root.value)

          
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                move(root.right)


        move(self.root)

        return collection

    def post_order(self):
        """
        Post-order: left >> right >> root
        This is a Depth First traversal method. It prioritizes print the left first,
         then looks to print the right and lastly prints the root.
         """
        collection = []

        def move(root):
            if not root:
                return

            
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                move(root.left)


           
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                move(root.right)

          
            collection.append(root.value)

       
        move(self.root)

        return collection

 

    def add(self, value):
       
        new_node = Node(value)
        breadth = Queue()
        breadth.enqueue(self.root)

        if not self.root:
            self.root = new_node
            return

        while not breadth.is_empty():
            front = breadth.dequeue()

            if not front.left:
                front.left = new_node
                return
            elif not front.right:
                front.right = new_node
                return

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

    def BT_max_val(self):
        """
        This instance method will traverse the tree and return the maximum value it has found.
        in the binary tree
        input: none
        output: number 
        """
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


#####################################################################################3
# CC 17
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






class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        The Binary search tree works in a manner where every element that is 
        to be inserted gets sorted then and there itself upon insertion.
        The comparison starts with the root,
         thereby following the left or right sub-tree depending if the value to be inserted is lesser or greater than root,
         respectively..
        """

        node = Node(value)

        if not self.root:
            self.root = node
            return

        def walk(root, new_node):

            if not root:
                return


            if new_node.value < root.value:

                if not root.left:
                    root.left = new_node
                else:
                    walk(root.left, new_node)

           
            else:
                if not root.right:
                    root.right = new_node
                else:
                    walk(root.right, new_node)

        walk(self.root, node)


    def contains(self, value):
        """
        This searches the tree in order to verify that a given value exists in the tree. Returns a boolean value.
        """
       
        if value in self.pre_order():
            return True
        else:
            return False


##########################################################################
# Code Challenge 16




    def BST_max_val(self):
            if not self.root:
                return "add some nodes to the tree :) "

            def move(root, max_val = 0):
                if not root:
                    return
                if root.value > max_val:
                    max_val = root.value

                left = move(root.left, max_val)
                right = move(root.right, max_val)

                if left and left > max_val:
                    max_val = left

                if right and right> max_val:
                    max_val = right


                return max_val

            return move(self.root)






if __name__=='__main__':  
          

    #  bt = BinarySearchTree() 
    #  [bt.add(i) for i in [0,5,10,15,20,25,30,35,40,45,50]]
    # print(bt.in_order())
    # print(bt.pre_order())

    # print(bt.post_order())

    # bt2 = BinarySearchTree()
    # [bt2.add(i) for i in [30,100,4,5,775,889,4,3]]

   
    bt= BinaryTree()
    n1= Node(2)
    n3= Node(3)
    n2= Node(50)
    print("hello")
    print(bt.BT_max_val())






