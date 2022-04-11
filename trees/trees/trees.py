class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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







if __name__=='__main__':        
    tree = BinarySearchTree() 
    [tree.add(i) for i in [0,5,10,15,20,25,30,35,40,45,50]]
    print(tree.in_order())
    print(tree.pre_order())

    print(tree.post_order())









