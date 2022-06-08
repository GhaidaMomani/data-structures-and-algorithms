##########################################################################
# Code Challenge 16

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