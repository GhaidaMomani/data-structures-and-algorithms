class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Solution:

    def __init__(self,seq):
        """prepends item of lists into linked list"""
        self.head = None
        for item in seq:
            node = Node(item)
            node.next = self.head
            self.head = node


    def palindrome(self):
        """ Check if linked list is palindrome and return True/False."""
        node = self.head
        var = node #var is initialized to head
        prev = None #initially, prev is None
    
        # prev approaches to middle of list till var reaches end or None 
        while var and var.next:
            var = var.next.next
            temp = node.next   #reverse elements of first half of list
            node.next = prev
            prev = node
            node = temp
    
        if var:  # in case of odd num elements
            tail = node.next 
        else:    # in case of even num elements
            tail = node
    
        while prev:
            # compare reverse element and next half elements          
            if prev.value == tail.value:
                tail = tail.next
                prev = prev.next
            else:
                return False
        return True

        
# Test Cases
list_1 = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
print([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7],end='->')
print(list_1.palindrome())
list_2 = Solution([6 , 3 , 4, 6])
print([6 , 3 , 4, 6],end='->')
print(list_2.palindrome())
list_3 = Solution([3, 7 ,3 ])
print([ 3 , 7, 3],end='->')
print(list_3.palindrome())
list_4 = Solution([1])
print([1],end='->')
print( list_4.palindrome())

