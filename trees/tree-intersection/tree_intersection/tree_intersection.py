from hashtable  import HashTable
from binary_tree import BinaryTree,Node


def tree_intersection(tree1, tree2):
    """
   Takes two binary tree roots and will return a list of intersecting values, 
   or nodes that share the same value at the same position in the tree.
    """
    if tree1.root is None or tree2.root is None:
        raise Exception ("Empty Tree")

    
    hashtable = HashTable()

    def tree_traversal(root1,root2):
        if root1.value == root2.value:
            # intersections.append(root.value)
            hashtable.set(str(root1.value), True)
        if root1.left and root2.left:
            tree_traversal(root1.left,root2.left)
        if root1.right and root2.right:
            tree_traversal(root1.right,root2.right)
    tree_traversal(tree1.root,tree2.root)
    return set(hashtable.keys())


###################################
## Sloution 2
# we can use a queue to solve it !

# def tree_intersection(self, tree_1, tree_2):
#         """The function take two trees and loop through the tree_2 and compare it with tree_1
#         to get the intersecting values at the same location, tree_1 passed to the hash_tree function.
#         INPUT --> tree object
#         OUTPUT --> list of intersecting values
#         """
#         self._validate_trees([tree_1, tree_2])
#         self.hash_tree(tree_1)
#         self.counter = 1
#         result = []
#         queue = Queue()
#         queue.put(tree_2)
#         while not queue.empty():
#             front = queue.get()
#             key = f"{front.value}+{self.counter}"
#             tree_value = self.get(key)
#             if tree_value == front.value:
#                 result.append(front.value)
#             if front.left:
#                 queue.put(front.left)
#             if front.right:
#                 queue.put(front.right)
#             self.counter += 1
#         return result