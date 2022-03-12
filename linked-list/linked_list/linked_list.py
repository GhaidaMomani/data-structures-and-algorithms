
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

    def append(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

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

    def includes(self, value):
        """
        method to check if the given value in the liked list
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        """
        method that returns a string that represents all list elements
         formatted as:
           "{ a } -> { b } -> { c } -> NULL"
        """
        elements = "head -> "
        if self.head is None:
            elements += "NULL"
        else:
            current = self.head
            while current:
                elements += "{" + f"{current.value}" + "} -> "
                current = current.next
            elements += "NULL"
            return elements
    
 
# def printLL(self):
#         "adds the values of the nodes in the linked list to an array"
#         current = self.head
#         data=[]
#         while(current):
#             data.append(current.data)
#             current = current.next
#         print(data)
#         return data



# def size(self):
#         """
#         returns the size of the linked list "how many node is in the list"
#         """
#         current = self.head
#         count = 0
#         while current:
#             count += 1
#             current = current.get_next()
#         print(count)
#         return count