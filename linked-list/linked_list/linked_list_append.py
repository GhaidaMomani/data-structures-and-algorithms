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


    def append(self, value):
        """method to append new node to the end of the list"""

        current = self.head
        while current:

            print(current.value)
            if current.next == None:
                current.next = Node(value)
                return self.__str__()
            else:
                current = current.next

        self.head = Node(value)
        return self.__str__()

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

    def insert_before(self, value, new_value):
        """method to insert new element before the given element of the list"""

        if self.includes(value):
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    return self.__str__()
                previous = current
                current = current.next
        else:
            return 'Value is not in the list'


    def insert_after(self, value, new_value):
        """method to insert new element after the given element of the list"""

        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next
        else:
            return 'Value is not in the list'

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
                elements += "{ " + f"{current.value}" + " } -> "
                current = current.next
            elements += "NULL"
            print (elements)
            return elements