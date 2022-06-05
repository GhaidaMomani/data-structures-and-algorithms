##########################################################################
# Code Challenge 16

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


