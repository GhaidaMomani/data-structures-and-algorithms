class Node:
    """
     Class for the Node instances
     """
    
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    pass


class LinkedList:
    """
    Class for the LinkedList instances
    Upon instantiation, an empty Linked List should be created.
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        method to add a new node with that value to the head of the list with an O(1) Time performance.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

            
    def kth_from_end(self, k):
        """
        Return the node's value that is k places from the tail of the linked list.
        """
        temp = self.head
        length = 0
        if type(k)!= type(5) or k<0:
            print("the index should be a positive integer value")
            return "the index should be a positive integer value"
        while temp.next is not None:
            temp = temp.next
            length += 1
        if k > length:
            """
            if the entered number is bigger than the length of the linked list
            """
            print('Location is greater than the length of LinkedList')
            return 'Location is greater than the length of LinkedList'
        temp = self.head
        for i in range(0, length - k):
            temp = temp.next
        print(temp.value)
        return temp.value


    # def kth_from_end(self, k):
        
    #     ll= LinkedList()

    #     """
    #     This is the optimal solution!
    #     head -> [1] -> [3] -> [8] -> [2] -> X
    #     """
    #     if k < 0 or k >= ll.length:
    #         return "Error"
        
    #     count = ll.length - 1
    #     current = ll.head
    #     while current:
    #         if k == count:
    #             return current.value
    #         current = current.next
    #         count = count - 1


